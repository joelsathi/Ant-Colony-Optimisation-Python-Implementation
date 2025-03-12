def calc_distance(graph, path):
    """
    Calculates the total distance of a given path in the graph.
    
    The distance is computed by summing up the weights of the edges between consecutive nodes,
    including the return to the starting node.
    
    Args:
        graph (list of list of float): The adjacency matrix representing the graph.
        path (list of int): The sequence of nodes representing the path.
    
    Returns:
        float: The total distance of the path.
    """

    # Compute distance for the given path
    distance = 0
    for i in range(len(path)-1):
        u = path[i] - 1
        v = path[i+1] - 1
        distance += graph[u][v]

    # Return back to the starting
    lst_node = path[-1] - 1
    fst_node = path[0] - 1
    distance += graph[lst_node][fst_node]
    
    return distance