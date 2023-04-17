import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'a': pygame.image.load('img/wp06.png').convert(),
                         'b': pygame.image.load('img/wp07.png').convert(),
                         'c': pygame.image.load('img/wp05.png').convert(),
                         'd': pygame.image.load('img/wp08.png').convert(),
                         'e': pygame.image.load('img/wp03.png').convert(),
                         'm': pygame.image.load('img/C01.png').convert()
                         }

    def background(self, view):
        sky_offset = -5 * math.degrees(view) % WIDTH
        self.sc.blit(self.textures['m'], (sky_offset, 0))
        self.sc.blit(self.textures['m'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['m'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_previous_direction_horizon):
        ray_casting(self.sc, player_pos, player_previous_direction_horizon, self.textures)
 
    def display_storyline_with_payoffs(self, text, x, y,covid,isvacc):
        isvaccinated = isvacc
        indicator_num = 0
        display_text1 = '  '
        render1 = self.font.render(display_text1, 0, WHITE)
        value1 = int(x)
        value2 = int(y)
        counter = 0 

        if value1 >= 80 and value1 <=230:
            if value2 >= 600:
                counter = 1
                if isvaccinated == True:
                    display_text1 ="You destroyed Covid."
                    render1 = render1 = self.font.render(display_text1, 0, SANDY)
                else:
                    covid[1] = 1                    
                    indicator_num = 4
                    display_text1 = "You got infected with Covid virus."
                    render1 = render1 = self.font.render(display_text1, 0, BLUE)

        if value1 >= 475 and value1 <= 630:
            if value2 <= 190:
                counter = 1
                if isvaccinated == True:
                    display_text1 ="You destroyed Covid."
                    render1 = render1 = self.font.render(display_text1, 0, SANDY)
                else:
                    covid[2] = 1
                    indicator_num = 4
                    display_text1 = "You got infected with Covid virus."
                    render1 = render1 = self.font.render(display_text1, 0, BLUE)

        if value1 >= 669 and value1 <= 800:
            if value2 >= 300 and value2 <= 435:
                counter = 1
                if isvaccinated == True:
                    display_text1 ="You destroyed Covid."
                    render1 = render1 = self.font.render(display_text1, 0, SANDY)
                else:
                    covid[3] = 1
                    indicator_num = 4
                    display_text1 = "You got infected with Covid virus."
                    render1 = render1 = self.font.render(display_text1, 0, BLUE)

        if value1 >= 964 and value1 <= 1122:
            if value2 >= 600 and value2 <= 695:
                counter = 1
                if isvaccinated == True:
                    display_text1 ="You destroyed Covid."
                    render1 = render1 = self.font.render(display_text1, 0, SANDY)
                else:
                    covid[4] = 1
                    indicator_num = 4
                    display_text1 = "You got infected with Covid virus."
                    render1 = render1 = self.font.render(display_text1, 0, BLUE)

        if value1 >= 584 and value1 <= 700:
            if value2 >= 579 and value2 <= 690:
                isvaccinated = True
                counter = 1
                indicator_num = 3
                display_text1 = "You got vaccinated."
                for i in covid:
                    covid[i] = 0
                render1 = render1 = self.font.render(display_text1, 0, SANDY)

        if value1 >= 1000 and value1 <= 1085:
            if value2 >= 95 and value2 <= 205:
                isvaccinated = True
                counter = 1
                indicator_num = 3
                display_text1 = "You got vaccinated."
                for i in covid:
                    covid[i] = 0
                render1 = render1 = self.font.render(display_text1, 0, SANDY)
        
        if counter == 0:
            display_text1 = text
            render1 = self.font.render(display_text1, 0, WHITE)
         
        self.sc.blit(render1, TEXT_POS)
        self.payoff_accomplice(indicator_num, covid)
        return isvaccinated
        
    def payoff_accomplice(self, indicator_num,covid):
        display_text1 = '  '
        payoff_render1 = self.font.render(display_text1, 0, WHITE)
        

        if indicator_num == 3:   
            pos =[TEXT_POS2,TEXT_POS3,TEXT_POS4,TEXT_POS5]
            line = 0                  
            for i in covid:
                if covid[i] == 1:
                    display = 'PAY OFF '+str(i)+': You destroyed Covid' 
                    payoff_render1 = self.font.render(display, 0, WHITE)
                    self.sc.blit(payoff_render1, pos[line])
                    line += 1

           

    def mini_map(self, accomplice):
        self.sc_map.fill(BLACK)
        map_x, map_y = accomplice.x // MAP_SCALE, accomplice.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(accomplice.perspective),
                                                 map_y + 12 * math.sin(accomplice.perspective)), 2)
        pygame.draw.circle(self.sc_map, BLUE, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, RED, (x, y, MAP_TILE, MAP_TILE))            
        self.sc.blit(self.sc_map, MAP_POS)

      
        
        
        
        
        
 