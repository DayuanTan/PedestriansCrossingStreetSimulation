class gui_global_params:
    def __init__(self):
        super().__init__()

        self.zebra_area_width_entry = 0
        self.zebra_area_length_entry = 0
        self.ped_amount_lr_entry = 0
        self.ped_amount_rl_entry = 0
        self.wheelchair_amount_lr_entry = 0
        self.wheelchair_amount_rl_entry = 0
        self.children_amount_lr_entry = 0
        self.children_amount_rl_entry = 0
        
        self.zebra_area_width = 0
        self.zebra_area_length = 0
        self.ped_amount_lr = 0
        self.ped_amount_rl = 0
        self.wheelchair_amount_lr = 0
        self.wheelchair_amount_rl = 0
        self.children_amount_lr = 0
        self.children_amount_rl = 0

        self.frame = 0


        self.cross_window = 0
        # self.cross_window_frame = 0
        self.waiting_area_left_canvas_images_dict = dict()