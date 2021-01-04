import tkinter as tk

root = tk.Tk()
root.title('Pedestrians Crossing Street Simulation')
root.geometry("1000x500")
greeting = tk.Label(root, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
greeting.grid(row = 1, columnspan = 3, padx = 280, pady = 5)

# left frame for parameters

frame = tk.LabelFrame(root, padx = 5, pady = 5, height=400, width=300)
frame.grid(row = 2, column = 0, padx = 10, pady = 5)
frame.configure(height=frame["height"],width=frame["width"])
frame.grid_propagate(0)

ask_for_param_label = tk.Label(frame, text="Please set up parameters:")
ask_for_param_label.place(relx = 0.5, rely = 0.1, anchor = "center")

zebra_area_width_label = tk.Label(frame, text="Width for zebra area:")
zebra_area_width_label.place(relx=0.0, rely=0.2, anchor = "w")

zebra_area_width_entry = tk.Entry(frame, width = 3)
zebra_area_width_entry.place(relx=0.5, rely=0.2, anchor = "w")

zebra_area_length_label = tk.Label(frame, text="Length for zebra area:")
zebra_area_length_label.place(relx=0.0, rely=0.3, anchor = "w")

zebra_area_length_entry = tk.Entry(frame, width = 3)
zebra_area_length_entry.place(relx=0.5, rely=0.3, anchor = "w")


def param_save_button_func():
    global zebra_area_width
    global zebra_area_length
    zebra_area_width = zebra_area_width_entry.get()
    zebra_area_length = zebra_area_length_entry.get()
    param_saved_label = tk.Label(frame, text="Parameters applied. Width: " + zebra_area_width + " Length: " + zebra_area_length)
    param_saved_label.place(relx=0, rely=0.6, anchor = "w")
    show_again()

def show_again():
    param_saved_label2 = tk.Label(frame, text="Parameters applied.2 Width: " + str(zebra_area_width) + " Length: " + str(zebra_area_length))
    param_saved_label2.place(relx=0, rely=0.7, anchor="w")


save_button = tk.Button(frame, text = "Apply all parameters", command = param_save_button_func)
save_button.place(relx=0.0, rely=0.4, anchor = "w")


quit_button = tk.Button(frame, text = "Quit", command = root.quit)
quit_button.place(relx=0.0, rely=0.5, anchor = "w")


# right frame for zebra and pedestrians crossing

zebra_frame = tk.LabelFrame(root, padx = 5, pady = 5, height=400, width=670)
zebra_frame.grid(row = 2, column = 1, padx = 0, pady = 5)
zebra_frame.configure(height=zebra_frame["height"],width=zebra_frame["width"])
zebra_frame.grid_propagate(0)

root.mainloop()