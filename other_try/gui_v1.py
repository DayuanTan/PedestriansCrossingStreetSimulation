import tkinter as tk
import random

root = tk.Tk()
root.title('Pedestrians Crossing Street Simulation')
root.geometry("1600x800")
greeting = tk.Label(root, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
greeting.grid(row=1, columnspan=3, padx=280, pady=5)

# left frame for parameters

frame = tk.LabelFrame(root, padx=5, pady=5, height=600, width=400)
frame.grid(row=2, column=0, padx=10, pady=5)
frame.configure(height=frame["height"], width=frame["width"])
frame.grid_propagate(0)

ask_for_param_label = tk.Label(frame, text="Please set up parameters:")
ask_for_param_label.place(relx=0.5, rely=0.1, anchor="center")

zebra_area_width_label = tk.Label(frame, text="Width for zebra area:")
zebra_area_width_label.place(relx=0.0, rely=0.2, anchor="w")
zebra_area_width_entry = tk.Entry(frame, width=3)
zebra_area_width_entry.insert(0, "3")
zebra_area_width_entry.place(relx=0.88, rely=0.2, anchor="w")

zebra_area_length_label = tk.Label(frame, text="Length for zebra area:")
zebra_area_length_label.place(relx=0.0, rely=0.27, anchor="w")
zebra_area_length_entry = tk.Entry(frame, width=3)
zebra_area_length_entry.insert(0, "10")
zebra_area_length_entry.place(relx=0.88, rely=0.27, anchor="w")

ped_amount_lr_label = tk.Label(frame, text="Amount of pedestrians from left to right:")
ped_amount_lr_label.place(relx=0.0, rely=0.34, anchor="w")
ped_amount_lr_entry = tk.Entry(frame, width=3)
ped_amount_lr_entry.insert(0, 20)
ped_amount_lr_entry.place(relx=0.88, rely=0.34, anchor="w")

ped_amount_rl_label = tk.Label(frame, text="Amount of pedestrians from right to left:")
ped_amount_rl_label.place(relx=0.0, rely=0.41, anchor="w")
ped_amount_rl_entry = tk.Entry(frame, width=3)
ped_amount_rl_entry.insert(0, 20)
ped_amount_rl_entry.place(relx=0.88, rely=0.41, anchor="w")

wheelchair_amount_lr_label = tk.Label(frame, text="Amount of wheelchairs from left to right:")
wheelchair_amount_lr_label.place(relx=0.0, rely=0.48, anchor="w")
wheelchair_amount_lr_entry = tk.Entry(frame, width=3)
wheelchair_amount_lr_entry.insert(0, 1)
wheelchair_amount_lr_entry.place(relx=0.88, rely=0.48, anchor="w")

wheelchair_amount_rl_label = tk.Label(frame, text="Amount of wheelchairs from right to left:")
wheelchair_amount_rl_label.place(relx=0.0, rely=0.55, anchor="w")
wheelchair_amount_rl_entry = tk.Entry(frame, width=3)
wheelchair_amount_rl_entry.insert(0, 1)
wheelchair_amount_rl_entry.place(relx=0.88, rely=0.55, anchor="w")

children_amount_lr_label = tk.Label(frame, text="Amount of children from left to right:")
children_amount_lr_label.place(relx=0.0, rely=0.62, anchor="w")
children_amount_lr_entry = tk.Entry(frame, width=3)
children_amount_lr_entry.insert(0, 1)
children_amount_lr_entry.place(relx=0.88, rely=0.62, anchor="w")

children_amount_rl_label = tk.Label(frame, text="Amount of children from right to left:")
children_amount_rl_label.place(relx=0.0, rely=0.69, anchor="w")
children_amount_rl_entry = tk.Entry(frame, width=3)
children_amount_rl_entry.insert(0, 1)
children_amount_rl_entry.place(relx=0.88, rely=0.69, anchor="w")

zebra_area_width = 0
zebra_area_length = 0
ped_amount_lr = 0
ped_amount_rl = 0
wheelchair_amount_lr = 0
wheelchair_amount_rl = 0
children_amount_lr = 0
children_amount_rl = 0


def param_save_button_func():
    param_save_button_logic()


def begin_crossing_func():
    begin_crossing_logic(0)


save_button = tk.Button(frame, text="Setup pedestrians", command=param_save_button_func)
save_button.place(relx=0.0, rely=0.83, anchor="w")

cross_botton = tk.Button(frame, text="Begin crossing", command=begin_crossing_func)
cross_botton.place(relx=0.0, rely=0.90, anchor="w")

quit_button = tk.Button(frame, text="Quit", command=root.quit)
quit_button.place(relx=0.4, rely=0.90, anchor="w")


def param_save_button_logic():
    zebra_area_width = int(zebra_area_width_entry.get())
    zebra_area_length = int(zebra_area_length_entry.get())
    ped_amount_lr = int(ped_amount_lr_entry.get())
    ped_amount_rl = int(ped_amount_rl_entry.get())
    wheelchair_amount_lr = int(wheelchair_amount_lr_entry.get())
    wheelchair_amount_rl = int(wheelchair_amount_rl_entry.get())
    children_amount_lr = int(children_amount_lr_entry.get())
    children_amount_rl = int(children_amount_rl_entry.get())

    if zebra_area_width <= 0 or zebra_area_length <= 0 or ped_amount_lr <= 0 or ped_amount_rl <= 0 \
            or wheelchair_amount_lr < 0 or wheelchair_amount_rl < 0 or children_amount_lr < 0 or children_amount_rl < 0:
        tk.messagebox.showinfo(title="Alert", message="Invalid arguments!")
        param_save_button_func()

    param_saved_label = tk.Label(frame, text="Parameters applied. Width: " + str(zebra_area_width) + " Length: " + str(
        zebra_area_length) + " p: " + str(ped_amount_lr))
    param_saved_label.place(relx=0, rely=0.76, anchor="w")

    waiting_area_left_setup(ped_amount_lr, wheelchair_amount_lr, children_amount_lr)


# right frame for zebra and pedestrians crossing

cartoon_frame = tk.LabelFrame(root, padx=5, pady=5, height=600, width=1170)
cartoon_frame.grid(row=2, column=1, padx=0, pady=5)
cartoon_frame.configure(height=cartoon_frame["height"], width=cartoon_frame["width"])
cartoon_frame.grid_propagate(0)

bg_canvas = tk.Canvas(cartoon_frame, height=400, width=1040, bg='#afeeee')


# curb
def setup_curb():
    bg_canvas.create_rectangle(200, 20, 210, 300, fill="gray", outline="gray")
    bg_canvas.create_rectangle(800, 20, 810, 300, fill="gray", outline="gray")
    bg_canvas.create_arc(105, 250, 205, 350, fill="red", start=270, style=tk.ARC, outline="gray", width=10)
    bg_canvas.create_arc(805, 250, 905, 350, fill="red", start=180, style=tk.ARC, outline="gray", width=10)
    # middle two lines
    bg_canvas.create_polygon(490, 0, 490, 80, 499, 80, 499, 0, fill="orange", outline="orange")
    bg_canvas.create_polygon(501, 0, 501, 80, 510, 80, 510, 0, fill="orange", outline="orange")
    # arrows
    bg_canvas.create_polygon(340, 10, 340, 60, 320, 60, 350, 85, 380, 60, 360, 60, 360, 10, fill="yellow",
                             outline="yellow")
    bg_canvas.create_polygon(650, 10, 620, 30, 640, 30, 640, 80, 660, 80, 660, 30, 680, 30, fill="yellow",
                             outline="yellow")
    bg_canvas.place(relx=0.05, rely=0.1)


# zebra
def setup_zebra():
    bg_canvas.create_rectangle(214, 95, 796, 297, fill="yellow", outline="yellow")
    bg_canvas.create_rectangle(224, 97, 254, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(284, 97, 314, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(344, 97, 374, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(404, 97, 434, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(464, 97, 494, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(524, 97, 554, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(584, 97, 614, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(644, 97, 674, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(704, 97, 734, 295, fill="lightgray", outline="lightgray")
    bg_canvas.create_rectangle(764, 97, 790, 295, fill="lightgray", outline="lightgray")


setup_curb()
setup_zebra()

ped_lr_img = tk.PhotoImage(file="other_try/ped_lr.png")
# wheelchair_lr_img = tk.PhotoImage(file="img/wheelchair_lr.png")

waiting_area_left_canvas_images_dict = dict()


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
    # waiting_area_left_canvas.create_image(118, 0, image = ped_lr_img, anchor = tk.NW)
    # waiting_area_left_canvas.create_image(118, 40, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(118, 80, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(118, 120, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(118, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(98, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(78, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(58, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(38, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(18, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(-2, 160, image=ped_lr_img, anchor=tk.NW)
    # waiting_area_left_canvas.create_image(8, 40, image=wheelchair_lr_img, anchor=tk.NW)


# 2D array records whether a spot is accupied
# zebra width is 796-214 = 582
# zebra height is 297-95 = 202
num_rows = 5
num_cols = 30
cells = [[False] * num_cols for _ in range(num_rows)]

# def find_available_cell():

def move(ped):
    bg_canvas.move(ped, +20, +0)
    # bg_canvas.place(relx=0.05, rely=0.1)


def begin_crossing_logic(counter):
    if counter < 50:
        for k, v in waiting_area_left_canvas_images_dict.items():
            move(v)
            root.after(100)
            counter += 1
        begin_crossing_logic(counter)
    # bg_canvas.move(waiting_area_left_canvas_images_dict.get(1), +20, +0)


#
# counter = 0
# begin_crossing_logic(counter)

root.mainloop()
