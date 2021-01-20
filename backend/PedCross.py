import random 

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
    def __init__(self, type: string, direction: string):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = type # one of {"ped", "wheelchair", "crutches_user", "child"}
        self.velocity = self.get_rand_velocity(type)
        self.direction = direction # one of {"left2right", "right2left"}
        self.radius = RADIUS_OF_SPACE_OCCUPIED[type]

    
    def get_rand_velocity(self, type):
        if type == "ped":
            return random.randrange(PED_WALKING_VELOCITY_MIN, PED_WALKING_VELOCITY_MAX)
        elif type == "wheelchair":
            return random.randrange(WHEELCHAIR_ROLLING_VELOCITY_MIN, WHEELCHAIR_ROLLING_VELOCITY_MAX)
        elif type == "crutches_user":
            return random.randrange(CRUTCHES_USER_WALKING_VELOCITY_MIN, CRUTCHES_USER_WALKING_VELOCITY_MAX)

    def is_inside_zebra(self):        
        if (self.x >= 0 and self.x <= ZEBRA_AREA_LENGTH) and (self.y >= 0 and self.y <= ZEBRA_AREA_WIDTH):
            return True
        return False

    def move_one_second(self):
        


