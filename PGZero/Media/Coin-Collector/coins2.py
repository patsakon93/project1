import pgzrun 
from random import randint

width = 800 
heigth = 600

fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200 ,200

score = 0
game_over = False

fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('skyblue')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white', topleft=(10, 10))
    if game_over:
        screen.fill('black')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10, 10), fontsize=50)

def place_coin():
    coin.x = randint(20, (width - 20))
    coin.y = randint(20, (heigth - 20))

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 15
        if fox.x <= 20:
            fox.x = 800 
    elif keyboard.right:
        fox.x = fox.x + 15
        if fox.x >= 800:
            fox.x =  20
    elif keyboard.up:
        fox.y = fox.y - 15
        if fox.y <= 20:
            fox.y = 600
    elif keyboard.down:
        fox.y = fox.y + 15
        if fox.y >= 600:
            fox.y = 20


    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 10.0)
place_coin()
pgzrun.go()