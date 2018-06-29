from item import Weapon

# Format : name, desc, dmg_range, sp_cost, type=1, value
wood_sword = Weapon('wood_sword',
                    "A sword made of wood for training",
                    (2,5), 5, 10)

iron_sword = Weapon('iron_sword',
                    """A sword made of iron. Can cut through flesh so don't swing
                    it around like a wooden sword""",
                    (5,7), 10, 50)

steel_sword = Weapon('steel_sword',
                     """A sword made of iron mixed with other stuff. Will cut through
                     your iron sword""",
                     (10,12), 10, 100)

iron_dagger = Weapon('iron_dagger',
                     """Dagger to hide in you cloak and be sneaky.
                     Just like a thief. Cloak and Dagger.""",
                     (3,5), 6, 30)

steel_dagger = Weapon('steel_dagger',
                      """Steel dagger for quick silent assassinations.""",
                      (8,10), 6, 80)

steel_mace = Weapon('steel_mace',
                    """A mace to crack open your enemie's head.""",
                    (13,16), 8, 80)