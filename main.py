import os, sys
import pygame
from Enemy import *
from Player import *
from Bullet import *
from Boss1 import *
from Boss2 import *
from Boss3 import *
from pygame.locals import *

screen = pygame.display.set_mode ((960,540))
clock = pygame.time.Clock()
stage = open("stage.txt", "r")
highscores = open("highscores.txt", "r+")

highscores.seek(0,0)
points = highscores.readline()
hs_points = points.split()
bestscore = hs_points[0]

def pause(x, sky, skyrect, player, playergroup, enemies, player_bullets, bullets, input_qt, bossgroup):
    i = 0

    def display_yes_no():
        screen.blit(options[0], (skyrect.x + 300 + x, skyrect.y + 300))
        screen.blit(options[1], (skyrect.x + 550 + x, skyrect.y + 300))

    def refresh_yes_no(i, yes, no):
        if i == 1:
            yes = movable_text("Yes", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
            no = movable_text("No", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))

        elif i == 0:
            yes = movable_text("Yes", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            no = movable_text("No", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))

        return yes, no

    def yes_no(i):
        if i == 1:
            options[i] = movable_text("Yes", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            i = 0
            options[i] = movable_text("No", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))

        elif i == 0:
            options[i] = movable_text("No", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            i = 1
            options[i] = movable_text("Yes", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))

        return i

    base_font = font_create(40)
    underline_font = font_create(40)
    underline_font.set_underline(True)

    yes, no = 0, 0
    yes, no = refresh_yes_no(i, yes, no)

    options = [yes, no]

    screen.blit(sky, skyrect)
    display_yes_no()
    if player.on:
        player.on = True
        playergroup.draw(screen)
    if player.alive:
        player.on = True
        playergroup.draw(screen)
        pygame.time.set_timer(USEREVENT + 3, 0)
    bossgroup.draw(screen)
    enemies.draw(screen)
    player_bullets.draw(screen)
    bullets.draw(screen)
    screen.blit(input_qt, (skyrect.x + 200 + x, skyrect.y + 100))
    pygame.display.update()

    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                elif event.key == K_RETURN:
                    if i == 0:
                        return True
                    return False
                elif event.key == K_RIGHT:
                    i = yes_no(i)
                elif event.key == K_LEFT:
                    i = yes_no(i)

        options[0], options[1] = refresh_yes_no(i, yes, no)
        screen.blit(sky, skyrect)
        if player.on:
            player.on = True
            playergroup.draw(screen)
        if player.alive:
            player.on = True
            playergroup.draw(screen)
            pygame.time.set_timer(USEREVENT + 3, 0)
        bossgroup.draw(screen)
        enemies.draw(screen)
        player_bullets.draw(screen)
        bullets.draw(screen)
        display_yes_no()
        screen.blit(input_qt, (skyrect.x + 200 + x, skyrect.y + 100))
        pygame.display.update()

def god_mode(x, sky, skyrect, player, playergroup, enemies, player_bullets, bullets, bossgroup, inv):
    i, ps, es, pf = 0, 0, 0, 0
    cheat = True

    def display_options():
        screen.blit(options[0], (skyrect.x + 200 + x, skyrect.y + 100))
        screen.blit(options[1], (skyrect.x + 200 + x, skyrect.y + 150))
        screen.blit(options[2], (skyrect.x + 200 + x, skyrect.y + 200))
        screen.blit(options[3], (skyrect.x + 200 + x, skyrect.y + 250))
        #screen.blit(options[4], (skyrect.x + 200 + x, skyrect.y + 300))

    def refresh(i, ps, es, pf, inv, p_speed, e_speed, p_firerate, invincible, sky, skyrect):
        if i == 0:
            p_speed = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
            e_speed = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            p_firerate = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            invincible = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))

        elif i == 1:
            p_speed = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            e_speed = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
            p_firerate = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            invincible = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))

        elif i == 2:
            p_speed = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            e_speed = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            p_firerate = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))
            invincible = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))

        elif i == 3:
            p_speed = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            e_speed = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            p_firerate = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            invincible = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))

        return p_speed, e_speed, p_firerate, invincible

    def delta(n, i, ps, es, pf, inv):
        if i == 0:
            ps += n
            return ps, es, pf, inv
        elif i == 1:
            es += n
            return ps, es, pf, inv
        elif i == 2:
            if  -450 < pf < 450:
                pf += n * 50
            elif pf == 450 and n < 0:
                pf += n * 50
            elif pf == -450 and n > 0:
                pf += n * 50
            return ps, es, pf, inv
        elif i == 3:
            if inv == 1:
                inv = 0
            else: inv = 1
            return ps, es, pf, inv

    def aux(n, i):
        if i == 0:
            options[i] = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, base_font, (250,250,250))
            if n == 1:
                options[i + n] = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
                i += 1
            else:
                options[3] = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))
                i = 3

        elif i == 1:
            options[i] = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            if n == 1:
                options[i + n] = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))
                i += 1
            else:
                options[i + n] = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
                i -= 1

        elif i == 2:
            options[i] = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            if n == 1:
                options[i + n] = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))
                i += 1
            else:
                options[i + n] = e_speed = movable_text("Enemy Speed  +=  < " + str(es) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
                i -= 1

        elif i == 3:
            options[i] = movable_text("Invincible  +=  < " + str(inv) + " >", skyrect.x + x + 100, 100, sky, base_font, (250,250,250))
            if n == 1:
                options[0] = movable_text("Player Speed  +=  < " + str(ps) + " >", skyrect.x + x + 200, 50, sky, underline_font, (250,250,250))
                i = 0
            else:
                options[i + n] = movable_text("Player Firerate  +=  < " + str(pf) + " >", skyrect.x + x + 100, 100, sky, underline_font, (250,250,250))
                i -= 1
        return i

    base_font = font_create(30)
    underline_font = font_create(30)
    underline_font.set_underline(True)

    p_speed, e_speed, p_firerate, invincible = 0, 0, 0, 0
    p_speed, e_speed, p_firerate, invincible = refresh(i, ps, es, pf, inv, p_speed, e_speed, p_firerate, invincible, sky, skyrect)

    options = [p_speed, e_speed, p_firerate, invincible]

    screen.blit(sky, skyrect)
    display_options()
    if player.on:
        player.on = True
        playergroup.draw(screen)
    if player.alive:
        player.on = True
        playergroup.draw(screen)
        pygame.time.set_timer(USEREVENT + 3, 0)
    bossgroup.draw(screen)
    enemies.draw(screen)
    player_bullets.draw(screen)
    bullets.draw(screen)
    pygame.display.update()

    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_g:
                    return player, enemies, es, pf, inv, cheat
                elif event.key == K_DOWN:
                    i = aux(1, i)
                elif event.key == K_UP:
                    i = aux(-1, i)
                elif event.key == K_LEFT:
                    ps, es, pf, inv = delta(-1, i, ps, es, pf, inv)
                    player.speed += ps
                    if player.speed < 1:
                        player.speed = 1
                    for enemy in enemies:
                        enemy.speed += es
                        if enemy.speed < 0:
                            enemy.speed = 2
                elif event.key == K_RIGHT:
                    ps, es, pf, inv = delta(1, i, ps, es, pf, inv)
                    player.speed += ps
                    for enemy in enemies:
                        enemy.speed += es

        options[0], options[1], options[2], options[3] = refresh(i, ps, es, pf, inv, p_speed, e_speed, p_firerate, invincible, sky, skyrect)
        screen.blit(sky, skyrect)
        if player.on:
            player.on = True
            playergroup.draw(screen)
        if player.alive:
            player.on = True
            playergroup.draw(screen)
            pygame.time.set_timer(USEREVENT + 3, 0)
        bossgroup.draw(screen)
        enemies.draw(screen)
        player_bullets.draw(screen)
        bullets.draw(screen)
        display_options()
        pygame.display.update()

def update_highscore(score):

    def move_char(step):
        last_char[letter] = char[letter]
        char[letter] = int(char[letter]) + step
        char[letter] = int(char[letter]) % len(alfa)
        if letter == 0:
            text_to_screen(alfa[last_char[letter]], 64 , background.get_rect().center[0] * 0.8, background.get_rect().center[1] + 100, background, (10,10,10))
            text_to_screen(alfa[char[letter]], 64 , background.get_rect().center[0] * 0.8, background.get_rect().center[1] + 100, background, (250,250,250))
        elif letter == 1:
            text_to_screen(alfa[last_char[letter]], 64 , background.get_rect().center[0], background.get_rect().center[1] + 100, background, (10,10,10))
            text_to_screen(alfa[char[letter]], 64 , background.get_rect().center[0], background.get_rect().center[1] + 100, background, (250,250,250))
        else:
            text_to_screen(alfa[last_char[letter]], 64 , background.get_rect().center[0] * 1.2, background.get_rect().center[1] + 100, background, (10,10,10))
            text_to_screen(alfa[char[letter]], 64 , background.get_rect().center[0] * 1.2, background.get_rect().center[1] + 100, background, (250,250,250))
        chars[letter] = alfa[char[letter]]

    pygame.mixer.music.load("resources/Stairway to heaven.mp3")
    pygame.mixer.music.play(0, 0)

    highscores.seek(0,0)
    points = highscores.readline()
    hs_points = points.split()
    for i in range(0,len(hs_points)):
        hs_points[i] = int(hs_points[i])
    players = highscores.readline()
    hs_players = players.split()

    update_hs = True
    alfa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    char =  [0,0,0]
    last_char = [0,0,0]
    letter = 0
    last_letter = 0
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((10,10,10))
    chars = ['A','A','A']
    text_to_screen("Your Score", 48, background.get_rect().midtop[0], background.get_rect().midtop[1]+128, background, (250,250,250))
    text_to_screen(str(score), 48 , background.get_rect().midtop[0], background.get_rect().midtop[1]+180, background, (250,250,250))
    text_to_screen("Choose your tag and press ENTER", 24 , background.get_rect().midtop[0], background.get_rect().midtop[1]+240, background, (250,250,250))


    letter1 = text_to_screen(chars[0], 64 , background.get_rect().center[0] * 0.8, background.get_rect().center[1] + 100, background, (250,250,250))
    letter2 = text_to_screen(chars[1], 64 , background.get_rect().center[0], background.get_rect().center[1] + 100, background, (250,250,250))
    letter3 = text_to_screen(chars[2], 64 , background.get_rect().center[0] * 1.2, background.get_rect().center[1] + 100, background, (250,250,250))

    letters = [letter1, letter2, letter3]
    draw_option_line(background, 0, letters, (250, 250, 250))

    screen.blit(background, (0,0))
    pygame.display.update()

    while update_hs:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    times = hs_points.count(score)
                    hs_points.append(score)
                    hs_points.sort()
                    hs_points.reverse()
                    ind = hs_points.index(score)
                    ind += times
                    if ind == len(hs_points)-1:
                        return
                    else:
                        hs_points.pop()
                        hs_players_copy = list(hs_players)
                        hs_players[ind] = chars[0]+chars[1]+chars[2]
                        ind += 1
                        while ind != len(hs_players):
                            hs_players[ind] = hs_players_copy[ind-1]
                            ind += 1
                        highscores.seek(0,0)
                        for i in range(0, len(hs_points)-1):
                            highscores.write(str(hs_points[i])+' ')
                        highscores.write(str(hs_points[-1])+'\n')
                        for i in range(0, len(hs_players)-1):
                            highscores.write(hs_players[i]+' ')
                        highscores.write(hs_players[-1]+'\n')
                        return

                    return
                elif event.key == K_RIGHT:
                    last_letter = letter
                    letter += 1
                    letter = letter % len(letters)
                    draw_option_line(background, last_letter, letters, (10,10,10))
                    draw_option_line(background, letter, letters, (250,250,250))
                elif event.key == K_LEFT:
                    last_letter = letter
                    letter -= 1
                    letter = letter % len(letters)
                    draw_option_line(background, last_letter, letters, (10,10,10))
                    draw_option_line(background, letter, letters, (250,250,250))
                elif event.key == K_UP:
                    move_char(1)
                elif event.key == K_DOWN:
                    move_char(-1)

        screen.blit(background, (0,0))
        pygame.display.update()



def highscore_menu():
    pygame.mixer.music.load("resources/Nickelback.mp3")
    pygame.mixer.music.play(0, 8)
    hs_menu = True
    space = 28
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((10,10,10))
    screen.blit(background, (0,0))
    pygame.display.update()

    text_to_screen("Highscores", 64, background.get_rect().midtop[0], background.get_rect().midtop[1]+32, background, (250,250,250))
    highscores.seek(0,0)
    points = highscores.readline()
    hs_points = points.split()
    players = highscores.readline()
    hs_players = players.split()

    for i in range(0,len(hs_points)):
        text_to_screen(str(hs_players[i]) + '.............................' + str(hs_points[i]), 48, background.get_rect().centerx, background.get_rect().midtop[1]+64+space, background, (250,250,250))
        space += 42

    text_to_screen("Press ESC to return to main menu", 24, background.get_rect().midtop[0], background.get_rect().midbottom[1]-12, background, (250,250,250))

    while hs_menu:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return


        screen.blit(background, (0,0))
        pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def font_create(fontsize):
    fontname = os.path.join('resources', 'ethno.ttf')
    font = pygame.font.Font(fontname, fontsize)
    return font

def movable_text(message, x, y, background, font, color):
    text = font.render(message, 1, color)
    return text

def text_to_screen(message, fontsize, x, y, background, color):
    font = font_create(fontsize)
    text = movable_text(message, x, y, background, font, color)
    textpos = text.get_rect()
    textpos.centerx = x
    textpos.centery = y
    background.blit(text, textpos)
    return textpos

def draw_option_line(background, option, options, color):
    pygame.draw.line(background, color, (options[option].bottomleft[0], options[option].bottom), \
    (options[option].bottomright[0], options[option].bottom), 3)

def menu(background):
    pygame.mixer.music.load("resources/TMWSTW.mp3")
    pygame.mixer.music.play()

    menu = True
    option = 0
    last_option = 0
    highscores.seek(0,0)
    points = highscores.readline()
    hs_points = points.split()
    global bestscore

    text_to_screen("Curtain of Death", 64, background.get_rect().centerx, background.get_rect().centery * 0.5, background, (250,250,250))
    play = text_to_screen("Play", 40, background.get_rect().centerx, background.get_rect().centery * 1.1, background, (250,250,250))
    score = text_to_screen("Highscores", 40, background.get_rect().centerx, background.get_rect().centery * 1.3, background, (250,250,250))
    exit = text_to_screen("Exit", 40, background.get_rect().centerx, background.get_rect().centery * 1.5, background, (250,250,250))
    text_to_screen("Best Score: " + str(bestscore), 28, background.get_rect().centerx, background.get_rect().centery * 1.75, background, (10,10,10))
    text_to_screen("Best Score: " + str(hs_points[0]), 28, background.get_rect().centerx, background.get_rect().centery * 1.75, background, (250,250,250))
    bestscore = hs_points[0]
    text_to_screen("Sick Stag Studios", 16, background.get_rect().centerx, background.get_rect().centery * 1.95, background, (250,250,250))

    options = [play, score, exit]

    draw_option_line(background, 0, options, (250, 250, 250))

    screen.blit(background, (0,0))
    pygame.display.update()

    while menu:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    last_option = option
                    option += 1
                    option = option % len(options)
                    draw_option_line(background, last_option, options, (10,10,10))
                    draw_option_line(background, option, options, (250,250,250))
                elif event.key == K_UP:
                    last_option = option
                    option -= 1
                    option = option % len(options)
                    draw_option_line(background, last_option, options, (10,10,10))
                    draw_option_line(background, option, options, (250,250,250))
                elif event.key == K_RETURN or event.key == K_SPACE:
                    if option == 0:
                        menu = False
                    if option == 1:
                        highscore_menu()
                        pygame.mixer.music.load("resources/TMWSTW.mp3")
                        pygame.mixer.music.play()
                    if option == 2:
                        quitgame()
                elif event.key == K_ESCAPE:
                    quitgame()

        screen.blit(background, (0,0))
        pygame.display.update()

def spawn_enemy(posx, posy, speed, image, hp, firerate, x, y, pattern, prate, score):
    enemy = Enemy(posx, posy, speed, image, hp, firerate, x, y, pattern, prate, score)
    return enemy

def chrono(enemies, bossgroup, es, player):
    step = stage.readline()
    if step != '0\n':
        if step == 'boss1\n':
            bossgroup.add(Boss1())
        elif step == 'boss2\n':
            bossgroup.add(Boss2())
        elif step == 'boss3\n':
            bossgroup.add(Boss3())
        elif step == 'song2\n':
            pygame.mixer.music.load("resources/Pantera.mp3")
            pygame.mixer.music.play()
            player.hp += 1
        elif step == 'song3\n':
            pygame.mixer.music.load("resources/RideTheLightning.mp3")
            pygame.mixer.music.play()
            player.hp += 1
        elif step == '!\n':
            return True
        else:
            args = step.split()
            while args != []:
                enemies.add(spawn_enemy(int(args[0]), int(args[1]), int(args[2]) + 2 + es, args[3], int(args[4]), \
                 int(args[5]), int(args[6]), int(args[7]), int(args[8]), int(args[9]), int(args[10])))
                for ele in range(0,11):
                    args.pop(0)


def game():
    pygame.mixer.music.load("resources/Led Zeppelin.mp3")
    pygame.mixer.music.play()
    cheat = False
    running = True
    score = 0
    x = 0
    es, pf, ef, inv = 0, 0, 0, 0
    end = False
    pygame.time.set_timer(USEREVENT + 2, 500)
    player = Player(screen.get_rect().midleft, 5)
    stage.seek(0,0)

    original_sky, original_skyrect = load_image('Sky101.png',-1)
    sky, skyrect =load_image('Sky101.png',-1)
    sky_death, sky_death_rect = load_image('Sky101Death.png',-1)
    game_over = movable_text("Game Over", skyrect.x + 200 + x, skyrect.y + 100, sky, font_create(64), (250,250,250))
    input_hs = movable_text("Press ENTER to save your Highscore", skyrect.x + 16 + x, skyrect.y + 200, sky, font_create(32), (250,250,250))
    input_qt = movable_text("Quit game?", skyrect.x + 200 + x, skyrect.y + 100, sky, font_create(64), (250,250,250))
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    playergroup = pygame.sprite.GroupSingle(player)
    bossgroup = pygame.sprite.GroupSingle()
    score_rect = screen.get_rect()

    while running:
        clock.tick(60)


        lives_text = movable_text("Lives: " + str(player.hp), skyrect.topleft[0] + x, skyrect.topleft[1]+1, sky, font_create(20), (250,250,250))
        score_text = movable_text("Score: " + str(score), skyrect.topleft[0]  + x, skyrect.topleft[1], sky, font_create(20), (250,250,250))
        if skyrect.midright == screen.get_rect().midright:
            skyrect.topleft = screen.get_rect().topleft
            x = 0
        if sky_death_rect.midright == screen.get_rect().midright:
            sky_death_rect.topleft = screen.get_rect().topleft
            x = 0
        skyrect = skyrect.move(-1, 0)
        sky_death_rect = sky_death_rect.move(-1, 0)
        x += 1
        score_rect = score_rect.move(1, 0)

        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.pause()
                    running = pause(x, sky, skyrect, player, playergroup, enemies, player_bullets, bullets, input_qt, bossgroup)
                    pygame.mixer.music.unpause()
                if event.key == K_g:
                    pygame.mixer.music.pause()
                    player, enemies, es, pf, inv, cheat = god_mode(x, sky, skyrect, player, playergroup, enemies, player_bullets, bullets, bossgroup, inv)
                    pygame.mixer.music.unpause()
                if end:
                    if event.key == K_RETURN:
                        if not cheat:
                            update_highscore(score)
                        running = False

            elif event.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(USEREVENT + 1, 0)
                player.alive = True
            elif event.type == USEREVENT + 2:
                if bossgroup.sprite == None:
                    end = chrono(enemies, bossgroup, es, player)
            elif event.type == pygame.USEREVENT + 3:
                pygame.time.set_timer(USEREVENT + 4, 100)
                player.on = False
            elif event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(USEREVENT + 4, 0)
                player.on = True
            elif event.type == pygame.USEREVENT + 5:
                player.fire = True


        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            player.move(0, -1)
        if keys[K_DOWN]:
            player.move(0, 1)
        if keys[K_RIGHT]:
            player.move(1, 0)
        if keys[K_LEFT]:
            player.move(-1, 0)
        if keys[K_z] or keys[K_SPACE]:
            if player.fire:
                pygame.time.set_timer(USEREVENT + 5, 500 - pf)
                bullet = Bullet(player.rect.midright, (player.speed + 2) * -1, False)
                player_bullets.add(bullet)
                player.fire = False

        for enemy in enemies:
            if enemy.hp <= 0:
                enemies.remove(enemy)
                if enemy.hp != -1:
                    score += enemy.score
            if player.alive:
                if player.rect.colliderect(enemy.rect):
                    player.reinit(inv)
            if enemy.fire == True:
                if enemy.name == 'mob2.png':
                    bullet = Bullet(enemy.rect.midright, -(enemy.speed + 2), False)
                    bullets.add(bullet)
                bullet = Bullet(enemy.rect.midleft, enemy.speed + 2, True)
                bullets.add(bullet)
                enemy.fire = False

        for boss in bossgroup:
            if boss.hp == 0:
                bossgroup.remove(boss)
                score += boss.score
            if player.alive:
                if player.rect.colliderect(boss.rect):
                    player.reinit(inv)
            if boss.fire == True:
                if isinstance(bossgroup.sprite, Boss1):
                    bullet = Bullet((boss.rect.midleft[0]+30, boss.rect.midleft[1]+20), boss.speed + 2, True)
                    bullets.add(bullet)
                    bullet = Bullet((boss.rect.midleft[0], boss.rect.midleft[1]-20), boss.speed + 2, True)
                    bullets.add(bullet)
                else:
                    bullet = Bullet(boss.rect.midleft, boss.speed + 2, True)
                    bullets.add(bullet)
                boss.fire = False

        for bullet in player_bullets:
            if not bullet.onscreen:
                player_bullets.remove(bullet)
            for enemy in enemies:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.update(1)
                        bullet.rect.midright = screen.get_rect().midleft
                        player_bullets.remove(bullet)
            for boss in bossgroup:
                    if bullet.rect.colliderect(boss.rect):
                        boss.update(1)
                        bullet.rect.midright = screen.get_rect().midleft
                        player_bullets.remove(bullet)

        for bullet in bullets:
            if not bullet.onscreen:
                bullets.remove(bullet)
            elif player.alive:
                if bullet.rect.colliderect(player.rect):
                    player.reinit(inv)
                    bullet.rect.midright = screen.get_rect().midleft
                    bullets.remove(bullet)

        bossgroup.update(0)
        enemies.update(0)
        player_bullets.update()
        bullets.update()

        if player.hp > 0:
            screen.blit(sky, skyrect)
            if player.on:
                player.on = True
                playergroup.draw(screen)
            if player.alive:
                player.on = True
                playergroup.draw(screen)
                pygame.time.set_timer(USEREVENT + 3, 0)
            bossgroup.draw(screen)
            enemies.draw(screen)
            player_bullets.draw(screen)
            bullets.draw(screen)
        else:
            screen.blit(sky_death, sky_death_rect)
            bossgroup.draw(screen)
            enemies.draw(screen)
            player_bullets.draw(screen)
            bullets.draw(screen)
            screen.blit(game_over, (skyrect.x + 200 + x, skyrect.y + 100))
            screen.blit(input_hs, (skyrect.x + 16 + x, skyrect.y + 200))
            pygame.time.set_timer(USEREVENT + 1, 0)
            pygame.time.set_timer(USEREVENT + 3, 0)
            pygame.time.set_timer(USEREVENT + 4, 0)
            end = True

        if end and player.hp > 0:
            if not cheat:
                update_highscore(score)
            running = False

        screen.blit(score_text, (skyrect.topleft[0] + x, skyrect.topleft[1]))
        screen.blit(lives_text, (skyrect.topleft[0] + x, skyrect.topleft[1] + 20))
        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption('Curtain of Death')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((10,10,10))

    while 1:
        menu(background)
        game()

    stage.close()
    highscores.close()

if __name__ == '__main__': main()
