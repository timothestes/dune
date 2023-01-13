class Location:
    def __init__(self, name, location_type, resources=None):
        self.name = name
        self.location_type = location_type
        self.resources = resources or {}

    def get_resources(self):
        return self.resources

    def location_effects(self):
        """This method is called when an agent lands on this location."""
        pass
