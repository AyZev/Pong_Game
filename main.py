import random
import pygame
from Assets.RGB_Colors import *

pygame.init()
pygame.display.set_caption("Ping Pong Game")

difficulty = 0.5

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200

pong_hit = pygame.mixer.Sound("Assets/pong.ogg")
game_start_sound = pygame.mixer.Sound("Assets/game_start.ogg")
game_over_sound = pygame.mixer.Sound("Assets/game_over.ogg")

img = pygame.image.load("Assets/image.jpg")
img = pygame.transform.scale(img,(SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.Font("Assets/Font.ttf", 50)

paddle_l = 20
paddle_b = 120
pong_s = 20
img2 = pygame.image.load("Assets/15133.jpg")
img2 = pygame.transform.scale(img2,(SCREEN_WIDTH,SCREEN_HEIGHT),)

def move_c_paddle(paddle:pygame.Rect, pong:pygame.Rect, pong_velocity_x):
    c_paddle_velocity = 6.5 + difficulty
    threshold = 6

    if abs(paddle.centery - pong.centery) > threshold and pong_velocity_x<0:
        if paddle.centery < pong.centery:
            paddle.y += c_paddle_velocity
        elif paddle.centery > pong.centery:
            paddle.y -= c_paddle_velocity
    if paddle.top < 0:
        paddle.top = 0
    elif paddle.bottom > screen.get_height():
        paddle.bottom = screen.get_height()


def game_over(win:bool):
    running = True
    color = green if win else red
    while running:
        text1 = font.render("Game Over!", True, color)
        text2 = font.render("Press space to play again",True,white)
        text3 = font.render("Press ESCAPE to exit",True,white)
        screen.blit(img,(0,0))
        screen.blit(text1, (screen.get_width() / 2 - text1.get_width() / 2, screen.get_height() / 2 - text1.get_height()*2))
        screen.blit(text2, (screen.get_width() / 2 - text2.get_width() / 2, screen.get_height() / 2))
        screen.blit(text3, (screen.get_width() / 2 - text3.get_width() / 2, screen.get_height() / 2 + text3.get_height()*2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    running = False
                    break
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    quit()
        pygame.display.update()


def check_collision(rect:pygame.Rect,pong:pygame.Rect):
    if rect.colliderect(pong):
        pong_hit.play()
        if rect.x<pong.center[0]<rect.x+rect.w:
            return "side"
        else:
            return "top"


def main():
    game_start_sound.play()
    pong = pygame.rect.Rect(SCREEN_WIDTH / 2 - pong_s / 2, SCREEN_HEIGHT / 2, pong_s, pong_s)
    paddle1 = pygame.rect.Rect(SCREEN_WIDTH * 19 / 20, SCREEN_HEIGHT / 2 - paddle_b / 2, paddle_l, paddle_b)
    paddle2 = pygame.rect.Rect(SCREEN_WIDTH / 20, SCREEN_HEIGHT / 2 - paddle_b / 2, paddle_l, paddle_b)
    paddle_velocity_y = 10
    pong_velocity_x = 6
    tvx = pong_velocity_x
    pong_velocity_y = 8
    tvy = pong_velocity_y
    u_score = 0
    b_score = 0
    max_score = 3

    running = True
    while running:
        if u_score == max_score or b_score == max_score:
            game_over_sound.play()
            game_over(u_score > b_score)
            break
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False


        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            if paddle1.y < SCREEN_HEIGHT-paddle1.h-5:
                paddle1.move_ip(0,paddle_velocity_y)
        elif key[pygame.K_UP]:
            if paddle1.y > 5:
                paddle1.move_ip(0,-paddle_velocity_y)


        if pong.y <= pong_s or pong.y >= SCREEN_HEIGHT-pong_s:
            pong_velocity_y *= -1
            pong_velocity_x += random.uniform(0,0.5) if pong_velocity_x > 0 else random.uniform(-0.5,0)

        if pong.x <= 0:
            u_score += 1
            pong_velocity_x = tvx
            pong_velocity_y = tvy
            pong.x = SCREEN_WIDTH/2
            pong.y = SCREEN_HEIGHT/2
            pong_velocity_x *= -1
        elif pong.x >= SCREEN_WIDTH-pong.w:
            b_score += 1
            pong_velocity_x = tvx
            pong_velocity_y = tvy
            pong.x = SCREEN_WIDTH/2
            pong.y = SCREEN_HEIGHT/2
            pong_velocity_x *= -1

        paddle1_collision = check_collision(paddle1, pong)
        paddle2_collision = check_collision(paddle2, pong)

        if paddle1_collision == "side" or paddle2_collision == "side":
            pong_velocity_y *= -1
            pong_velocity_x += random.uniform(0,0.5) if pong_velocity_x>0 else random.uniform(-0.5,0)
            if paddle1_collision == "side":
                pong.top = paddle1.bottom if pong_velocity_y > 0 else paddle1.top - pong.height
            elif paddle2_collision == "side":
                pong.top = paddle2.bottom if pong_velocity_y > 0 else paddle2.top - pong.height

        elif paddle1_collision == "top" or paddle2_collision == "top":
            pong_velocity_x *= -1
            paddle_velocity_y += random.uniform(0,0.5) if pong_velocity_y>0 else random.uniform(-0.5,0)
            if paddle1_collision == "top":
                pong.left = paddle1.right if pong_velocity_x > 0 else paddle1.left - pong.width
            elif paddle2_collision == "top":
                pong.left = paddle2.right if pong_velocity_x > 0 else paddle2.left - pong.width


        text1 = font.render(f"{b_score}",True,white)
        text2 = font.render(f"{u_score}",True,white)
        pong.move_ip(pong_velocity_x,pong_velocity_y)
        move_c_paddle(paddle2,pong,pong_velocity_x)

        screen.blit(img2,(0,0))
        pygame.draw.rect(screen,white,paddle1,border_radius=10)
        pygame.draw.rect(screen,white,paddle2,border_radius=10)
        pygame.draw.rect(screen,white,pong,border_radius=10)
        pygame.draw.line(screen,white,(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),width=3)
        screen.blit(text1,(SCREEN_WIDTH/4,SCREEN_HEIGHT/8))
        screen.blit(text2,(3*SCREEN_WIDTH/4,SCREEN_HEIGHT/8))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
pygame.quit()


