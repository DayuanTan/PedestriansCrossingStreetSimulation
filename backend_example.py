from BackendAPI import BackendAPI
import global_params.global_params as global_params

# Step 1: Modify parameters in global_params.py

# Step 2:
params = global_params.global_params()
BackendAPI.set_peds_initial_positions(params)
BackendAPI.cross_street(params)
needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
print("These pedestrains need ", needed_time, " seconds to cross the street.\n")
