class Location:
    def __init__(
        self,
        name: str,
        friendly_name: str,
        agent_icon: str,
        combat_space: bool = False,
        controller_resources: dict = None,
        cost: dict = None,
        resources: dict = None,
        requirements: dict = None,
    ):
        self.name = name
        self.friendly_name = friendly_name
        self.combat_space = combat_space
        self.agent_icon = agent_icon
        self.resources = resources or {}
        self.controller_resources = controller_resources
        self.cost = cost

    def get_resources(self):
        return self.resources

    def location_effects(self):
        """This method is called when an agent lands on this location."""
        pass
