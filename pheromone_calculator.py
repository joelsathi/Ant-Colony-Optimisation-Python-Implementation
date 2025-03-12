from distance_calculator import calc_distance

def update_pheromone_matrix(pheromone_matrix, distance_matrix, ant_paths, evaporation_rate):
    """
    Updates the pheromone matrix based on ant paths and evaporation rate.
    
    Args:
        pheromone_matrix (list of list of float): The pheromone levels between nodes.
        distance_matrix (list of list of float): The distance between nodes.
        ant_paths (list of list of int): The paths taken by ants.
        evaporation_rate (float): The rate at which pheromones evaporate.
    
    Returns:
        list of list of float: The updated pheromone matrix.
    """
    num_nodes = len(pheromone_matrix)

    # Apply evaporation to the pheromone matrix
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            pheromone_matrix[i][j] *= (1 - evaporation_rate)
    
    # Reinforce pheromones based on ant paths
    for path in ant_paths:
        total_distance = calc_distance(distance_matrix, path)

        for i in range(len(path) - 1):
            start_node = path[i] - 1
            end_node = path[i + 1] - 1
            pheromone_matrix[start_node][end_node] += 1 / total_distance
            pheromone_matrix[end_node][start_node] += 1 / total_distance
        
        # Return to the starting node
        last_node = path[-1] - 1
        first_node = path[0] - 1
        pheromone_matrix[last_node][first_node] += 1 / total_distance
        pheromone_matrix[first_node][last_node] += 1 / total_distance
    
    return pheromone_matrix
