class global_params:
    def __init__(self):
        super().__init__()

        #
        # params needed in both gui and backend
        #

        # simulation area with default value
        self.crosswalk_width = 300 #cm
        self.crosswalk_length = 1000 #cm

        # simulation amount with default value
        self.ped_amount_lr = 20
        self.ped_amount_rl = 20
        self.wheelchair_amount_lr = 1
        self.wheelchair_amount_rl = 0
        self.crutches_user_amount_lr = 0
        self.crutches_user_amount_rl = 1
        self.children_amount_lr = 0
        self.children_amount_rl = 0
        self.elder_amount_lr = 0
        self.elder_amount_rl = 0

        # simulation speed with default value
        self.ped_walking_velocity_min = 110 #cm/s
        self.ped_walking_velocity_max = 140 #cm/s
        self.ped_walking_velocity_mean = 125 #cm/s
        self.ped_walking_velocity_sigma = 0.1 # standard deviation
 
        self.wheelchair_rolling_velocity_min = 70 #cm/s
        self.wheelchair_rolling_velocity_max = 100 #cm/s
        self.wheelchair_rolling_velocity_mean = 85 #cm/s
        self.wheelchair_rolling_velocity_sigma = 0.1

        self.crutches_user_walking_velocity_min = 50 #cm/s
        self.crutches_user_walking_velocity_max = 80 #cm/s
        self.crutches_user_walking_velocity_mean = 75 #cm/s
        self.crutches_user_walking_velocity_sigma = 0.1

        self.children_walking_velocity_min = 50 #cm/s
        self.children_walking_velocity_max = 80 #cm/s
        self.children_walking_velocity_mean = 75 #cm/s
        self.children_walking_velocity_sigma = 0.1

        self.elder_walking_velocity_min = 50 #cm/s
        self.elder_walking_velocity_max = 80 #cm/s
        self.elder_walking_velocity_mean = 75 #cm/s
        self.elder_walking_velocity_sigma = 0.1

        # simulation occupied space with default value
        self.radius_of_space_occupied = {
            "ped": 50, #cm
            "wheelchair": 70, 
            "crutches_user": 90,
            "children": 40,
            "elder": 50
        }


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
        
