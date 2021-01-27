import PedCross
from Circles import Circles
import operator


PED_L2R_SIZE = 30
WHEELCHAIR_L2R_SIZE = 1
CRUTCHES_USER_L2R_SIZE = 1

SIMU_STEP_TIME = 1 


all_peds = list()

for i in range(0, PED_L2R_SIZE):
    all_peds.append(PedCross.Ped("ped", "left2right"))
    print(all_peds[i].x, all_peds[i].y, all_peds[i].type, all_peds[i].velocity, all_peds[i].direction, all_peds[i].radius)

total_size = PED_L2R_SIZE + WHEELCHAIR_L2R_SIZE + CRUTCHES_USER_L2R_SIZE
print("total_size: ", total_size, " ", len(all_peds))

# all_peds_sorted_by_y = sorted(all_peds, key=operator.attrgetter('y'), reverse=True)
all_peds_sorted_by_y = sorted(all_peds, key=operator.attrgetter('y'))
print(all_peds_sorted_by_y, "\n")

for i in range(total_size):
    newx = all_peds_sorted_by_y[i].x + all_peds_sorted_by_y[i].velocity 
    newy = all_peds_sorted_by_y[i].y
    conflict = all_peds_sorted_by_y[i].is_newspace_conflict(newx, newy , all_peds_sorted_by_y[i+1:])
    print("conflict: ", len(conflict))
    if (len(conflict) == 0):
        all_peds_sorted_by_y[i].x = newx
        all_peds_sorted_by_y[i].y = newy
    else:
        for in_front_ped in all_peds_sorted_by_y[i+1:]:
            print("test: ", Circles.get_intersections(1,1,1,2,1,1), "\n")
            intersection = Circles.get_intersections(all_peds_sorted_by_y[i].x, all_peds_sorted_by_y[i].y, all_peds_sorted_by_y[i].velocity * SIMU_STEP_TIME, in_front_ped.x, in_front_ped.y, in_front_ped.radius + all_peds_sorted_by_y[i].radius)
            print(intersection)
            newx = intersection[2]
            newy = intersection[3]
            conflict = all_peds_sorted_by_y[i].is_newspace_conflict(newx, newy , all_peds_sorted_by_y[:i])
            print(conflict)
            if (len(conflict) == 0):
                all_peds_sorted_by_y[i].x = newx
                all_peds_sorted_by_y[i].y = newy
