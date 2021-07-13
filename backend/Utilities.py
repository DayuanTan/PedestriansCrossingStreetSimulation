import matplotlib.pyplot as py  

class Utilities:

    @staticmethod
    def is_all_peds_finish(params):
        for ped_i in params.all_peds_ordered:
            if ped_i.finished == False:
                return False            
        return True

    @staticmethod
    def plot_positions(params):
        for ped_i in params.all_peds_ordered:
            py.plot(ped_i.x, ped_i.y, 'ro')
            
        split_line_left_x = [params.waiting_area_length, params.waiting_area_length]
        split_line_left_y = [0, params.crosswalk_width]
        split_line_right_x = [params.waiting_area_length + params.crosswalk_length, params.waiting_area_length + params.crosswalk_length]
        split_line_right_y = [0, params.crosswalk_width]
        py.plot(split_line_left_x, split_line_left_y, 'b-')
        py.plot(split_line_right_x, split_line_right_y, 'b-')
        py.show()

