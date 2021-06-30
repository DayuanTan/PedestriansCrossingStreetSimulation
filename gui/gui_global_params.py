class gui_global_params:
    def __init__(self):
        super().__init__()

        self.crosswalk_width_entry = 0
        self.crosswalk_length_entry = 0
        self.ped_amount_lr_entry = 0
        self.ped_amount_rl_entry = 0
        self.wheelchair_amount_lr_entry = 0
        self.wheelchair_amount_rl_entry = 0
        self.children_amount_lr_entry = 0
        self.children_amount_rl_entry = 0
        
        self.crosswalk_width = 0
        self.crosswalk_length = 0
        self.ped_amount_lr = 0
        self.ped_amount_rl = 0
        self.wheelchair_amount_lr = 0
        self.wheelchair_amount_rl = 0
        self.children_amount_lr = 0
        self.children_amount_rl = 0

        self.frame = 0


        self.cross_window = 0
        self.cross_frame = 0
        self.cross_bg_canvas = 0
        self.background = 0
        self.waiting_area_left_canvas_images_dict = dict()
        self.ped_lr_img = 0
        