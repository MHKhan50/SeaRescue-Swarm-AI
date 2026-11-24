import numpy as np


class Agent:
    def __init__(self, kind, x, y):
        self.kind = kind
        self.x = x
        self.y = y
        self.energy = 250
        self.active = True


class RescueGrid:
    def __init__(self, width=30, height=20, victim_count=5, seed=7):
        self.width = width
        self.height = height
        self.rng = np.random.default_rng(seed)
        self.victims = set()

        while len(self.victims) < victim_count:
            self.victims.add((
                int(self.rng.integers(width)),
                int(self.rng.integers(height))
            ))

        self.found = set()
        self.agents = [
            Agent("drone", 0, 0),
            Agent("drone", width - 1, 0),
            Agent("boat", width // 2, height - 1)
        ]

    def move(self, agent, target):
        if not agent.active or agent.energy <= 0:
            agent.active = False
            return

        tx, ty = target
        old_position = (agent.x, agent.y)

        if agent.x < tx:
            agent.x += 1
        elif agent.x > tx:
            agent.x -= 1
        elif agent.y < ty:
            agent.y += 1
        elif agent.y > ty:
            agent.y -= 1

        if (agent.x, agent.y) != old_position:
            agent.energy -= 1

        if agent.energy <= 0:
            agent.energy = 0
            agent.active = False

        if (agent.x, agent.y) in self.victims:
            self.found.add((agent.x, agent.y))
