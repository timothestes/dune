class Location:
    def __init__(self, name, agent_icon, resources=None):
        self.name = name
        self.agent_icon = agent_icon
        self.resources = resources or {}

    def get_resources(self):
        return self.resources

    def location_effects(self):
        """This method is called when an agent lands on this location."""
        pass
