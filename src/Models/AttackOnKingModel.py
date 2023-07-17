class AttackOnKing:
    def __init__(self, attackers_ray: int, check_count: int, attackers_bitmask: int, attackers: list,
                 opponent_attacks: int):
        self.attackers_ray = attackers_ray
        self.check_count = check_count
        self.attackers = attackers
        self.attackers_bitmask = attackers_bitmask
        self.opponent_attacks = opponent_attacks
