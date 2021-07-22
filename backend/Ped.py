
import numpy as np
import math



class Ped:
    def __init__(self, type: str, direction: str, params):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = type # one of {"ped", "wheelchair", "crutches_user", "child", "elder"}
        self.direction = direction # one of {"left2right", "right2left"}
        self.speed = self.set_speed(type, params)
        self.radius_standing = params.radius_of_space_occupied_when_standing[type]
        self.radius_moving = params.radius_of_space_occupied_when_moving[type]
        self.status = "standing" # one of {"standing", "moving", "finished"}

        self.previousx = 0
        self.previousy = 0

        self.set_initial_standing_position(params)
        


    def set_speed(self, type, params) -> int:
        if type == "ped":
            return np.random.normal(params.ped_walking_speed_mean, params.ped_walking_speed_sigma, 1)[0]
        elif type == "wheelchair":
            return np.random.normal(params.wheelchair_rolling_speed_mean, params.wheelchair_rolling_speed_sigma, 1)[0]
        elif type == "crutches_user":
            return np.random.normal(params.crutches_user_walking_speed_mean, params.crutches_user_walking_speed_sigma, 1)[0]
        elif type == "child":
            return np.random.normal(params.children_walking_speed_mean, params.children_walking_speed_sigma, 1)[0]
        elif type == "elder":
            return np.random.normal(params.elder_walking_speed_mean, params.elder_walking_speed_sigma, 1)[0]

    def set_initial_standing_position(self, params):
        is_conflict = True
        newx = 0
        newy = 0
        while is_conflict:
            x_offset = abs(np.random.normal(params.waiting_area_position_x_offset_mean, params.waiting_area_position_x_offset_sigma, 1)[0])
            if self.direction == "left2right":
                newx = params.waiting_area_length - x_offset
            elif self.direction == "right2left":
                newx = params.waiting_area_length + params.crosswalk_length + x_offset
            newy = np.random.normal(params.waiting_area_position_y_mean, params.waiting_area_position_y_sigma, 1)[0]
            if newx < 0 or newx > params.waiting_area_length + params.crosswalk_length + params.waiting_area_length: # outside, so drop
                is_conflict = True
                continue

            #check whether conflict with existing params.all_peds_lr or params.all_peds_rl
            if self.direction == "left2right":
                if not self.is_newposition_conflicted(newx, newy, "standing", params):
                    is_conflict = False
            elif self.direction == "right2left":
                if not self.is_newposition_conflicted(newx, newy, "standing", params):
                    is_conflict = False
        
        self.x = newx
        self.y = newy

    def is_inside_crosswalk(self, params) -> bool:        
        if (self.x >= params.waiting_area_length and self.x <= params.waiting_area_length+params.crosswalk_length) and (self.y >= 0 and self.y <= params.crosswalk_width):
            return True
        return False

    def is_newposition_conflicted(self, newx: int, newy: int, mode: str, params) -> bool:
        used_all_peds = 0
        if mode == "standing":
            if self.direction == "left2right":
                used_all_peds = params.all_peds_lr 
            elif self.direction == "right2left":
                used_all_peds = params.all_peds_rl 
        if mode == "moving":
            used_all_peds = params.all_peds
        
        for another in used_all_peds:
            if mode == "moving" and (another.status == "finished"):
                continue
            if another.status == self.status and another.x == self.x and another.y == self.y and another.direction == self.direction and another.speed == self.speed:
                continue
            if "debug" in params.log_keywords: print("is_newposition_conflicted another: ", another.status)
            distance = math.sqrt((newx - another.x)**2 + (newy - another.y)**2)
            radius_sum = 0
            if mode == "standing":
                radius_sum = self.radius_standing + another.radius_standing
            elif mode == "moving":
                radius_sum = self.radius_moving + another.radius_moving
            if "debug" in params.log_keywords: print("curr: ", self.x, " ", self.y, " another: ", another.x, " ", another.y)
            if "debug" in params.log_keywords: print("radius_sum: ", radius_sum, " distance: ", distance)
            if (distance < radius_sum):
                return True
        return False

    def generate_100_newpositions(self, params, counter):
        all_newpositions = list()
        farthest_newx = (self.x + self.speed * params.step_time) if self.direction == "left2right" else (self.x - self.speed * params.step_time)
        farthest_newy = self.y
        all_newpositions.append([farthest_newx, farthest_newy])
        if "debug" in params.log_keywords: print("-----------\nfarthest_newx, farthest_newy:  ",  farthest_newx, farthest_newy)

        offset = self.speed * params.step_time / 100
        for i in range(1 + counter, 99):
            newx = farthest_newx - offset * i if self.direction == "left2right" else farthest_newx + offset * i
            circle_radius_sq = (self.speed * params.step_time - offset * counter) ** 2
            x_x0_sq = (newx - self.x)**2
            if "debug" in params.log_keywords: 
                print("-----------\nself.speed:  ",self.speed)
                print("self.speed * params.step_time: ", self.speed * params.step_time)
                print("newx : ", newx, " self.x: ", self.x )
                print("circle_radius_sq : ", circle_radius_sq )
                print("x_x0_sq: ",  x_x0_sq)
                print("circle_radius_sq - x_x0_sq: ", circle_radius_sq - x_x0_sq)
            if circle_radius_sq - x_x0_sq < 0: # this case is weired and should not happen in theory but it happens rarely. Guess it is becuase precision error.
                continue
            sqrt_abs = math.sqrt(circle_radius_sq - x_x0_sq)
            newy1 = sqrt_abs + self.y
            newy2 = 0 - sqrt_abs + self.y
            if "debug" in params.log_keywords: 
                print("sqrt_abs: ", sqrt_abs, " self.y: ", self.y)
                print("newy1: ", newy1, " newy2: ", newy2)
            if self.y > params.crosswalk_width / 2:
                all_newpositions.append([newx, newy2])
                all_newpositions.append([newx, newy1])
            else:
                all_newpositions.append([newx, newy1])
                all_newpositions.append([newx, newy2])
        return all_newpositions



    def move_one_step(self, params):
        if self.direction == "left2right" and self.x > params.crosswalk_length + params.waiting_area_length:
            self.status = "finished"
            return
        if self.direction == "right2left" and self.x < params.waiting_area_length:
            self.status = "finished"
            return
        
        self.previousx = self.x
        self.previousy = self.y
        counter = 0
        while counter >= 0 and counter < 99:
            all_newpositions = self.generate_100_newpositions(params, counter)
            if "debug" in params.log_keywords: 
                for newx, newy in all_newpositions:
                    print("all_newpositions pos: ", newx, newy)
            for newx, newy in all_newpositions:
                if not self.is_newposition_conflicted(newx, newy, "moving", params):
                    if "debug" in params.log_keywords: print("\nFOUND!!\nold pos: ", self.x, self.y)
                    self.x = newx
                    self.y = newy
                    self.status = "moving" # move as designed
                    if "debug" in params.log_keywords: 
                        print("newx newy: ", newx, newy)
                        print("new pos: ", newx, newy)
                    return
            counter += 1
            # print("counter: ", counter)
        self.status = "moving" #  no place to move so stay


    
