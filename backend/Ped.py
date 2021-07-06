import random 
import numpy as np
import math
import global_params.global_params as global_params



class Ped:
    def __init__(self, type: str, direction: str, params):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = type # one of {"ped", "wheelchair", "crutches_user", "child", "elder"}
        self.direction = direction # one of {"left2right", "right2left"}
        self.velocity = self.set_velocity(type)
        self.radius = params.radius_of_space_occupied[type]

        self.set_initial_standing_position()
        


    def set_velocity(self, type, params) -> int:
        if type == "ped":
            return np.random.normal(params.ped_walking_velocity_mean, params.ped_walking_velocity_sigma, 1)[0]
        elif type == "wheelchair":
            return np.random.normal(params.wheelchair_rolling_velocity_mean, params.wheelchair_rolling_velocity_sigma, 1)[0]
        elif type == "crutches_user":
            return np.random.normal(params.crutches_user_walking_velocity_mean, params.crutches_user_walking_velocity_sigma, 1)[0]
        elif type == "child":
            return np.random.normal(params.children_walking_velocity_mean, params.children_walking_velocity_sigma, 1)[0]
        elif type == "elder":
            return np.random.normal(params.elder_walking_velocity_mean, params.elder_walking_velocity_sigma, 1)[0]

    def set_initial_standing_position(self, params):
        x_offset = abs(np.random.normal(params.waiting_area_position_x_offset_mean, params.waiting_area_position_x_offset_sigma, 1)[0])
        if self.direction == "left2right":
            self.x = params.waiting_area_length - x_offset
        elif self.direction == "right2left":
            self.x = params.waiting_area_length + params.crosswalk_length + x_offset
        
        self.y = np.random.normal(params.waiting_area_position_y_mean, params.waiting_area_position_y_sigma, 1)[0]

    def is_inside_crosswalk(self, params) -> bool:        
        if (self.x >= params.waiting_area_length and self.x <= params.waiting_area_length+params.crosswalk_length) and (self.y >= 0 and self.y <= params.crosswalk_width):
            return True
        return False

    def is_newposition_conflict(self, newx: int, newy: int, others: 'Ped[]', , params) -> 'Ped[]':
        # newx = self.x + self.velocity if self.direction == "left2right" else self.x - self.velocity
        conflict = []
        for another in others:
            distance = math.sqrt((newx - another.x)^2 + (newy - another.y)^2)
            if (distance <= self.radius + another.radius):
                conflict.append(another)
        return conflict
    

    # def move_one_second(self):
    #     newx = self.x + self.velocity if self.direction == "left2right" else self.x - self.velocity
    #     newy = self.y
    #     if (is_newspace_conflict(newx, newy, ))
    #     if self.direction == "left2right":
    #         self.x = self.x + self.velocity


