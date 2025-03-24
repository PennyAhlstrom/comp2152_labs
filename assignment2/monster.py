import functions
from character import Character

class Monster(Character):

    def __init__(self, small_dice_options=None, big_dice_options=None):
        self.combat_strength = functions.small_dice_roll(small_dice_options)
        self.health_points = functions.big_dice_roll(big_dice_options)

        super().__init__(self.health_points, self.combat_strength)

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector.")
        super().__del__()

    # Monster's Attack Function
    def monster_attacks(self, combat_strength, hero):
        # asciiart.eu
        ascii_image2 = """                                                                                                                                            
                                   @@@                                
                               @  @@ @@  @                            
                           @@ @@  @   @ @@@ @@                        
              @@@          @@@@ @@@   @@@ @@@           @@@           
            @@@ @          @@ @   @       @  @          @@@@@         
           @@@  @        @@                   @@        @  @@@        
           @   @@@     @        @@@@@@@@@        @     @@@@  @        
           @  @  @@  @@        @@  @@@  @@        @@  @   @  @        
            @@     @@          @ @@@@@@@ @          @@     @@         
        @@@  @     @           @@@@@@@@@ @@          @     @  @@@     
     @@@@ @@ @@   @            @ @@@@@@@ @            @   @  @  @@@@  
     @     @  @@ @@            @@@@@@@@@@@            @  @   @     @  
     @@@ @@ @@  @@      @@        @@@@@        @@      @@  @@@   @@@  
     @@       @@ @         @@@             @@@         @ @@   @    @  
      @@@       @@        @ @ @@@@@@@@@@@@@@@ @        @@       @@@   
         @       @     @  @  @@@@@ @ @ @ @@@  @  @@    @       @      
          @@     @@       @@                 @@       @      @@       
            @@    @        @@@@@         @@@@@        @    @@         
               @@@@@        @@ @         @ @@        @@@@@            
                    @         @@@        @@         @                 
                     @@          @@@@@@@          @@                  
                       @                         @                    
                       @ @@                   @@ @                    
                      @@    @@@           @@@    @@                   
                      @          @@@@@@@          @                   
                     @           @     @          @@                  
                      @@@@       @    @@       @@@@                   
                         @@@@@  @@     @@  @@@@                                                                                                                                                                       
                 """
        print(ascii_image2)
        # Created using https://www.asciiart.eu/image-to-ascii
        print("    |    Monster's Claw (" + str(combat_strength) + ") ---> Player (" + str(hero.health_points) + ")")
        if combat_strength >= hero.health_points:
            # Monster was strong enough to kill player in one blow
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            hero.health_points -= combat_strength
            print("    |    The monster has reduced Player's health to: " + str(hero.health_points))
        return hero.health_points