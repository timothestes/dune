from src.game.board.locations.arrakis import Arrakis
from game.pieces.agents.agent import Agent
from src.game.board.board import Board

if __name__ == "__main__":

    # Create a new agent
    blue_agent = Agent("blue")

    # create a new location
    arrakis = Arrakis()

    # create a new board
    board = Board()

    # add the location to the board
    board.add_location(arrakis)

    # move the agent to the location
    board.move_agent(blue_agent, arrakis)

    # end the turn, recalling all agents
    board.recall_agents()
