import PedCross
import operator


PED_L2R_SIZE = 30
WHEELCHAIR_L2R_SIZE = 1
CRUTCHES_USER_L2R_SIZE = 1

all_peds = list()

for i in range(0, PED_L2R_SIZE):
    all_peds.append(PedCross.Ped("ped", "left2right"))
    print(all_peds[i].x, all_peds[i].y, all_peds[i].type, all_peds[i].velocity, all_peds[i].direction, all_peds[i].radius)

total_size = PED_L2R_SIZE + WHEELCHAIR_L2R_SIZE + CRUTCHES_USER_L2R_SIZE
print("total_size: ", total_size, " ", len(all_peds))

all_peds_sorted_by_y = sorted(all_peds, key=operator.attrgetter('y'), reverse=True)
for i in range(total_size):
    newx = all_peds_sorted_by_y[i].x + all_peds_sorted_by_y[i].velocity 
    newy = all_peds_sorted_by_y[i].y
    conflict = all_peds_sorted_by_y[i].is_newspace_conflict(newx, newy , all_peds_sorted_by_y[:i])
    if (len(conflict) == 0):
        all_peds_sorted_by_y[i].x = newx
        all_peds_sorted_by_y[i].y = newy
    else:
        find a new space
