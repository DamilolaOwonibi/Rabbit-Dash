# game option/settings
TITLE = "Rabbit Dash!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "Georgia"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.1
PLAYER_GRAV = 0.9
PLAYER_JUMP = 22

# Game properties
BOOST_POWER = 70
POW_SPAWN_PCT = 10
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
				(WIDTH / 2 - 50, HEIGHT * 3 / -50),
				(125, HEIGHT - 350),
				(350, 200),
				(175, 100),
				(500, 300)]

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BROWN = (100, 30, 0)
ORANGE = (255, 100, 0)
LIGHTBLUE = (51, 153, 255)
BGCOLOR = LIGHTBLUE
