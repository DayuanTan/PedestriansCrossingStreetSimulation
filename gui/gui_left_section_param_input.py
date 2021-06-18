import tkinter as tk
import random


# left frame for parameters
def left_section_param_input(root, params):
    frame = tk.LabelFrame(root, padx=5, pady=5, height=600, width=400)
    frame.grid(row=2, column=0, padx=10, pady=5)
    frame.configure(height=frame["height"], width=frame["width"])
    frame.grid_propagate(0)

    ask_for_param_label = tk.Label(frame, text="Please set up parameters:")
    ask_for_param_label.place(relx=0.5, rely=0.1, anchor="center")

    zebra_area_width_label = tk.Label(frame, text="Width for zebra area:")
    zebra_area_width_label.place(relx=0.0, rely=0.2, anchor="w")
    params.zebra_area_width_entry = tk.Entry(frame, width=3)
    params.zebra_area_width_entry.insert(0, "3")
    params.zebra_area_width_entry.place(relx=0.88, rely=0.2, anchor="w")

    zebra_area_length_label = tk.Label(frame, text="Length for zebra area:")
    zebra_area_length_label.place(relx=0.0, rely=0.27, anchor="w")
    params.zebra_area_length_entry = tk.Entry(frame, width=3)
    params.zebra_area_length_entry.insert(0, "10")
    params.zebra_area_length_entry.place(relx=0.88, rely=0.27, anchor="w")

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


def param_save_button_func(params):
    param_save_button_logic(params)


# def begin_crossing_func():
#     begin_crossing_logic(0)


# save_button = tk.Button(frame, text="Setup pedestrians", command=param_save_button_func)
# save_button.place(relx=0.0, rely=0.83, anchor="w")

# cross_botton = tk.Button(frame, text="Begin crossing", command=begin_crossing_func)
# cross_botton.place(relx=0.0, rely=0.90, anchor="w")

# quit_button = tk.Button(frame, text="Quit", command=root.quit)
# quit_button.place(relx=0.4, rely=0.90, anchor="w")


def param_save_button_logic(params):
    params.zebra_area_width = int(params.zebra_area_width_entry.get())
    params.zebra_area_length = int(params.zebra_area_length_entry.get())
    params.ped_amount_lr = int(params.ped_amount_lr_entry.get())
    params.ped_amount_rl = int(params.ped_amount_rl_entry.get())
    params.wheelchair_amount_lr = int(params.wheelchair_amount_lr_entry.get())
    params.wheelchair_amount_rl = int(params.wheelchair_amount_rl_entry.get())
    params.children_amount_lr = int(params.children_amount_lr_entry.get())
    params.children_amount_rl = int(params.children_amount_rl_entry.get())

    if params.zebra_area_width <= 0 or params.zebra_area_length <= 0 or params.ped_amount_lr <= 0 or params.ped_amount_rl <= 0 \
            or params.wheelchair_amount_lr < 0 or params.wheelchair_amount_rl < 0 or params.children_amount_lr < 0 or params.children_amount_rl < 0:
        tk.messagebox.showinfo(title="Alert", message="Invalid arguments!")
        param_save_button_func(params)

    param_saved_label = tk.Label(params.frame, text="Parameters applied. Width: " + str(params.zebra_area_width) + " Length: " + str(
        params.zebra_area_length) + " p: " + str(params.ped_amount_lr))
    param_saved_label.place(relx=0, rely=0.76, anchor="w")

    # waiting_area_left_setup(ped_amount_lr, wheelchair_amount_lr, children_amount_lr)




def waiting_area_left_setup(ped_amount_lr, wheelchair_amount_lr, children_amount_lr):
    if ped_amount_lr <= 5:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
    elif ped_amount_lr <= 10:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, ped_amount_lr - 4):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
    elif ped_amount_lr <= 15:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 9):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
    elif ped_amount_lr <= 20:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 14):
            waiting_area_left_canvas_images_dict[i + 15] = bg_canvas.create_image(117, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
    elif ped_amount_lr <= 25:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 15] = bg_canvas.create_image(117, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 19):
            waiting_area_left_canvas_images_dict[i + 20] = bg_canvas.create_image(97, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
    elif ped_amount_lr <= 30:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 15] = bg_canvas.create_image(117, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 20] = bg_canvas.create_image(97, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 24):
            waiting_area_left_canvas_images_dict[i + 25] = bg_canvas.create_image(77, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
    elif ped_amount_lr <= 35:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 15] = bg_canvas.create_image(117, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 20] = bg_canvas.create_image(97, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 25] = bg_canvas.create_image(77, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 29):
            waiting_area_left_canvas_images_dict[i + 30] = bg_canvas.create_image(57, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
    else:
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i] = bg_canvas.create_image(177, 95 + 40 * (i - 1), image=ped_lr_img,
                                                                             anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 5] = bg_canvas.create_image(157, 95 + 40 * (i - 1),
                                                                                 image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 10] = bg_canvas.create_image(137, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 15] = bg_canvas.create_image(117, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 20] = bg_canvas.create_image(97, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 25] = bg_canvas.create_image(77, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, 6):
            waiting_area_left_canvas_images_dict[i + 30] = bg_canvas.create_image(57, 95 + 40 * (i - 1),
                                                                                  image=ped_lr_img, anchor=tk.NW)
        for i in range(1, ped_amount_lr - 34):
            waiting_area_left_canvas_images_dict[i + 35] = bg_canvas.create_image(random.randrange(57, 177),
                                                                                  random.randrange(95, 255),
                                                                                  image=ped_lr_img, anchor=tk.NW)