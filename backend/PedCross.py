import random 
import math

ZEBRA_AREA_WIDTH = 300 #cm
ZEBRA_AREA_LENGTH = 1000 #cm

PED_WALKING_VELOCITY_MIN = 110 #cm/s
PED_WALKING_VELOCITY_MAX = 140 #cm/s
WHEELCHAIR_ROLLING_VELOCITY_MIN = 70 #cm/s
WHEELCHAIR_ROLLING_VELOCITY_MAX = 100 #cm/s
CRUTCHES_USER_WALKING_VELOCITY_MIN = 50 #cm/s
CRUTCHES_USER_WALKING_VELOCITY_MAX = 80 #cm/s

RADIUS_OF_SPACE_OCCUPIED = {
    "ped": 50, #cm
    "wheelchair": 70, 
    "crutches_user": 90
}

class Ped:
    def __init__(self, type: str, direction: str):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = type # one of {"ped", "wheelchair", "crutches_user", "child"}
        self.velocity = self.get_rand_velocity(type)
        self.direction = direction # one of {"left2right", "right2left"}
        self.radius = RADIUS_OF_SPACE_OCCUPIED[type]

    def get_rand_velocity(self, type) -> int:
        if type == "ped":
            return random.randrange(PED_WALKING_VELOCITY_MIN, PED_WALKING_VELOCITY_MAX)
        elif type == "wheelchair":
            return random.randrange(WHEELCHAIR_ROLLING_VELOCITY_MIN, WHEELCHAIR_ROLLING_VELOCITY_MAX)
        elif type == "crutches_user":
            return random.randrange(CRUTCHES_USER_WALKING_VELOCITY_MIN, CRUTCHES_USER_WALKING_VELOCITY_MAX)

    def is_inside_zebra(self) -> bool:        
        if (self.x >= 0 and self.x <= ZEBRA_AREA_LENGTH) and (self.y >= 0 and self.y <= ZEBRA_AREA_WIDTH):
            return True
        return False

    def is_newspace_conflict(self, newx: int, newy: int, others: 'Ped[]') -> 'Ped[]':
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



# class Utilities:
#     @staticmethod
    
