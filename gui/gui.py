import tkinter as tk

root = tk.Tk()
root.title('Pedestrians Crossing Street Simulation')
root.geometry("1600x800")
greeting = tk.Label(root, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
greeting.grid(row = 1, columnspan = 3, padx = 280, pady = 5)

# left frame for parameters

frame = tk.LabelFrame(root, padx = 5, pady = 5, height=600, width=400)
frame.grid(row = 2, column = 0, padx = 10, pady = 5)
frame.configure(height=frame["height"],width=frame["width"])
frame.grid_propagate(0)

ask_for_param_label = tk.Label(frame, text="Please set up parameters:")
ask_for_param_label.place(relx = 0.5, rely = 0.1, anchor = "center")

zebra_area_width_label = tk.Label(frame, text="Width for zebra area:")
zebra_area_width_label.place(relx=0.0, rely=0.2, anchor = "w")
zebra_area_width_entry = tk.Entry(frame, width = 3)
zebra_area_width_entry.place(relx=0.88, rely=0.2, anchor = "w")

zebra_area_length_label = tk.Label(frame, text="Length for zebra area:")
zebra_area_length_label.place(relx=0.0, rely=0.27, anchor = "w")
zebra_area_length_entry = tk.Entry(frame, width = 3)
zebra_area_length_entry.place(relx=0.88, rely=0.27, anchor = "w")

ped_amount_lr_label = tk.Label(frame, text="Amount of pedestrians from left to right:")
ped_amount_lr_label.place(relx=0.0, rely=0.34, anchor = "w")
ped_amount_lr_entry = tk.Entry(frame, width = 3)
ped_amount_lr_entry.place(relx=0.88, rely=0.34, anchor = "w")

ped_amount_rl_label = tk.Label(frame, text="Amount of pedestrians from right to left:")
ped_amount_rl_label.place(relx=0.0, rely=0.41, anchor = "w")
ped_amount_rl_entry = tk.Entry(frame, width = 3)
ped_amount_rl_entry.place(relx=0.88, rely=0.41, anchor = "w")

wheelchair_amount_lr_label = tk.Label(frame, text="Amount of wheelchairs from left to right:")
wheelchair_amount_lr_label.place(relx=0.0, rely=0.48, anchor = "w")
wheelchair_amount_lr_entry = tk.Entry(frame, width = 3)
wheelchair_amount_lr_entry.place(relx=0.88, rely=0.48, anchor = "w")

wheelchair_amount_rl_label = tk.Label(frame, text="Amount of wheelchairs from right to left:")
wheelchair_amount_rl_label.place(relx=0.0, rely=0.55, anchor = "w")
wheelchair_amount_rl_entry = tk.Entry(frame, width = 3)
wheelchair_amount_rl_entry.place(relx=0.88, rely=0.55, anchor = "w")

children_amount_lr_label = tk.Label(frame, text="Amount of children from left to right:")
children_amount_lr_label.place(relx=0.0, rely=0.62, anchor = "w")
children_amount_lr_entry = tk.Entry(frame, width = 3)
children_amount_lr_entry.place(relx=0.88, rely=0.62, anchor = "w")

children_amount_rl_label = tk.Label(frame, text="Amount of children from right to left:")
children_amount_rl_label.place(relx=0.0, rely=0.69, anchor = "w")
children_amount_rl_entry = tk.Entry(frame, width = 3)
children_amount_rl_entry.place(relx=0.88, rely=0.69, anchor = "w")



def param_save_button_func():
    global zebra_area_width
    global zebra_area_length
    global ped_amount_lr
    global ped_amount_rl
    global wheelchair_amount_lr
    global wheelchair_amount_rl
    global children_amount_lr
    global children_amount_rl
    zebra_area_width = zebra_area_width_entry.get()
    zebra_area_length = zebra_area_length_entry.get()
    ped_amount_lr = ped_amount_lr_entry.get()
    ped_amount_rl = ped_amount_rl_entry.get()
    wheelchair_amount_lr = wheelchair_amount_lr_entry.get()
    wheelchair_amount_rl = wheelchair_amount_rl_entry.get()
    children_amount_lr = children_amount_lr_entry.get()
    children_amount_rl = children_amount_rl_entry.get()
    param_saved_label = tk.Label(frame, text="Parameters applied. Width: " + zebra_area_width + " Length: " + zebra_area_length)
    param_saved_label.place(relx=0, rely=0.76, anchor = "w")




save_button = tk.Button(frame, text = "Apply all parameters", command = param_save_button_func)
save_button.place(relx=0.0, rely=0.83, anchor = "w")


quit_button = tk.Button(frame, text = "Quit", command = root.quit)
quit_button.place(relx=0.0, rely=0.9, anchor = "w")


# right frame for zebra and pedestrians crossing

cartoon_frame = tk.LabelFrame(root, padx = 5, pady = 5, height=600, width=1170)
cartoon_frame.grid(row = 2, column = 1, padx = 0, pady = 5)
cartoon_frame.configure(height=cartoon_frame["height"],width=cartoon_frame["width"])
cartoon_frame.grid_propagate(0)

# curb
curb_canvas = tk.Canvas(cartoon_frame, height = 400, width = 1040, bg = '#afeeee')
curb_canvas.create_rectangle(200, 20, 210, 300, fill = "gray", outline = "gray")
curb_canvas.create_rectangle(800, 20, 810, 300, fill = "gray", outline = "gray")
curb_canvas.create_arc(105, 250, 205, 350, fill = "red", start = 270, style=tk.ARC, outline = "gray", width = 10)
curb_canvas.create_arc(805, 250, 905, 350, fill = "red", start = 180, style=tk.ARC, outline = "gray", width = 10)
curb_canvas.place(relx = 0.05, rely = 0.1)

# zebra
zebra_canvas = tk.Canvas(cartoon_frame, height = 200, width = 577, bg = 'yellow')
zebra_canvas.create_rectangle(25, 0, 55, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(85, 0, 115, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(145, 0, 175, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(205, 0, 235, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(265, 0, 295, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(325, 0, 355, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(385, 0, 415, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(445, 0, 475, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(505, 0, 535, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.create_rectangle(565, 0, 595, 200, fill = "lightgray", outline = "lightgray")
zebra_canvas.place(relx = 0.235, rely = 0.26)


root.mainloop()