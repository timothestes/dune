from src.game.board.locations.location import Location
from game.pieces.agents.agent import Agent
from typing import List
import json


class Board:
    def __init__(self, type: str = "default"):
        self.locations = {}
        self.add_locations(self.get_locations(type))

    def get_locations(self, type):
        if type == "default":
            return self.get_default_locations()
        elif type == "rise_of_ix":
            return self.get_rise_of_ix_locations()
        else:
            raise ValueError(f"{type} is not a valid board type (yet).")

    def get_default_locations(self) -> List[Location]:
        with open("resources/dune_imperium.json", "r") as f:
            config = json.load(f)
            return [Location(**location) for location in config["locations"]]

    def get_default_locations_as_dict(self) -> dict:
        return {location.name: location for location in self.get_default_locations()}

    def get_rise_of_ix_locations(self):
        locations = self.get_default_locations_as_dict()
        with open("resources/rise_of_ix.json", "r") as f:
            config = json.load(f)
            for location in config["locations"]:
                if location.get("replaces"):
                    locations.pop(location["replaces"], None)
                locations[location["name"]] = Location(**location)

            return list(locations.values())

    def add_location(self, location: Location):
        self.locations[location.name] = location

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
