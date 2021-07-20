import tkinter as tk
from tkinter import messagebox



# frame for parameters 
def param_input(root, params):
    #
    # basic params
    #

    frame = tk.LabelFrame(root, padx=5, pady=5, height=600, width=400)
    frame.grid(row=2, column=0, padx=10, pady=5)
    frame.configure(height=frame["height"], width=frame["width"])
    frame.grid_propagate(0)

    ask_for_param_label = tk.Label(frame, text="Please set up following basic parameters:")
    ask_for_param_label.place(relx=0.5, rely=0.1, anchor="center")

    crosswalk_width_label = tk.Label(frame, text="Width for crosswalk area: (cm)")
    crosswalk_width_label.place(relx=0.0, rely=0.2, anchor="w")
    params.crosswalk_width_entry = tk.Entry(frame, width=4)
    params.crosswalk_width_entry.insert(0, params.crosswalk_width)
    params.crosswalk_width_entry.place(relx=0.88, rely=0.2, anchor="w")

    crosswalk_length_label = tk.Label(frame, text="Length for crosswalk area: (cm)")
    crosswalk_length_label.place(relx=0.0, rely=0.27, anchor="w")
    params.crosswalk_length_entry = tk.Entry(frame, width=4)
    params.crosswalk_length_entry.insert(0, params.crosswalk_length)
    params.crosswalk_length_entry.place(relx=0.88, rely=0.27, anchor="w")

    ped_amount_lr_label = tk.Label(frame, text="Amount of pedestrians from left to right:")
    ped_amount_lr_label.place(relx=0.0, rely=0.34, anchor="w")
    params.ped_amount_lr_entry = tk.Entry(frame, width=3)
    params.ped_amount_lr_entry.insert(0, params.ped_amount_lr)
    params.ped_amount_lr_entry.place(relx=0.88, rely=0.34, anchor="w")

    ped_amount_rl_label = tk.Label(frame, text="Amount of pedestrians from right to left:")
    ped_amount_rl_label.place(relx=0.0, rely=0.41, anchor="w")
    params.ped_amount_rl_entry = tk.Entry(frame, width=3)
    params.ped_amount_rl_entry.insert(0, params.ped_amount_rl)
    params.ped_amount_rl_entry.place(relx=0.88, rely=0.41, anchor="w")

    wheelchair_amount_lr_label = tk.Label(frame, text="Amount of wheelchairs from left to right:")
    wheelchair_amount_lr_label.place(relx=0.0, rely=0.48, anchor="w")
    params.wheelchair_amount_lr_entry = tk.Entry(frame, width=3)
    params.wheelchair_amount_lr_entry.insert(0, params.wheelchair_amount_lr)
    params.wheelchair_amount_lr_entry.place(relx=0.88, rely=0.48, anchor="w")

    wheelchair_amount_rl_label = tk.Label(frame, text="Amount of wheelchairs from right to left:")
    wheelchair_amount_rl_label.place(relx=0.0, rely=0.55, anchor="w")
    params.wheelchair_amount_rl_entry = tk.Entry(frame, width=3)
    params.wheelchair_amount_rl_entry.insert(0, params.wheelchair_amount_rl)
    params.wheelchair_amount_rl_entry.place(relx=0.88, rely=0.55, anchor="w")

    crutches_user_amount_lr_label = tk.Label(frame, text="Amount of crutches user from left to right:")
    crutches_user_amount_lr_label.place(relx=0.0, rely=0.62, anchor="w")
    params.crutches_user_amount_lr_entry = tk.Entry(frame, width=3)
    params.crutches_user_amount_lr_entry.insert(0, params.crutches_user_amount_lr)
    params.crutches_user_amount_lr_entry.place(relx=0.88, rely=0.62, anchor="w")

    crutches_user_amount_rl_label = tk.Label(frame, text="Amount of crutches user from right to left:")
    crutches_user_amount_rl_label.place(relx=0.0, rely=0.69, anchor="w")
    params.crutches_user_amount_rl_entry = tk.Entry(frame, width=3)
    params.crutches_user_amount_rl_entry.insert(0, params.crutches_user_amount_rl)
    params.crutches_user_amount_rl_entry.place(relx=0.88, rely=0.69, anchor="w")

    children_amount_lr_label = tk.Label(frame, text="Amount of children from left to right:")
    children_amount_lr_label.place(relx=0.0, rely=0.76, anchor="w")
    params.children_amount_lr_entry = tk.Entry(frame, width=3)
    params.children_amount_lr_entry.insert(0, params.children_amount_lr)
    params.children_amount_lr_entry.place(relx=0.88, rely=0.76, anchor="w")

    children_amount_rl_label = tk.Label(frame, text="Amount of children from right to left:")
    children_amount_rl_label.place(relx=0.0, rely=0.83, anchor="w")
    params.children_amount_rl_entry = tk.Entry(frame, width=3)
    params.children_amount_rl_entry.insert(0, params.children_amount_rl)
    params.children_amount_rl_entry.place(relx=0.88, rely=0.83, anchor="w")

    elder_amount_lr_label = tk.Label(frame, text="Amount of elder from left to right:")
    elder_amount_lr_label.place(relx=0.0, rely=0.9, anchor="w")
    params.elder_amount_lr_entry = tk.Entry(frame, width=3)
    params.elder_amount_lr_entry.insert(0, params.elder_amount_lr)
    params.elder_amount_lr_entry.place(relx=0.88, rely=0.9, anchor="w")

    elder_amount_rl_label = tk.Label(frame, text="Amount of elder from right to left:")
    elder_amount_rl_label.place(relx=0.0, rely=0.97, anchor="w")
    params.elder_amount_rl_entry = tk.Entry(frame, width=3)
    params.elder_amount_rl_entry.insert(0, params.elder_amount_rl)
    params.elder_amount_rl_entry.place(relx=0.88, rely=0.97, anchor="w")


    #
    # advanced params
    #

    right_frame = tk.LabelFrame(root, padx=1, pady=5, height=600, width=1000)
    right_frame.grid(row=2, column=1, padx=10, pady=5)
    right_frame.configure(height=right_frame["height"], width=right_frame["width"])
    right_frame.grid_propagate(0)

    ask_for_adv_param_label = tk.Label(right_frame, text="Please set up following advaced parameters if you want:\n(Please be carefula bout advanced parameters, the reasons for the choice of the default values are explained in our paper.)")
    ask_for_adv_param_label.place(relx=0.5, rely=0.1, anchor="center")

    step_time_label = tk.Label(right_frame, text="Each simulation step reflects how long in read world: (s)")
    step_time_label.place(relx=0.0, rely=0.2, anchor="w")
    params.step_time_entry = tk.Entry(right_frame, width=4)
    params.step_time_entry.insert(0, params.step_time)
    params.step_time_entry.place(relx=0.4, rely=0.2, anchor="w")

    waiting_area_length_label = tk.Label(right_frame, text="Length for waiting area: (cm)")
    waiting_area_length_label.place(relx=0.0, rely=0.27, anchor="w")
    waiting_area_length_label2 = tk.Label(right_frame, text="(Waiting area width == Crosswalk width)")
    waiting_area_length_label2.place(relx=0.0, rely=0.30, anchor="w")
    params.waiting_area_length_entry = tk.Entry(right_frame, width=4)
    params.waiting_area_length_entry.insert(0, params.waiting_area_length)
    params.waiting_area_length_entry.place(relx=0.4, rely=0.27, anchor="w")

    ped_walking_velocity_min_label = tk.Label(right_frame, text="Pedestrians walking min velocity (cm/s):")
    ped_walking_velocity_min_label.place(relx=0.0, rely=0.34, anchor="w")
    params.ped_walking_velocity_min_entry = tk.Entry(right_frame, width=3)
    params.ped_walking_velocity_min_entry.insert(0, params.ped_walking_velocity_min)
    params.ped_walking_velocity_min_entry.place(relx=0.4, rely=0.34, anchor="w")

    ped_walking_velocity_max_label = tk.Label(right_frame, text="Pedestrians walking max velocity (cm/s):")
    ped_walking_velocity_max_label.place(relx=0.0, rely=0.41, anchor="w")
    params.ped_walking_velocity_max_entry = tk.Entry(right_frame, width=3)
    params.ped_walking_velocity_max_entry.insert(0, params.ped_walking_velocity_max)
    params.ped_walking_velocity_max_entry.place(relx=0.4, rely=0.41, anchor="w")

    ped_walking_velocity_mean_label = tk.Label(right_frame, text="Pedestrians walking mean velocity (cm/s):")
    ped_walking_velocity_mean_label.place(relx=0.0, rely=0.48, anchor="w")
    params.ped_walking_velocity_mean_entry = tk.Entry(right_frame, width=3)
    params.ped_walking_velocity_mean_entry.insert(0, params.ped_walking_velocity_mean)
    params.ped_walking_velocity_mean_entry.place(relx=0.4, rely=0.48, anchor="w")



    wheelchair_rolling_velocity_min_label = tk.Label(right_frame, text="Wheelchair rolling min velocity (cm/s):")
    wheelchair_rolling_velocity_min_label.place(relx=0.0, rely=0.55, anchor="w")
    params.wheelchair_rolling_velocity_min_entry = tk.Entry(right_frame, width=3)
    params.wheelchair_rolling_velocity_min_entry.insert(0, params.wheelchair_rolling_velocity_min)
    params.wheelchair_rolling_velocity_min_entry.place(relx=0.4, rely=0.55, anchor="w")

    wheelchair_rolling_velocity_max_label = tk.Label(right_frame, text="Wheelchair rolling max velocity (cm/s):")
    wheelchair_rolling_velocity_max_label.place(relx=0.0, rely=0.62, anchor="w")
    params.wheelchair_rolling_velocity_max_entry = tk.Entry(right_frame, width=3)
    params.wheelchair_rolling_velocity_max_entry.insert(0, params.wheelchair_rolling_velocity_max)
    params.wheelchair_rolling_velocity_max_entry.place(relx=0.4, rely=0.62, anchor="w")

    wheelchair_rolling_velocity_mean_label = tk.Label(right_frame, text="Wheelchair rolling mean velocity (cm/s):")
    wheelchair_rolling_velocity_mean_label.place(relx=0.0, rely=0.69, anchor="w")
    params.wheelchair_rolling_velocity_mean_entry = tk.Entry(right_frame, width=3)
    params.wheelchair_rolling_velocity_mean_entry.insert(0, params.wheelchair_rolling_velocity_mean)
    params.wheelchair_rolling_velocity_mean_entry.place(relx=0.4, rely=0.69, anchor="w")



    crutches_user_walking_velocity_min_label = tk.Label(right_frame, text="Crutchesuser walking min velocity (cm/s):")
    crutches_user_walking_velocity_min_label.place(relx=0.0, rely=0.76, anchor="w")
    params.crutches_user_walking_velocity_min_entry = tk.Entry(right_frame, width=3)
    params.crutches_user_walking_velocity_min_entry.insert(0, params.crutches_user_walking_velocity_min)
    params.crutches_user_walking_velocity_min_entry.place(relx=0.4, rely=0.76, anchor="w")

    crutches_user_walking_velocity_max_label = tk.Label(right_frame, text="Crutchesuser walking max velocity (cm/s):")
    crutches_user_walking_velocity_max_label.place(relx=0.0, rely=0.83, anchor="w")
    params.crutches_user_walking_velocity_max_entry = tk.Entry(right_frame, width=3)
    params.crutches_user_walking_velocity_max_entry.insert(0, params.crutches_user_walking_velocity_max)
    params.crutches_user_walking_velocity_max_entry.place(relx=0.4, rely=0.83, anchor="w")

    crutches_user_walking_velocity_mean_label = tk.Label(right_frame, text="Crutchesuser walking mean velocity (cm/s):")
    crutches_user_walking_velocity_mean_label.place(relx=0.0, rely=0.9, anchor="w")
    params.crutches_user_walking_velocity_mean_entry = tk.Entry(right_frame, width=3)
    params.crutches_user_walking_velocity_mean_entry.insert(0, params.crutches_user_walking_velocity_mean)
    params.crutches_user_walking_velocity_mean_entry.place(relx=0.4, rely=0.9, anchor="w")



    children_walking_velocity_min_label = tk.Label(right_frame, text="Children walking min velocity (cm/s):")
    children_walking_velocity_min_label.place(relx=0.5, rely=0.2, anchor="w")
    params.children_walking_velocity_min_entry = tk.Entry(right_frame, width=3)
    params.children_walking_velocity_min_entry.insert(0, params.children_walking_velocity_min)
    params.children_walking_velocity_min_entry.place(relx=0.9, rely=0.2, anchor="w")

    children_walking_velocity_max_label = tk.Label(right_frame, text="Children walking max velocity (cm/s):")
    children_walking_velocity_max_label.place(relx=0.5, rely=0.27, anchor="w")
    params.children_walking_velocity_max_entry = tk.Entry(right_frame, width=3)
    params.children_walking_velocity_max_entry.insert(0, params.children_walking_velocity_max)
    params.children_walking_velocity_max_entry.place(relx=0.9, rely=0.27, anchor="w")

    children_walking_velocity_mean_label = tk.Label(right_frame, text="Children walking mean velocity (cm/s):")
    children_walking_velocity_mean_label.place(relx=0.5, rely=0.34, anchor="w")
    params.children_walking_velocity_mean_entry = tk.Entry(right_frame, width=3)
    params.children_walking_velocity_mean_entry.insert(0, params.children_walking_velocity_mean)
    params.children_walking_velocity_mean_entry.place(relx=0.9, rely=0.34, anchor="w")

    

    elder_walking_velocity_min_label = tk.Label(right_frame, text="Elder walking mean velocity (cm/s):")
    elder_walking_velocity_min_label.place(relx=0.5, rely=0.41, anchor="w")
    params.elder_walking_velocity_min_entry = tk.Entry(right_frame, width=3)
    params.elder_walking_velocity_min_entry.insert(0, params.elder_walking_velocity_min)
    params.elder_walking_velocity_min_entry.place(relx=0.9, rely=0.41, anchor="w")

    elder_walking_velocity_max_label = tk.Label(right_frame, text="Elder walking mean velocity (cm/s):")
    elder_walking_velocity_max_label.place(relx=0.5, rely=0.48, anchor="w")
    params.elder_walking_velocity_max_entry = tk.Entry(right_frame, width=3)
    params.elder_walking_velocity_max_entry.insert(0, params.elder_walking_velocity_max)
    params.elder_walking_velocity_max_entry.place(relx=0.9, rely=0.48, anchor="w")

    elder_walking_velocity_mean_label = tk.Label(right_frame, text="Elder walking mean velocity (cm/s):")
    elder_walking_velocity_mean_label.place(relx=0.5, rely=0.55, anchor="w")
    params.elder_walking_velocity_mean_entry = tk.Entry(right_frame, width=3)
    params.elder_walking_velocity_mean_entry.insert(0, params.elder_walking_velocity_mean)
    params.elder_walking_velocity_mean_entry.place(relx=0.9, rely=0.55, anchor="w")



def param_save_button_func(root, params):
    param_save_button_logic(root, params)
    



def param_save_button_logic(root, params):
    # basic
    params.crosswalk_width = int(params.crosswalk_width_entry.get())
    params.crosswalk_length = int(params.crosswalk_length_entry.get())
    params.ped_amount_lr = int(params.ped_amount_lr_entry.get())
    params.ped_amount_rl = int(params.ped_amount_rl_entry.get())
    params.wheelchair_amount_lr = int(params.wheelchair_amount_lr_entry.get())
    params.wheelchair_amount_rl = int(params.wheelchair_amount_rl_entry.get())
    params.crutches_user_amount_lr = int(params.crutches_user_amount_lr_entry.get())
    params.crutches_user_amount_rl = int(params.crutches_user_amount_rl_entry.get())
    params.children_amount_lr = int(params.children_amount_lr_entry.get())
    params.children_amount_rl = int(params.children_amount_rl_entry.get())
    params.elder_amount_lr = int(params.elder_amount_lr_entry.get())
    params.elder_amount_rl = int(params.elder_amount_rl_entry.get())
    # adv
    params.step_time = int(params.step_time_entry.get())
    params.waiting_area_length = int(params.waiting_area_length_entry.get())
    params.ped_walking_velocity_min_entry = int(params.ped_walking_velocity_min_entry.get())
    params.ped_walking_velocity_max_entry = int(params.ped_walking_velocity_max_entry.get())
    params.ped_walking_velocity_mean_entry = int(params.ped_walking_velocity_mean_entry.get())
    params.wheelchair_rolling_velocity_min = int(params.wheelchair_rolling_velocity_min_entry.get())
    params.wheelchair_rolling_velocity_max = int(params.wheelchair_rolling_velocity_max_entry.get())
    params.wheelchair_rolling_velocity_mean = int(params.wheelchair_rolling_velocity_mean_entry.get())
    params.crutches_user_walking_velocity_min = int(params.crutches_user_walking_velocity_min_entry.get())
    params.crutches_user_walking_velocity_max = int(params.crutches_user_walking_velocity_max_entry.get())
    params.crutches_user_walking_velocity_mean = int(params.crutches_user_walking_velocity_mean_entry.get())
    params.children_walking_velocity_min = int(params.children_walking_velocity_min_entry.get())
    params.children_walking_velocity_max = int(params.children_walking_velocity_max_entry.get())
    params.children_walking_velocity_mean = int(params.children_walking_velocity_mean_entry.get())
    params.elder_walking_velocity_min = int(params.elder_walking_velocity_min_entry.get())
    params.elder_walking_velocity_max = int(params.elder_walking_velocity_max_entry.get())
    params.elder_walking_velocity_mean = int(params.elder_walking_velocity_mean_entry.get())



    if params.crosswalk_width <= 0 or params.crosswalk_length <= 0 or params.ped_amount_lr <= 0 or params.ped_amount_rl <= 0 \
            or params.wheelchair_amount_lr < 0 or params.wheelchair_amount_rl < 0 or params.crutches_user_amount_lr < 0 or params.crutches_user_amount_rl < 0 \
            or params.children_amount_lr < 0 or params.children_amount_rl < 0 or params.elder_amount_lr < 0 or params.elder_amount_rl < 0 \
            or params.step_time <= 0 or params.waiting_area_length <=0 \
            or params.ped_walking_velocity_min <= 0 or params.ped_walking_velocity_max <= 0 or params.ped_walking_velocity_mean <= 0 \
            or params.wheelchair_rolling_velocity_min <= 0 or params.wheelchair_rolling_velocity_max <= 0 or params.wheelchair_rolling_velocity_mean <= 0 \
            or params.crutches_user_walking_velocity_min <= 0 or params.crutches_user_walking_velocity_max <= 0 or params.crutches_user_walking_velocity_mean <= 0 \
            or params.children_walking_velocity_min <= 0 or params.children_walking_velocity_max <= 0 or params.children_walking_velocity_mean <= 0 \
            or params.elder_walking_velocity_min <= 0 or params.elder_walking_velocity_max <= 0 or params.elder_walking_velocity_mean <= 0:
        messagebox.showinfo(title="Alert", message="Invalid arguments!")
        param_save_button_func(root, params)

    
    messagebox.showinfo(title="Parameters applied", message="Parameters applied! \nBasic parameters:" 
        + "\nCrosswalk Width: " + str(params.crosswalk_width) 
        + "\nCrosswalk Length: " + str(params.crosswalk_length) 
        + "\nped_amount_lr: " + str(params.ped_amount_lr) + "\nped_amount_rl: " + str(params.ped_amount_rl)
        + "\nwheelchair_amount_lr: " + str(params.wheelchair_amount_lr) + "\nwheelchair_amount_rl: " + str(params.wheelchair_amount_rl)
        + "\ncrutches_user_amount_lr: " + str(params.crutches_user_amount_lr) + "\ncrutches_user_amount_rl: " + str(params.crutches_user_amount_rl)
        + "\nchildren_amount_lr: " + str(params.children_amount_lr) + "\nchildren_amount_rl: " + str(params.children_amount_rl)
        + "\nelder_amount_lr: " + str(params.elder_amount_lr) + "\nelder_amount_lr: " + str(params.elder_amount_lr)
        + "\n\n\nAdvanced parameters:"
        + "\nstep_time: " + str(params.step_time)
        + "\nwaiting_area_length: " + str(params.waiting_area_length)
        + "\nped_walking_velocity: min: " + str(params.ped_walking_velocity_min) + " max: " + str(params.ped_walking_velocity_max) + " mean: " + str(params.ped_walking_velocity_mean)
        + "\nwheelchair_rolling_velocity: min: " + str(params.wheelchair_rolling_velocity_min) + " max: " + str(params.wheelchair_rolling_velocity_max) + " mean: " + str(params.wheelchair_rolling_velocity_mean)
        + "\ncrutches_user_walking_velocity: min: " + str(params.crutches_user_walking_velocity_min) + " max: " + str(params.crutches_user_walking_velocity_max) + " mean: " + str(params.crutches_user_walking_velocity_mean)
        + "\nchildren_walking_velocity: min: " + str(params.children_walking_velocity_min) + " max: " + str(params.children_walking_velocity_max) + " mean: " + str(params.children_walking_velocity_mean)
        + "\nelder_walking_velocity: min: " + str(params.elder_walking_velocity_min) + " max: " + str(params.elder_walking_velocity_max) + " mean: " + str(params.elder_walking_velocity_mean)
        )


    


