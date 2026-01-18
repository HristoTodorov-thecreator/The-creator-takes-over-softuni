from project.zones.base_zone import BaseZone

class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, PirateZone.INITIAL_VOLUME)
    def zone_info(self):
        ships = self.get_ships()
        royal_count = sum(1 for ship in ships if ship.__class__.__name__ == "RoyalBattleship")

        lines = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(ships)}, {royal_count} out of them are Royal Battleships."
        ]

        if ships:
            ship_names = ", ".join(ship.name for ship in ships)
            lines.append(f"#{ship_names}#")

        return "\n".join(lines)