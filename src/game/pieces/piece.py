class Piece:
    def __init__(self):
        self.name = "Piece"

    def move(self, location):
        print(f"Moving to {location}.")
        
    def get_name(self):
        return self.name
