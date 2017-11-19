import sys
import pygame
from pygame.locals import *

pygame.init()

# ディスプレイ作成
SURFACE = pygame.display.set_mode( (1280,720) )
pygame.display.set_caption("Just Window")

sysFont = pygame.font.SysFont(None, 36)

def quit():
    pygame.quit()
    sys.exit()

def main():

    # 初期化
    counter = 0

    # メインループ
    while True:
        # 画面クリア
        SURFACE.fill((0,0,0))

        # イベントハンドル
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        counter += 1
        count_image = sysFont.render(
            "count is {}".format(counter),
            True,
            (255,255,255)
        )
        SURFACE.blit(count_image, (50,50))
        # 画面更新
        pygame.display.update()

if __name__ == '__main__':
    main()
