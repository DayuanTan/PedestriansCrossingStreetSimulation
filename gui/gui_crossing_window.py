import tkinter as tk

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
    quit_button.place(relx=0.5, rely=0.9, anchor="w")

    # draw the canvas for crosswalk
    # frame for crosswalk and pedestrians crossing
    params.cross_frame = tk.LabelFrame(params.cross_window, padx=0, pady=0, height=600, width=1200)
    params.cross_frame.grid(row=2, column=1, padx=0, pady=5)
    params.cross_frame.configure(height=params.cross_frame["height"], width=params.cross_frame["width"])
    params.cross_frame.grid_propagate(0)


    params.cross_bg_canvas = tk.Canvas(params.cross_frame, height=590, width=1190, bg='red')
    params.cross_bg_canvas.place(relx=0, rely=0)
    params.background = tk.PhotoImage(file="gui/img/background.png") # 595x1195 px
    params.cross_bg_canvas.create_image(0,0, image=params.background, anchor=tk.NW)

    params.ped_lr_img = tk.PhotoImage(file="gui/img/ped_lr.png")
    print("png: ", params.ped_lr_img)
    params.cross_bg_canvas.create_image(200,100, image=params.ped_lr_img, anchor=tk.NW)
    print("png a: ")
    
    print("params.ped_amount_lr: ", params.ped_amount_lr)
    if params.ped_amount_lr <= 20:
        for i in range(1, 6):
            print(i)
            params.waiting_area_left_canvas_images_dict[i] = params.cross_bg_canvas.create_image(177, 95 + 40 * (i - 1), image=params.ped_lr_img,
                                                                             anchor=tk.NW)

    # params.cross_window.mainloop()
    # move ped