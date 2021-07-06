class global_params:
    def __init__(self):
        super().__init__()

        #
        # params needed in both gui and backend
        #

        self.step_time = 0.1 # second # each simulation step reflects how long in read world

        # simulation area with default value
        self.crosswalk_width = 300 #cm
        self.crosswalk_length = 1000 #cm
        self.waiting_area_length = 300 #cm

        self.waiting_area_position_x_offset_min = 0 - self.waiting_area_length
        self.waiting_area_position_x_offset_max = self.waiting_area_length
        self.waiting_area_position_x_offset_mean = 0 #coordinate
        self.waiting_area_position_x_offset_sigma = self.waiting_area_length / 2 # max = mean + 2*sigma

        self.waiting_area_position_y_min = 0
        self.waiting_area_position_y_max = self.crosswalk_width
        self.waiting_area_position_y_mean = self.crosswalk_width / 2 #coordinate
        self.waiting_area_position_y_sigma = self.crosswalk_width / 4 # max = mean + 2*sigma => sigma = (max - mean )/2

        # simulation amount with default value
        self.ped_amount_lr = 10
        self.ped_amount_rl = 10
        self.wheelchair_amount_lr = 1
        self.wheelchair_amount_rl = 0
        self.crutches_user_amount_lr = 0
        self.crutches_user_amount_rl = 1
        self.children_amount_lr = 1
        self.children_amount_rl = 0
        self.elder_amount_lr = 0
        self.elder_amount_rl = 1

        # simulation speed with default value
        self.ped_walking_velocity_min = 110 #cm/s
        self.ped_walking_velocity_max = 140 #cm/s
        self.ped_walking_velocity_mean = 125 #cm/s
        self.ped_walking_velocity_sigma = (self.ped_walking_velocity_max - self.ped_walking_velocity_mean) / 3  # standard deviation # max = mean + 3*sigma => sigma = (max - mean )/3
 
        self.wheelchair_rolling_velocity_min = 70 #cm/s
        self.wheelchair_rolling_velocity_max = 100 #cm/s
        self.wheelchair_rolling_velocity_mean = 85 #cm/s
        self.wheelchair_rolling_velocity_sigma = (self.wheelchair_rolling_velocity_max - self.wheelchair_rolling_velocity_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.crutches_user_walking_velocity_min = 50 #cm/s
        self.crutches_user_walking_velocity_max = 80 #cm/s
        self.crutches_user_walking_velocity_mean = 75 #cm/s
        self.crutches_user_walking_velocity_sigma = (self.crutches_user_walking_velocity_max - self.crutches_user_walking_velocity_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.children_walking_velocity_min = 50 #cm/s
        self.children_walking_velocity_max = 80 #cm/s
        self.children_walking_velocity_mean = 75 #cm/s
        self.children_walking_velocity_sigma = (self.children_walking_velocity_max - self.children_walking_velocity_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.elder_walking_velocity_min = 50 #cm/s
        self.elder_walking_velocity_max = 80 #cm/s
        self.elder_walking_velocity_mean = 75 #cm/s
        self.elder_walking_velocity_sigma = (self.elder_walking_velocity_max - self.elder_walking_velocity_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        # simulation occupied space with default value
        self.radius_of_space_occupied_when_standing = {
            "ped": 30, #cm
            "wheelchair": 70, 
            "crutches_user": 40,
            "children": 30,
            "elder": 30
        }
        self.radius_of_space_occupied_when_moving = {
            "ped": 50, #cm
            "wheelchair": 70, 
            "crutches_user": 90,
            "children": 40,
            "elder": 50
        }

        self.all_peds_lr = list() # all ped who want go from left to right
        self.all_peds_rl = list() # all ped who want go from right to left
        self.all_peds = list()  # all ped 
        self.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed
        self.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x 


        #
        # params needed only in gui 
        #

        # gui display, left section params input 
        self.crosswalk_width_entry = 0
        self.crosswalk_length_entry = 0
        self.ped_amount_lr_entry = 0
        self.ped_amount_rl_entry = 0
        self.wheelchair_amount_lr_entry = 0
        self.wheelchair_amount_rl_entry = 0
        self.children_amount_lr_entry = 0
        self.children_amount_rl_entry = 0
        
        # self.frame = 0

        # gui display, second window, ped crossing 
        self.cross_window = 0
        self.cross_frame = 0
        self.cross_bg_canvas = 0
        self.background = 0
        self.waiting_area_left_canvas_images_dict = dict()
        self.ped_lr_img = 0
        
