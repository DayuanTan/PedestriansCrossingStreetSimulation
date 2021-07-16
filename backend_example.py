from BackendAPI import BackendAPI
import global_params.global_params as global_params

# Step 1: Modify parameters in global_params.py and enable it
params = global_params.global_params()

# Step 2:
BackendAPI.set_peds_initial_positions(params)
BackendAPI.cross_street(params)
needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
print("These pedestrains need ", needed_time, " seconds to cross the street.\n")
