import matplotlib.pyplot as py  

class Utilities:

    @staticmethod
    def is_all_peds_finish(params):
        for ped_i in params.all_peds_ordered:
            if ped_i.status != "finished":
                return False            
        return True

    @staticmethod
    def plot_positions(params, status):
        ax = py.gca()
        for ped_i in params.all_peds_lr_sorted_by_x:
            ax.plot(ped_i.x, ped_i.y, 'ro')
            ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving if status == "moving" else ped_i.radius_standing, color='r', fill=False, clip_on=False) )
            
        for ped_i in params.all_peds_rl_sorted_by_x:
            ax.plot(ped_i.x, ped_i.y, 'cs')
            ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving if status == "moving" else ped_i.radius_standing, color='c', fill=False, clip_on=False) )
            
        split_line_left_x = [params.waiting_area_length, params.waiting_area_length]
        split_line_left_y = [0, params.crosswalk_width]
        split_line_right_x = [params.waiting_area_length + params.crosswalk_length, params.waiting_area_length + params.crosswalk_length]
        split_line_right_y = [0, params.crosswalk_width]
        top_line_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        top_line_y = [params.crosswalk_width, params.crosswalk_width]
        bottom_line_x = [params.waiting_area_length, params.waiting_area_length + params.crosswalk_length]
        bottom_line_y = [0, 0]
        py.plot(split_line_left_x, split_line_left_y, 'b-')
        py.plot(split_line_right_x, split_line_right_y, 'b-')
        py.plot(top_line_x, top_line_y, 'b-')
        py.plot(bottom_line_x, bottom_line_y, 'b-')

        py.xlim([-50, params.total_length + 50])

        py.text(params.waiting_area_length - 200, params.crosswalk_width / 3, "Waiting\narea\non one\nside")
        py.text(params.waiting_area_length + params.crosswalk_length + 10, params.crosswalk_width / 3, "Waiting\narea\non another\nside")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width / 2, "Crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width + 10, "Outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, -30, "Outside crosswalk area")

        py.show()

