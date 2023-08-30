def calculate_geometric_progression(initial_value, num_iterations, ratio):
    progress_vals = [initial_value * ratio ** _i for _i in range(num_iterations)]
    return progress_vals

