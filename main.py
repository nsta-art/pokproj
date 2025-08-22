import pygame as pg

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1880, 1040
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake Game")
score = 1
fon = 1



class Meny(pg.sprite.Sprite):
    global score
    def __init__(self):

        super().__init__()

        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_13-23-04.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (500, 100))



        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    def update(self):
        if score == 1:
            self.rect.x = 700
            self.rect.y = 600
        else:
            self.rect.x = 2000
            self.rect.y = 2000
    def render(self):
        screen.blit(self.image, self.rect)
    def mousee(self):
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            meny_2()
            print("4")

class Meny2_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-29-08.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        self.rect.x = 700
        self.rect.y = 600
        if score == 2:
            self.rect.x = 500
            self.rect.y = 400
        if score != 2:
            self.rect.x = 2000
            self.rect.y = 2000
class Meny2_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-58.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 2:
            self.rect.x = 500
            self.rect.y = 600
        if score != 2:
            self.rect.x = 2000
            self.rect.y = 2000
class Meny2_3(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-29-04.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 2:
            self.rect.x = 500
            self.rect.y = 800
        if score != 2:
            self.rect.x = 2000
            self.rect.y = 2000

class Play1_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-09_12-37-24.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 3:
            self.rect.x = 550
            self.rect.y = 850
        if score != 3:
            self.rect.x = 2000
            self.rect.y = 200
class Play1_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-54.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 3:
            self.rect.x = 550
            self.rect.y = 650
        if score != 3:
            self.rect.x = 2000
            self.rect.y = 2000

class Play2_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-39.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 4:
            self.rect.x = 985
            self.rect.y = 750
        if score != 4:
            self.rect.x = 2000
            self.rect.y = 2000
class Play2_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 4:
            self.rect.x = 135
            self.rect.y = 750
        if score != 4:
            self.rect.x = 2000
            self.rect.y = 2000
class Play2_3(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-45.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 4:
            self.rect.x = 550
            self.rect.y = 900
        if score != 4:
            self.rect.x = 2000
            self.rect.y = 2000

class Play3_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_13-13-40.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 5:
            self.rect.x = 135
            self.rect.y = 750
        if score != 5:
            self.rect.x = 2000
            self.rect.y = 2000
class Play3_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_13-13-30.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 5:
            self.rect.x = 985
            self.rect.y = 750
        if score != 5:
            self.rect.x = 2000
            self.rect.y = 2000

class Play4_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-43.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 6:
            self.rect.x = 135
            self.rect.y = 750
        if score != 6:
            self.rect.x = 2000
            self.rect.y = 2000
class Play4_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-48.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 6:
            self.rect.x = 985
            self.rect.y = 750
        if score != 6:
            self.rect.x = 2000
            self.rect.y = 2000
class Play4_3(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-37-15.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 6:
            self.rect.x = 550
            self.rect.y = 900
        if score != 6:
            self.rect.x = 2000
            self.rect.y = 2000

class Play5_1(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-37-15.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 7:
            self.rect.x = 135
            self.rect.y = 900
        if score != 7:
            self.rect.x = 2000
            self.rect.y = 2000
class Play5_2(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-53.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 7:
            self.rect.x = 985
            self.rect.y = 750
        if score != 7:
            self.rect.x = 2000
            self.rect.y = 2000
class Play5_3(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-33-03.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 7:
            self.rect.x = 135
            self.rect.y = 750
        if score != 7:
            self.rect.x = 2000
            self.rect.y = 2000
class Play5_4(pg.sprite.Sprite):
    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-59.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (800, 125))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        if score == 7:
            self.rect.x = 985
            self.rect.y = 900
        if score != 7:
            self.rect.x = 2000
            self.rect.y = 2000




def meny():
    score = 1
    fon = 1
def meny_2():
    global score
    score = 2
    fon = 1
    print(score)
def meny_21():
    score = 2
    fon = 2
def play_1():
    score = 3
    fon = 3
def play_2():
    score = 4
    fon = 4
def play_3():
    score = 5
    fon = 5
def play_4():
    score = 6
    fon = 6
def play_5():
    score = 7
    fon = 7
def final():
    score = 8
    fon = 8







3











class Crosshair:
    def __init__(self):  # Fixed double underscores
        try:
            self.image = pg.image.load("photo_2025-08-12_12-47-34.jpg").convert_alpha()
            self.image = pg.transform.scale(self.image, (30, 30))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (0, 0, 255), (50, 50), 50)  # Blue circle placeholder

        self.rect = self.image.get_rect()
        self.rect.center = pg.mouse.get_pos()  # Start at mouse position

    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.center = pg.mouse.get_pos()
def where_mouse_pressed(mouse_key):
    """Return mouse position if specified button is pressed"""
    if pg.mouse.get_pressed()[mouse_key]:
        return pg.mouse.get_pos()
    return None

def main():

    cross = Crosshair()  # Create crosshair here
    clock = pg.time.Clock()
    meny = Meny()
    meny21 = Meny2_1()
    meny22 = Meny2_2()
    meny23 = Meny2_3()
    play11 = Play1_1()
    play12 = Play1_2()
    play21 = Play2_1()
    play22 = Play2_2()
    play23 = Play2_3()
    play31 = Play3_1()
    play32 = Play3_2()
    play41 = Play4_1()
    play42 = Play4_2()
    play43 = Play4_3()
    play51 = Play5_1()
    play52 = Play5_2()
    play53 = Play5_3()
    play54 = Play5_4()




    running = True
    while running:
        # Handle events first
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update game state
        meny.update()
        meny.mousee()

        # Rendering

        meny.render()

        screen.blit(meny21.image, meny21.rect)
        screen.blit(meny22.image, meny22.rect)
        screen.blit(meny23.image, meny23.rect)
        screen.blit(play11.image, play11.rect)
        screen.blit(play12.image, play12.rect)
        screen.blit(play21.image, play21.rect)
        screen.blit(play22.image, play22.rect)
        screen.blit(play23.image, play23.rect)
        screen.blit(play31.image, play31.rect)
        screen.blit(play32.image, play32.rect)
        screen.blit(play41.image, play41.rect)
        screen.blit(play42.image, play42.rect)
        screen.blit(play43.image, play43.rect)
        screen.blit(play51.image, play51.rect)
        screen.blit(play52.image, play52.rect)
        screen.blit(play53.image, play53.rect)
        screen.blit(play54.image, play54.rect)


        cross.draw()

        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == '__main__':
    main()