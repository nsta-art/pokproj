import time

import pygame as pg

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake Game")
back_ground =pg.image.load("photo_2025-08-12_14-28-32.jpg")
score = 1
fon = 1
prg = 0
prg1 = 0
key = 0
ks = 0
ks1 = 0
prg2 = 0
prg3 = 0
class Meny(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_13-23-04.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (500, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    def update(self):
        if score == 1:
            self.rect.x = 100
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000
    def render(self):

        screen.blit(self.image, self.rect)
    def mousee(self):
        global score
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score =2
class Meny1_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-29_15-53-33.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (500, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    def update(self):
        if score == 1:
            self.rect.x = 100
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000
    def render(self):

        screen.blit(self.image, self.rect)
    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score =13
            fon = 12
class Meny2_1(pg.sprite.Sprite):
    global score
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
    def update(self):
        if score == 2:
            self.rect.x = 500
            self.rect.y = 400
        else:
            self.rect.x = 2000
            self.rect.y = 2000
    def render(self):

        screen.blit(self.image, self.rect)
    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 3
            fon = 3


class Meny2_2(pg.sprite.Sprite):
    global score
    global fon
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
    def update(self):
        if score == 2:
            self.rect.x = 500
            self.rect.y = 600
        else:
            self.rect.x = 20000
            self.rect.y = 20000
    def render(self):

        screen.blit(self.image, self.rect)
    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 2
            fon = 2
class Meny2_3(pg.sprite.Sprite):
    global score
    global fon
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

    def update(self):
        if score == 2:
            self.rect.x = 500
            self.rect.y = 800
        else:
            self.rect.x = 20000
            self.rect.y = 20000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 2
            fon = 2


class Play1_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-09_12-37-24.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 3:
            self.rect.x = 985
            self.rect.y = 300
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 4
            fon = 4

class Play1_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-54.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 3:
            self.rect.x = 35
            self.rect.y = 300
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 15


class Play2_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-39.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 4:
            self.rect.x = 35
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 14
class Play2_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-45.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 4:
            self.rect.x = 985
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 13
class Play2_3(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-12_14-28-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 4:
            self.rect.x = 500
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 5
            fon = 5



class Play3_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_13-13-30.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 5:
            self.rect.x = 985
            self.rect.y = 300
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 7
            fon = 7

class Play3_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_13-13-40.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 5:
            self.rect.x = 35
            self.rect.y = 300
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        global prg1
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 6
            fon = 6




class Play4_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-43.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 6:
            self.rect.x = 35
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 16
class Play4_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-48.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 6:
            self.rect.x = 985
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        global key
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 8
            fon = 8
            key = 1

class Play4_3(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-37-15.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 6:
            self.rect.x = 985
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 17
class Play4_4(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 6 :
            self.rect.x = 35
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        global prg
        global prg2
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 5
            fon = 5
            prg = 1
            prg2 = 1

class Play5_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-33-03.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 7:
            self.rect.x = 35
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 18
class Play5_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-59.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 7:
            self.rect.x = 985
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 19
class Play5_3(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-14_15-32-53.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 7:
            self.rect.x = 985
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global fon
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            fon = 9
            if key == 1:
                score = 10
            if key == 0:
                score = 9
class Play5_4(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 7 :
            self.rect.x = 35
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global prg2
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 5
            fon = 5
            prg1 = 1
            prg2 = 1


class Play6_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 8 :
            self.rect.x = 500
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 6
            fon = 6
            prg = 1
class Play6_3(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 9 :
            self.rect.x = 500
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 7
            fon = 7
            prg1 = 1
class Play6_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-29_14-48-08.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 0 :
            self.rect.x = 35
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global key
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 3
            fon = 3
            prg1 = 0
            key = 0
            prg =0
class Play6_4(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-29_15-35-56.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 0 :
            self.rect.x = 985
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global key
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 1
            fon = 1
            prg1 = 0
            key = 0
            prg =0
class Play6_5(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 13 :
            self.rect.x = 1000
            self.rect.y = 900
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 1
            fon = 1
class Play6_6(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-24_15-18-49.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 5 :
            self.rect.x = 500
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global prg3
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 4
            fon = 4
            prg3 = 1

class Play7_1(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-29_15-17-43.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 10 :
            self.rect.x = 500
            self.rect.y = 500
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global key
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 11
            fon = 10
class Play7_2(pg.sprite.Sprite):
    global score

    def __init__(self):  # Fixed double underscores
        super().__init__()
        try:
            # Load image and scale it
            self.image = pg.image.load('photo_2025-08-29_15-17-43.jpg').convert_alpha()
            self.image = pg.transform.scale(self.image, (900, 150))
        except pg.error:
            # Create a placeholder if image fails to load
            self.image = pg.Surface((100, 100), pg.SRCALPHA)
            pg.draw.circle(self.image, (255, 0, 0), (50, 50), 50)  # Red circle placeholder

        # Get rectangle and position at center
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    def update(self):
        if score == 11 :
            self.rect.x = 500
            self.rect.y = 700
        else:
            self.rect.x = 2000
            self.rect.y = 2000

    def render(self):

        screen.blit(self.image, self.rect)

    def mousee(self):
        global score
        global  fon
        global prg1
        global key
        global prg
        mouse_pos = where_mouse_pressed(0)
        mouse_posijin = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_posijin) and mouse_pos:
            time.sleep(0.5)
            score = 0
            fon = 11
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
    meny11 = Meny1_1()
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
    play44 = Play4_4()
    play51 = Play5_1()
    play52 = Play5_2()
    play53 = Play5_3()
    play54 = Play5_4()
    play61 = Play6_1()
    play62 = Play6_2()
    play63 = Play6_3()
    play64 = Play6_4()
    play65 = Play6_5()
    play66 = Play6_6()
    play71 = Play7_1()
    play72 = Play7_2()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


        if fon == 0:
            back_ground = pg.image.load("photo_2025-08-28_16-01-36.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))


        if fon == 1:
            back_ground = pg.image.load("photo_2025-08-12_14-28-32.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 2:
            back_ground = pg.image.load("photo_2025-08-12_14-28-28.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))


        if fon == 3:
            back_ground = pg.image.load("photo_2025-08-28_15-24-38.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 4 and prg3 == 0:
            back_ground = pg.image.load("photo_2025-08-28_15-28-54.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))
        if fon == 4 and prg3 == 1:
            back_ground = pg.image.load("photo_2025-08-29_16-37-25.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 5 and prg2 == 0:
            back_ground = pg.image.load("photo_2025-08-28_15-45-43.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))
        if fon == 5 and prg2 == 1:
            back_ground = pg.image.load("photo_2025-08-29_16-30-13.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 6 and prg == 0:
            back_ground = pg.image.load("photo_2025-08-28_15-51-19.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 7 and prg1 == 0:
            back_ground = pg.image.load("photo_2025-08-28_15-59-05.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 6 and prg == 1:
            back_ground = pg.image.load("photo_2025-08-28_15-51-28.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 7 and prg1 ==1:
            back_ground = pg.image.load("photo_2025-08-28_15-59-27.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 8:
            back_ground = pg.image.load("photo_2025-08-28_16-23-02.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))



        if fon == 9 and key ==0:
            back_ground = pg.image.load("photo_2025-08-28_16-44-50.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 9 and key == 1:
            back_ground = pg.image.load("photo_2025-08-28_16-44-55.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 10 :
            back_ground = pg.image.load("photo_2025-08-29_15-13-40.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 11 :
            back_ground = pg.image.load("photo_2025-08-29_15-34-26.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))
        if fon == 12 :
            back_ground = pg.image.load("photo_2025-08-29_15-53-50.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 13 :
            back_ground = pg.image.load("photo_2025-08-29_16-11-56.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 14 :
            back_ground = pg.image.load("photo_2025-08-29_16-18-22.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 15 :
            back_ground = pg.image.load("photo_2025-08-29_16-13-27.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 16 :
            back_ground = pg.image.load("photo_2025-08-29_16-12-44.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 17:
            back_ground = pg.image.load("photo_2025-08-29_16-22-17.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 18 :
            back_ground = pg.image.load("photo_2025-08-29_16-26-55.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if fon == 19 :
            back_ground = pg.image.load("photo_2025-08-29_16-26-59.jpg")
            back_ground = pg.transform.scale(back_ground, (SCREEN_WIDTH, SCREEN_HEIGHT))



        print(score)
        meny.update()
        meny.mousee()
        meny11.update()
        meny11.mousee()
        meny21.update()
        meny21.mousee()
        meny22.update()
        meny22.mousee()
        play11.update()
        meny23.update()
        meny23.mousee()
        play11.mousee()
        play12.update()
        play12.mousee()
        play21.update()
        play21.mousee()
        play22.update()
        play22.mousee()
        play23.update()
        play23.mousee()
        play31.update()
        play31.mousee()
        play32.update()
        play32.mousee()
        play41.update()
        play41.mousee()
        play42.update()
        play42.mousee()
        play43.update()
        play43.mousee()
        play44.update()
        play44.mousee()
        play51.update()
        play51.mousee()
        play52.update()
        play52.mousee()
        play53.update()
        play53.mousee()
        play54.update()
        play54.mousee()
        play61.update()
        play61.mousee()
        play62.update()
        play62.mousee()
        play63.update()
        play63.mousee()
        play64.update()
        play64.mousee()
        play65.update()
        play65.mousee()
        play66.update()
        play66.mousee()
        play71.update()
        play71.mousee()
        play72.update()
        play72.mousee()


        # Rendering
        screen.blit(back_ground, (0, 0))
        meny.render()
        meny11.render()
        meny21.render()
        meny22.render()
        meny23.render()
        play11.render()
        play12.render()
        play21.render()
        play22.render()
        play23.render()
        play31.render()
        play32.render()
        play41.render()
        play42.render()
        play43.render()
        play44.render()
        play51.render()
        play52.render()
        play53.render()
        play54.render()
        play61.render()
        play62.render()
        play63.render()
        play64.render()
        play65.render()
        play66.render()
        play71.render()
        play72.render()

        screen.blit(meny.image, meny.rect)
        screen.blit(meny11.image, meny11.rect)
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
        screen.blit(play44.image, play44.rect)
        screen.blit(play51.image, play51.rect)
        screen.blit(play52.image, play52.rect)
        screen.blit(play53.image, play53.rect)
        screen.blit(play54.image, play54.rect)
        screen.blit(play61.image, play61.rect)
        screen.blit(play62.image, play62.rect)
        screen.blit(play63.image, play63.rect)
        screen.blit(play64.image, play64.rect)
        screen.blit(play65.image, play65.rect)
        screen.blit(play66.image, play66.rect)
        screen.blit(play71.image, play71.rect)
        screen.blit(play72.image, play72.rect)

        pg.display.flip()
        clock.tick(60)
    pg.quit()
if __name__ == '__main__':
    main()