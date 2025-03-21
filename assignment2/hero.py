import random
import functions

class Hero:
    combat_strength = 0
    health_points = 0
    def __init__(self, small_dice_options=None, big_dice_options=None):
        self.combat_strength = functions.small_dice_roll(small_dice_options)
        self.health_points = functions.big_dice_roll(big_dice_options)

    # Hero's Attack Function
    def hero_attacks(combat_strength, health_points):
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
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points