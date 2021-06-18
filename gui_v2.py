import tkinter as tk
import gui.gui_global_params as gui_global_params 
import gui.gui_left_section_param_input as l
import gui.gui_crossing_window as cross

root = tk.Tk()
root.title('Pedestrians Crossing Street Simulation')
root.geometry("1600x800")

# top greeting section
greeting = tk.Label(root, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
greeting.grid(row=0, columnspan=3, padx=600, pady=5)
greeting = tk.Label(root, text="Parameters Setting")
greeting.grid(row=1, columnspan=3, padx=600, pady=5)

# declare global parameters
params = gui_global_params.gui_global_params()

# left param input section
l.left_section_param_input(root, params)

# buttons
save_button = tk.Button(params.frame, text="Save parameters", command = lambda: l.param_save_button_func(root, params) )
save_button.place(relx=0.25, rely=0.9, anchor="w")

quit_button = tk.Button(params.frame, text="Quit", command=root.quit)
quit_button.place(relx=0.75, rely=0.9, anchor="w")

# second window for ped crossing street
cross_botton = tk.Button(params.frame, text="Begin ped crossing", command = lambda: cross.begin_crossing_func(root, params))
cross_botton.place(relx=0.5, rely=0.9, anchor="w")


root.mainloop()