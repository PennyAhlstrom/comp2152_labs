import random
import functions

class Monster:
    combat_strength = 0
    health_points = 0

    def __init__(self, small_dice_options=None, big_dice_options=None):
        self.combat_strength = functions.small_dice_roll(small_dice_options)
        self.health_points = functions.big_dice_roll(big_dice_options)

    # Monster's Attack Function
    def monster_attacks(combat_strength, health_points):
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
        print("    |    Monster's Claw (" + str(combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points