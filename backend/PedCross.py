import random 

ZEBRA_AREA_WIDTH = 300 #cm
ZEBRA_AREA_LENGTH = 1000 #cm

PED_WALKING_VELOCITY_MIN = 110 #cm/s
PED_WALKING_VELOCITY_MAX = 140 #cm/s

class Ped:
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = "ped" # one of {"ped", "wheelchair", "crutches_user", "child"}
        self.velocity = random.randrange(PED_WALKING_VELOCITY_MIN, PED_WALKING_VELOCITY_MAX)
        self.direction = "left2right" # one of {"left2right", "right2left"}
    
    def is_inside_zebra(self):        
        if (self.x >= 0 and self.x <= ZEBRA_AREA_LENGTH) and (self.y >= 0 and self.y <= ZEBRA_AREA_WIDTH):
            return True
        return False




