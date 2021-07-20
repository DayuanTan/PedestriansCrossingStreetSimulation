import tkinter as tk
from tkinter import messagebox
import backend.Ped as Ped
from BackendAPI import BackendAPI
from backend.Utilities import Utilities as Utilities

def begin_crossing_func(root, params):
    
    # add backend plot system
    params.log_keywords.append("plot")

    # initial
    BackendAPI.set_peds_initial_positions(params)

    # call BackendAPI, it uses backend plot system
    BackendAPI.cross_street(params)
    params.total_needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
    print("These pedestrains need ", params.total_needed_time, " seconds to cross the street.\n")
    
    messagebox.showinfo(title="Result", message="These pedestrains need " + str(params.total_needed_time) +  " seconds to cross the street.\n" )
