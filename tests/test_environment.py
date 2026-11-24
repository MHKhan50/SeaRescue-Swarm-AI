from searescue.environment import RescueGrid


def test_zero_energy_agent_cannot_move():
    env = RescueGrid()
    agent = env.agents[0]

    agent.energy = 0
    original_position = (agent.x, agent.y)

    env.move(agent, (10, 10))

    assert (agent.x, agent.y) == original_position
    assert agent.active is False


def test_agent_energy_decreases_after_movement():
    env = RescueGrid()
    agent = env.agents[0]

    original_energy = agent.energy
    env.move(agent, (10, 0))

    assert agent.energy == original_energy - 1


def test_agent_becomes_inactive_at_zero_energy():
    env = RescueGrid()
    agent = env.agents[0]

    agent.energy = 1
    env.move(agent, (10, 0))

    assert agent.energy == 0
    assert agent.active is False
