def sweep_path(agent_index, agent_count, width, height):
    """
    Generate a fixed serpentine search path
    inside an agent's assigned vertical zone.
    """
    if agent_count <= 0:
        raise ValueError("agent_count must be positive")

    if not 0 <= agent_index < agent_count:
        raise ValueError("invalid agent_index")

    x_start = agent_index * width // agent_count
    x_end = (agent_index + 1) * width // agent_count
    zone_width = x_end - x_start

    if zone_width <= 0:
        raise ValueError("grid is too narrow for the number of agents")

    path = []

    for row in range(height):
        columns = range(zone_width)

        if row % 2 == 1:
            columns = reversed(range(zone_width))

        for column in columns:
            path.append((x_start + column, row))

    return path
