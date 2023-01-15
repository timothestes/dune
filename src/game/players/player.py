import uuid


class Player:
    def __init__(self, color: str, player_id: int = None):
        self.player_id = player_id or uuid.uuid4()
        self.hand = []
        self.points = 0
        self.color = color
