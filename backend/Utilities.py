import matplotlib.pyplot as py  
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.pyplot import figure


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
        # draw ped
        for ped_i in params.all_peds_lr_sorted_by_x:
            ax.plot(ped_i.x, ped_i.y, 'ro', clip_on=False)
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='r', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving, color='r', fill=False, clip_on=False) )

        for ped_i in params.all_peds_rl_sorted_by_x:
            ax.plot(ped_i.x, ped_i.y, 'cs', clip_on=False)
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='c', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving, color='c', fill=False, clip_on=False) )
            
        # draw crosswalk area
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
        py.ylim([-500, params.crosswalk_width + 500])

        py.text(params.waiting_area_length - 200, params.crosswalk_width / 3, "Waiting\narea\non one\nside")
        py.text(params.waiting_area_length + params.crosswalk_length + 10, params.crosswalk_width / 3, "Waiting\narea\non another\nside")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width / 2, "Crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width + 100, "Outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, -100, "Outside crosswalk area")

        py.show()

    @staticmethod
    def get_image(ped_direction, ped_type):
        if ped_direction == "left2right" and ped_type == "ped":
            return OffsetImage(py.imread(fname="backend/img/ped_lr.png"))

    @staticmethod
    def plot_ped_image(ped_i, ax, zoom=1):
        # if ped_direction == "left2right" and ped_type == "ped":
        image = py.imread("backend/img/ped_lr.png")
        if ped_i.direction == "left2right" and ped_i.type == "ped":
            image = py.imread("backend/img/ped_lr.png")
        elif ped_i.direction == "right2left" and ped_i.type == "ped":
            image = py.imread("backend/img/ped_rl.png")
    
        im = OffsetImage(image, zoom=zoom)
        ab = AnnotationBbox(im, (ped_i.x, ped_i.y), xycoords='data', frameon=False, clip_on=False)
        ax.add_artist(ab)
        ax.autoscale()

    @staticmethod
    def plot_positions2(params, status):
        figure(figsize=(12.6, 11), dpi=80)
        ax = py.gca()

        # draw ped
        for ped_i in params.all_peds_lr_sorted_by_x:
            # draw dot
            # ax.plot(ped_i.x, ped_i.y, 'ro', clip_on=False)
            Utilities.plot_ped_image(ped_i, ax, zoom=0.4)
            # add circle
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='b', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving, color='b', fill=False, clip_on=False) )

        for ped_i in params.all_peds_rl_sorted_by_x:
            # draw dot
            # ax.plot(ped_i.x, ped_i.y, 'cs', clip_on=False)
            Utilities.plot_ped_image(ped_i, ax, zoom=0.4)
            # add circle
            if status == "standing":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_standing, color='g', fill=False, clip_on=False) )
            if status == "moving" and ped_i.status == "moving":
                ax.add_patch( py.Circle((ped_i.x, ped_i.y), ped_i.radius_moving, color='g', fill=False, clip_on=False) )
            
        # draw crosswalk area
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

        py.xlim([-100, params.total_length + 00])
        py.ylim([-600, params.crosswalk_width + 600])

        py.text(params.waiting_area_length - 200, params.crosswalk_width / 3, "Waiting\narea\non one\nside")
        py.text(params.waiting_area_length + params.crosswalk_length + 10, params.crosswalk_width / 3, "Waiting\narea\non another\nside")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width / 2, "Crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, params.crosswalk_width + 100, "Outside crosswalk area")
        py.text(params.waiting_area_length + params.crosswalk_length/3, -100, "Outside crosswalk area")

        py.show()
