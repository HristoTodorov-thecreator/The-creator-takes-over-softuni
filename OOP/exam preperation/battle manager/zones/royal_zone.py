from project.zones.base_zone import BaseZone

class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self,code: str):
        super().__init__(code,RoyalZone.INITIAL_VOLUME)

    def zone_info(self):
        ships = self.get_ships()
        pirate_count = sum(1 for ship in ships if ship.__class__.__name__ == "PirateBattleship")
        lines = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(ships)}, {pirate_count} out of them are Pirate Battleships."
        ]
        if ships:
            ship_names = ", ".join(ship.name for ship in ships)
            lines.append(f"#{ship_names}#")

        return "\n".join(lines)