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
    cross_frame = tk.LabelFrame(params.cross_window, padx=5, pady=5, height=600, width=1200)
    cross_frame.grid(row=2, column=1, padx=0, pady=5)
    cross_frame.configure(height=cross_frame["height"], width=cross_frame["width"])
    cross_frame.grid_propagate(0)

    cross_bg_canvas = tk.Canvas(cross_frame, height=500, width=1100, bg='#afeeee')
    ped_lr_img = tk.PhotoImage(file="gui/img/ped_lr.png")
    print("png: ", ped_lr_img)
    a = cross_bg_canvas.create_image(20,20, image=ped_lr_img, anchor=tk.NW)
    print("png a: ", a)
    # waiting_area_left_canvas_images_dict = dict()
    # if params.ped_amount_lr <= 5:
    #     for i in range(1, 6):
    #         waiting_area_left_canvas_images_dict[i] = cross_bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
    #                                                                          anchor=tk.NW)

    # params.cross_window.mainloop()
    # move ped