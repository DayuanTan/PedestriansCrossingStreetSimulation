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
    greeting = tk.Label(params.cross_window, text="PPedestrians Crossing")
    greeting.grid(row=1, columnspan=3, padx=600, pady=5)

    quit_button = tk.Button(params.cross_window, text="Quit", command=root.quit)
    quit_button.place(relx=0.75, rely=0.9, anchor="w")