def get_input(file_name):
    """
    Reads input data from a file and extracts relevant parameters.
    
    The function reads the number of towns, distance matrix, number of ants,
    evaporation rate, and initial guesses from the input file.
    
    Args:
        file_name (str): The name of the input file.
    
    Returns:
        tuple: A tuple containing:
            - num_towns (int): The number of towns.
            - distance_matrix (list of list of int): The symmetric distance matrix.
            - ant_count (int): The number of ants.
            - initial_guess (list of list of int): The initial paths guessed by the ants.
    """
    # read from file
    input_txt = open(file_name, 'r')
    input_lines = input_txt.readlines()

    # Get the number of towns
    n = int(input_lines[0])

    distance_matrix = []

    # Get the distance matrix
    i = 0
    for line_idx in range(n):
        line = input_lines[line_idx+1]
        distances = [int(s) for s in line.split()]
        distance_matrix.append(distances)

    ant_count = int(input_lines[n+1])
    
    initial_guess = []
    for j in range(ant_count):
        cur_line = input_lines[n+2+j]
        initial_guess.append([int(s) for s in cur_line.split()])

    return n, distance_matrix, ant_count, initial_guess