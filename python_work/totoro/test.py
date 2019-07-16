import pygame, time

class Stats():
    def __init__(self):
        self.cnt = 1
        self.COUNT = pygame.USEREVENT + 1
        self.update_time = 1000
        pygame.time.set_timer(self.COUNT, self.update_time)
        self.fps = 0

    def update(self):
        # self.update_time = int(self.update_time * 0.98)
        # print(self.update_time)
        # pygame.time.set_timer(self.COUNT, self.update_time)
        print('fps：', self.fps)
        self.fps = 0

def check_events(stats):
    for event in pygame.event.get():
        if event.type == stats.COUNT:
            print (stats.cnt)
            stats.cnt += 1
            stats.update()


def main():
    # screen = pygame.display.set_mode((100,100))
    #
    #
    # stats = Stats()
    # while True:
    #     stats.fps += 1
    #     screen.fill((0,0,0))
    #     check_events(stats)
    #     pygame.display.flip()
    t = time.time()
    time.sleep(1)
    t2 = time.time()
    print(t2-t)


main()
