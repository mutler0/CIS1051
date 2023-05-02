import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',43)
pygame.display.set_caption('CHIMP TRIBULATIONS')

LIGHTGREEN = (89, 171, 87)
GREEN = (42, 120, 46)
enabledButton = True
LIVES = 3



#make them count upX
#make sure they dont overlapX
#make them flip when one is clickedX
#make them click in orderX
#loose life when click incorrectly and start over####
#flip once clicked one######


class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, 'WHITE')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (70,70))
        global LIVES
        global amount
        lives_text = font.render("LIVES: "+ "I"*LIVES, True, 'WHITE')
        if self.enabled:
            if self.checkClick():
                if int(self.text) == 1:
                    pygame.draw.rect(screen,LIGHTGREEN,button_rect, 3, 5)
                    button_text = font.render(self.text, True, GREEN)
                    #flip to lightgreen
                if int(self.text) == amount:
                    amount += 1
                    #restart
                if int(self.text) == Button.next_button_num:
                    Button.next_button_num += 1
                    self.enabled = False
                else:
                    LIVES -= 1
                    #restart
            if self.enabled:
                pygame.draw.rect(screen, GREEN, button_rect, 0, 5)
                pygame.draw.rect(screen, 'WHITE', button_rect, 3, 5)
            else:
                pygame.draw.rect(screen,GREEN,button_rect, 2, 5)
                button_text = font.render(self.text, True, GREEN)
        else:
            pygame.draw.rect(screen,GREEN,button_rect, 2, 5)
            button_text = font.render(self.text, True, GREEN)
        screen.blit(lives_text, (20, 20))
        screen.blit(button_text, (self.x_pos+13, self.y_pos+12))

    def checkClick(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (70,70))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

Button.next_button_num = 1


#generate block positions
def generate_random_position(positions):
    x = random.randint(50,720)
    y = random.randint(50,520)
    while any(abs(x - prev_x) < 80 and abs(y - prev_y) < 80 for prev_x, prev_y in positions):
        x = random.randint(30,720)
        y = random.randint(30,520)
    positions.append((x, y))
    return x, y

amount = 5
positions = []
while len(positions) < amount:
    x, y = generate_random_position(positions)
    

# create buttons using the generated positions
buttons = []
for pos, digit in zip(positions, range(1, amount+1)):
    x, y = pos
    digit_str = str(digit)
    button = Button(digit_str, x, y, enabledButton)
    buttons.append(button)

#puts buttons on display
def generate_buttons():
    for button in buttons:
        button.draw()

#restart display for lives and amounts
def restart_game():
    global LIVES, amount, positions, buttons
    positions.clear()
    buttons.clear()
    positions = []
    buttons = []
    while len(positions) < amount:
        x, y = generate_random_position(positions)
    for pos, digit in zip(positions, range(1, amount+1)):
        x, y = pos
        digit_str = str(digit)
        button = Button(digit_str, x, y, enabledButton)
        buttons.append(button)
        #was not sure how to restart the self.text back when restart
        #scatters again


run = True
while run:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # check for changes in LIVES and amount
    if LIVES != len("I"*LIVES) or amount != len(buttons):
        restart_game()
    if LIVES == 0:
        screen.fill(GREEN)
        gameover = font.render("GAME OVER", True, 'WHITE')
        screen.blit(gameover, (280, 200))
        
    generate_buttons()
    
    pygame.display.flip()

pygame.quit()

