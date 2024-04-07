
def flatten_2d_list(array) -> list:
    """Method to change a 2d array to a 1d array"""
    if isinstance(array[0], list): # Checking if it's a 2D array
        # For a 2D array transform to a 1D array
        return [element for sublist in array for element in sublist]
    else:
        # For a 1D array
        return array
