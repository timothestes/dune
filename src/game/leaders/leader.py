class Leader:
    def __init__(
        self,
        name: str,
        name_friendly: str,
        faction: str,
        faction_friendly: str,
        signet_ring_ability: str or dict,
        passive_ability: str,
        house_hagal_playable: bool,
    ):
        self.name = name
        self.name_friendly = name_friendly
        self.faction = faction
        self.faction_friendly = faction_friendly
        self.signet_ring_ability = signet_ring_ability
        self.passive_ability = passive_ability
        self.house_hagal_playable = house_hagal_playable

    def __str__(self):
        return self.name_friendly
