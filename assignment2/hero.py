import functions
from character import Character

class Hero(Character):

    def __init__(self, small_dice_options=None, big_dice_options=None):
        self.combat_strength = functions.small_dice_roll(small_dice_options)
        self.health_points = functions.big_dice_roll(big_dice_options)

        super().__init__(self.health_points, self.combat_strength)

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector.")
        super().__del__()

    # Hero's Attack Function
    def hero_attacks(self, combat_strength, monster):
        ascii_image = """
@                                                           
@ @                                                         
@  @                              @@@@                       
@   @                           @ @@   @                     
 @  @                    @@ @@ @@      @                    
  @  @               @@       @     @  @                    
   @  @              @ @@        @  @  @                    
   @  @            @@   @@ @     @  @  @                     
    @  @                   @@@@  @  @  @                     
     @ @            @         @ @   @   @                 
      @ @            @       @ @    @    @ @  @  @          
      @  @            @  @@@  @      @         @             
       @ @                    @@@@@     @@   @           
        @ @ @@@        @ @  @      @                        
     @@@@@@ @@@        @    @      @                        
     @@@@@ @@         @@@ @  @@  @@@                        
         @@@@        @  @    @@    @                        
              @@@@         @@       @                       
          @    @         @@@        @@                      
           @@@        @     @@@@@@    @                     
            @@@    @       @           @@                   
             @  @       @@ @@@@@@@@@@   @                    
                     @                  @                   
                   @           @        @                   
                  @      @@@@   @@       @                  
                 @    @@          @        @  @             
                @ @@@@@             @@        @ @           
                      @                @@@   @    @         
                 @    @                    @@       @       
                  @   @@                      @@      @@    
                   @   @                          @@@    @@ 
                    @  @                               @   @
                   @    @                              @  @ 
                @@     @                              @  @  
              @@@@@@                                 @@@          """
        print(ascii_image)
        # Created using https://www.asciiart.eu/image-to-ascii
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(monster.health_points) + ")")
        if combat_strength >= monster.health_points:
            # Player was strong enough to kill monster in one blow
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            monster.health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(monster.health_points))
        return monster.health_points