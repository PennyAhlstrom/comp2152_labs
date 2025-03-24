import functions

# class Character:
#     def __init__(self, small_dice_options=None, big_dice_options=None):
#         self.__combat_strength = functions.small_dice_roll(small_dice_options)
#         self.__health_points = functions.big_dice_roll(big_dice_options)

class Character:
    def __init__(self, health_points, combat_strength):
        self.__combat_strength = combat_strength
        self.__health_points = health_points

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, combat_strength):
        self.__combat_strength = combat_strength

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, health_points):
        self.__health_points = health_points

    def __del__(self):
        print("The Character object is being destroyed by the garbage collector.")