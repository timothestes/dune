from src.game.board.locations.location import Location
from game.pieces.agents.agent import Agent
from typing import List


class Board:
    def __init__(self):
        self.locations = {}

    def add_location(self, location: Location):
        self.locations[location.name] = None

    def add_locations(self, locations: List[Location]):
        for location in locations:
            self.add_location(location)

    def remove_location(self, location_name):
        if location_name not in self.locations:
            raise ValueError(f"{location_name} not found on the board.")
        del self.locations[location_name]

    def get_agent_at(self, location_name):
        if location_name not in self.locations:
            raise ValueError(f"{location_name} not found on the board.")
        return self.locations[location_name]

    def move_agent(self, agent: Agent, location: Location):
        if location.name not in self.locations:
            raise ValueError(f"{location.name} not found on the board.")
        if self.locations[location.name] is not None:
            raise ValueError(
                f"Location {location.name} is already occupied by another agent."
            )

        print(f"Moving {agent.color} {agent.name} to {location.name}.")
        # move agent to location
        self.locations[location.name] = agent
        agent.current_position = location
        # collect resources
        location.location_effects()
        # set agent to activated
        agent.activate()

    def recall_agents(self):
        for location in self.locations:
            if self.locations[location] is not None:
                agent: Agent = self.locations[location]
                agent.recall()
                self.locations[location] = None
