import tkinter as tk
from tkinter import messagebox
import random


# left frame for parameters
def left_section_param_input(root, params):
    frame = tk.LabelFrame(root, padx=5, pady=5, height=600, width=400)
    frame.grid(row=2, column=0, padx=10, pady=5)
    frame.configure(height=frame["height"], width=frame["width"])
    frame.grid_propagate(0)

    ask_for_param_label = tk.Label(frame, text="Please set up parameters:")
    ask_for_param_label.place(relx=0.5, rely=0.1, anchor="center")

    crosswalk_width_label = tk.Label(frame, text="Width for zebra area:")
    crosswalk_width_label.place(relx=0.0, rely=0.2, anchor="w")
    params.crosswalk_width_entry = tk.Entry(frame, width=3)
    params.crosswalk_width_entry.insert(0, "3")
    params.crosswalk_width_entry.place(relx=0.88, rely=0.2, anchor="w")

    crosswalk_length_label = tk.Label(frame, text="Length for zebra area:")
    crosswalk_length_label.place(relx=0.0, rely=0.27, anchor="w")
    params.crosswalk_length_entry = tk.Entry(frame, width=3)
    params.crosswalk_length_entry.insert(0, "10")
    params.crosswalk_length_entry.place(relx=0.88, rely=0.27, anchor="w")

    ped_amount_lr_label = tk.Label(frame, text="Amount of pedestrians from left to right:")
    ped_amount_lr_label.place(relx=0.0, rely=0.34, anchor="w")
    params.ped_amount_lr_entry = tk.Entry(frame, width=3)
    params.ped_amount_lr_entry.insert(0, 20)
    params.ped_amount_lr_entry.place(relx=0.88, rely=0.34, anchor="w")

    ped_amount_rl_label = tk.Label(frame, text="Amount of pedestrians from right to left:")
    ped_amount_rl_label.place(relx=0.0, rely=0.41, anchor="w")
    params.ped_amount_rl_entry = tk.Entry(frame, width=3)
    params.ped_amount_rl_entry.insert(0, 20)
    params.ped_amount_rl_entry.place(relx=0.88, rely=0.41, anchor="w")

    wheelchair_amount_lr_label = tk.Label(frame, text="Amount of wheelchairs from left to right:")
    wheelchair_amount_lr_label.place(relx=0.0, rely=0.48, anchor="w")
    params.wheelchair_amount_lr_entry = tk.Entry(frame, width=3)
    params.wheelchair_amount_lr_entry.insert(0, 1)
    params.wheelchair_amount_lr_entry.place(relx=0.88, rely=0.48, anchor="w")

    wheelchair_amount_rl_label = tk.Label(frame, text="Amount of wheelchairs from right to left:")
    wheelchair_amount_rl_label.place(relx=0.0, rely=0.55, anchor="w")
    params.wheelchair_amount_rl_entry = tk.Entry(frame, width=3)
    params.wheelchair_amount_rl_entry.insert(0, 1)
    params.wheelchair_amount_rl_entry.place(relx=0.88, rely=0.55, anchor="w")

    children_amount_lr_label = tk.Label(frame, text="Amount of children from left to right:")
    children_amount_lr_label.place(relx=0.0, rely=0.62, anchor="w")
    params.children_amount_lr_entry = tk.Entry(frame, width=3)
    params.children_amount_lr_entry.insert(0, 1)
    params.children_amount_lr_entry.place(relx=0.88, rely=0.62, anchor="w")

    children_amount_rl_label = tk.Label(frame, text="Amount of children from right to left:")
    children_amount_rl_label.place(relx=0.0, rely=0.69, anchor="w")
    params.children_amount_rl_entry = tk.Entry(frame, width=3)
    params.children_amount_rl_entry.insert(0, 1)
    params.children_amount_rl_entry.place(relx=0.88, rely=0.69, anchor="w")


def param_save_button_func(root, params):
    param_save_button_logic(root, params)
    



def param_save_button_logic(root, params):
    params.crosswalk_width = int(params.crosswalk_width_entry.get())
    params.crosswalk_length = int(params.crosswalk_length_entry.get())
    params.ped_amount_lr = int(params.ped_amount_lr_entry.get())
    params.ped_amount_rl = int(params.ped_amount_rl_entry.get())
    params.wheelchair_amount_lr = int(params.wheelchair_amount_lr_entry.get())
    params.wheelchair_amount_rl = int(params.wheelchair_amount_rl_entry.get())
    params.children_amount_lr = int(params.children_amount_lr_entry.get())
    params.children_amount_rl = int(params.children_amount_rl_entry.get())

    if params.crosswalk_width <= 0 or params.crosswalk_length <= 0 or params.ped_amount_lr <= 0 or params.ped_amount_rl <= 0 \
            or params.wheelchair_amount_lr < 0 or params.wheelchair_amount_rl < 0 or params.children_amount_lr < 0 or params.children_amount_rl < 0:
        messagebox.showinfo(title="Alert", message="Invalid arguments!")
        param_save_button_func(root, params)

    # param_saved_label = tk.Label(params.frame, text="Parameters applied. Width: " + str(params.crosswalk_width) + " Length: " + str(
    #     params.crosswalk_length) + " p: " + str(params.ped_amount_lr))
    # param_saved_label.place(relx=0.25, rely=0.83, anchor="w")
    messagebox.showinfo(title="Parameters applied", message="Parameters applied! \nCrosswalk Width: " + str(params.crosswalk_width) 
        + "\nCrosswalk Length: " + str(params.crosswalk_length) + "\nped_amount_lr: " + str(params.ped_amount_lr))


    


