import tkinter as tk
import random
import gui_global_params 
import gui_left_section_param_input as l

root = tk.Tk()
root.title('Pedestrians Crossing Street Simulation')
root.geometry("1600x800")

# top greeting section
greeting = tk.Label(root, text="Pedestrians Crossing Street Simulation by Dayuan Tan @UMBC")
greeting.grid(row=1, columnspan=3, padx=280, pady=5)

# left param input section
params = gui_global_params.gui_global_params()
l.left_section_param_input(root, params)

# l.param_save_button_func(params)

save_button = tk.Button(params.frame, text="Save parameters", command = lambda: l.param_save_button_func(params) )
save_button.place(relx=0.0, rely=0.83, anchor="w")


 

print("zebra_area_width: ", params.zebra_area_width) 
print("zebra_area_length: ", params.zebra_area_length) 
print("ped_amount_lr: ", params.ped_amount_lr) 
print("ped_amount_rl: ", params.ped_amount_rl) 
print("wheelchair_amount_lr: ", params.wheelchair_amount_lr) 
print("wheelchair_amount_rl: ", params.wheelchair_amount_rl) 
print("children_amount_lr: ", params.children_amount_lr) 
print("children_amount_rl: ", params.children_amount_rl) 


root.mainloop()