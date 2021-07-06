import backend.Ped as Ped
from backend.Circles import Circles as Circles
import operator
import global_params.global_params as global_params

SIMU_STEP_TIME = 1 



#
# Initial
#

params = global_params.global_params()

print("Parameters applied!\ncrosswalk_width: ", params.crosswalk_width)
print("crosswalk_length: ", params.crosswalk_length)


for i in range(0, params.ped_amount_lr):
    params.all_peds_lr.append(Ped.Ped("ped", "left2right", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.wheelchair_amount_lr):
    params.all_peds_lr.append(Ped.Ped("wheelchair", "left2right", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.crutches_user_amount_lr):
    params.all_peds_lr.append(Ped.Ped("crutches_user", "left2right", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.children_amount_lr):
    params.all_peds_lr.append(Ped.Ped("child", "left2right", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.elder_amount_lr):
    params.all_peds_lr.append(Ped.Ped("elder", "left2right", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.ped_amount_rl):
    params.all_peds_lr.append(Ped.Ped("ped", "right2left", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.wheelchair_amount_rl):
    params.all_peds_lr.append(Ped.Ped("wheelchair", "right2left", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.crutches_user_amount_rl):
    params.all_peds_lr.append(Ped.Ped("crutches_user", "right2left", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.children_amount_rl):
    params.all_peds_lr.append(Ped.Ped("child", "right2left", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)
for i in range(0, params.elder_amount_rl):
    params.all_peds_lr.append(Ped.Ped("elder", "right2left", params))
    print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].velocity, params.all_peds_lr[i].radius)


params.all_peds = params.all_peds_lr + params.all_peds_lr

total_size_lr = params.ped_amount_lr + params.wheelchair_amount_lr + params.crutches_user_amount_lr + params.children_amount_lr + params.elder_amount_lr
total_size_rl = params.ped_amount_rl + params.wheelchair_amount_rl + params.crutches_user_amount_rl + params.children_amount_rl + params.elder_amount_rl
total_size =  total_size_lr + total_size_rl
print("total_size_lr: ", total_size_lr )
print("total_size_rl: ", total_size_rl )
print("total_size: ", total_size, " len(all_peds): ", len(params.all_peds))
if total_size != len(params.all_peds):
    raise Exception("total_size != len(all_peds)")


# all_peds_sorted_by_x = sorted(all_peds, key=operator.attrgetter('y'), reverse=True)
params.all_peds_lr_sorted_by_x = sorted(params.all_peds_lr, key=operator.attrgetter('x'), reverse=True)
print("params.all_peds_lr_sorted_by_x: ", params.all_peds_lr_sorted_by_x, "\n")
params.all_peds_rl_sorted_by_x = sorted(params.all_peds_rl, key=operator.attrgetter('x'))
print("params.all_peds_rl_sorted_by_x: ", params.all_peds_rl_sorted_by_x, "\n")


#
# Move
#

# for i in range(total_size):
#     newx = all_peds_sorted_by_y[i].x + all_peds_sorted_by_y[i].velocity 
#     newy = all_peds_sorted_by_y[i].y
#     conflict = all_peds_sorted_by_y[i].is_newposition_conflict(newx, newy , all_peds_sorted_by_y[i+1:])
#     print("conflict: ", len(conflict))
#     if (len(conflict) == 0):
#         all_peds_sorted_by_y[i].x = newx
#         all_peds_sorted_by_y[i].y = newy
#     else:
#         for in_front_ped in all_peds_sorted_by_y[i+1:]:
#             print("test: ", Circles.get_intersections(1,1,1,2,1,1), "\n")
#             intersection = Circles.get_intersections(all_peds_sorted_by_y[i].x, all_peds_sorted_by_y[i].y, all_peds_sorted_by_y[i].velocity * SIMU_STEP_TIME, in_front_ped.x, in_front_ped.y, in_front_ped.radius + all_peds_sorted_by_y[i].radius)
#             print(intersection)
#             newx = intersection[2]
#             newy = intersection[3]
#             conflict = all_peds_sorted_by_y[i].is_newposition_conflict(newx, newy , all_peds_sorted_by_y[:i])
#             print(conflict)
#             if (len(conflict) == 0):
#                 all_peds_sorted_by_y[i].x = newx
#                 all_peds_sorted_by_y[i].y = newy
