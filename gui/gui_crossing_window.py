import tkinter as tk
import backend.Ped as Ped
from BackendAPI import BackendAPI
from backend.Utilities import Utilities as Utilities

def begin_crossing_func(root, params):
      
    # Toplevel object which will be treated as a new window
    params.cross_window = tk.Toplevel(root)

    # sets the title of the Toplevel widget
    params.cross_window.title("Pedestrians Crossing Street Simulation - Ped Crossing")
  
    # A Label widget to show in toplevel
    # top greeting section
    greeting = tk.Label(params.cross_window, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
    greeting.grid(row=0, columnspan=3, padx=600, pady=5)
    greeting = tk.Label(params.cross_window, text="Pedestrians Crossing")
    greeting.grid(row=1, columnspan=3, padx=600, pady=5)

    # buttons
    quit_button = tk.Button(params.cross_window, text="Quit", command=root.quit)
    quit_button.place(relx=0.33, rely=0.9, anchor="w")
    next_step_button = tk.Button(params.cross_window, text="Next step", command = lambda: onestep(params) )
    next_step_button.place(relx=0.66, rely=0.9, anchor="w")

    # draw the canvas for crosswalk
    params.cross_frame = tk.LabelFrame(params.cross_window, padx=0, pady=0, height=params.cross_frame_height, width=params.cross_frame_width)
    params.cross_frame.grid(row=2, column=1, padx=0, pady=5)
    params.cross_frame.configure(height=params.cross_frame["height"], width=params.cross_frame["width"])
    params.cross_frame.grid_propagate(0)


    params.cross_bg_canvas = tk.Canvas(params.cross_frame, height=params.cross_frame_height-10, width=params.cross_frame_width-10, bg='red')
    params.cross_bg_canvas.place(relx=0, rely=0)
    params.background = tk.PhotoImage(file="gui/img/background.png") # 595x1195 px
    params.cross_bg_canvas.create_image(0,0, image=params.background, anchor=tk.NW)

    params.ped_lr_img = tk.PhotoImage(file="gui/img/ped_lr.png")
    print("png 1: ", params.ped_lr_img)
    # params.cross_bg_canvas.create_image(245,135, image=params.ped_lr_img, anchor=tk.NW)
    # params.cross_bg_canvas.create_image(245,400, image=params.ped_lr_img, anchor=tk.NW)
    # params.cross_bg_canvas.create_image(890,135, image=params.ped_lr_img, anchor=tk.NW)
    # params.cross_bg_canvas.create_image(890,400, image=params.ped_lr_img, anchor=tk.NW)
    print("png 1 a: ")
    # params.ped_rl_img = tk.PhotoImage(file="gui/img/ped_rl.png")
    # print("png 2: ", params.ped_rl_img)
    # params.cross_bg_canvas.create_image(800,100, image=params.ped_rl_img, anchor=tk.NW)
    # print("png 2 a: ")
    
    # initial
    BackendAPI.set_peds_initial_positions(params)
    Utilities.plot_positions(params, "moving")
    print("params.ped_amount_lr: ", params.ped_amount_lr)
    # scale ped coordinates to frame length and width: ped.x / params.total_length  = unknown / frame width; ped.y / params.crosswalk_width  = unknown / frame height
    # draw initial position
    counter = 0
    for ped_i in params.all_peds_lr_sorted_by_x:
        params.waiting_area_left_canvas_images_dict[counter] = params.cross_bg_canvas.create_image(ped_i.x * params.cross_frame_width / params.total_length, 
                                                                                                    params.cross_frame_height - ped_i.y * params.cross_frame_height / params.crosswalk_width, 
                                                                                                    image=params.ped_lr_img, anchor=tk.NW)
        counter += 1
    params.step_counter = 0
    
def onestep(params):
    
    if not Utilities.is_all_peds_finish(params):
        for ped_i in params.all_peds_lr_sorted_by_x:
            ped_i.move_one_step(params)
        params.step_counter += 1

    counter = 0
    for ped_i in params.all_peds_lr_sorted_by_x:
        params.cross_bg_canvas.move( params.waiting_area_left_canvas_images_dict[counter], 
                                    30, 
                                    0)
        # params.cross_bg_canvas.move( params.waiting_area_left_canvas_images_dict[counter], 
        #                             (ped_i.x - ped_i.previousx) * params.cross_frame_width / params.total_length, 
        #                             params.cross_frame_height - (ped_i.y - ped_i.previousy) * params.cross_frame_height / params.crosswalk_width )
        counter += 1

    # for ped_i in params.all_peds_rl:
    #     params.waiting_area_left_canvas_images_dict[counter] = params.cross_bg_canvas.create_image(ped_i.x, ped_i.y, image=params.ped_rl_img,
    #                                                                          anchor=tk.NW)
    #     counter += 1
    # if params.ped_amount_lr <= 20:
    #     for i in range(1, 6):
    #         print(i)
    #         params.waiting_area_left_canvas_images_dict[i] = params.cross_bg_canvas.create_image(177, 95 + 40 * (i - 1), image=params.ped_lr_img,
    #                                                                          anchor=tk.NW)

    # params.cross_window.mainloop()
    # move ped