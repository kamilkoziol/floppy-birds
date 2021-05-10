import pygame
from Characters import Bird, Surface, PipePair

SCREEN_SIZE = (576,800)
BIRD_SIZE = (41, 29)
BIRD_POS = (100,int(SCREEN_SIZE[1]/2))

def draw_frame(win, char):
    char.draw(win)

def main():
    screen_size = SCREEN_SIZE
    pygame.init()
    win = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Polska gurom")
    clock = pygame.time.Clock()

    floor_image = "floor.png"
    floor = Surface(floor_image, (0, screen_size[1]-100))
    floor.surface = pygame.transform.scale2x(floor.surface)

    bg_image = "bg.png"
    bg = Surface(bg_image, (0,0))
    bg.surface = pygame.transform.scale2x(bg.surface)

    bird_image = "bird.png"
    bird = Bird(bird_image, BIRD_POS)

    pipe_pair_list = [PipePair()]

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 2000)

    run = True
    while run:
        clock.tick(60)
        dt = clock.get_time()

        bird.jump(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump(dt)
                    bird.new_jump = True
            if event.type == SPAWNPIPE:
                pipe_pair_list.append(PipePair())

        bg.draw(win)

        floor.draw(win)
        floor.move_left(v=2)

        for pipe_pair in pipe_pair_list:
            pipe_pair.draw(win)
            pipe_pair.move_left(v=2)

        if pipe_pair_list[0].remove:
            del pipe_pair_list[0]

        #bird.draw(win)
        pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    main()