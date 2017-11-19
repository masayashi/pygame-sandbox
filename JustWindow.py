import sys
import pygame
from pygame.locals import QUIT

pygame.init()

# ディスプレイ作成
SURFACE = pygame.display.set_mode( (1280,720) )
pygame.display.set_caption("Just Window")

def main():
    # メインループ
    while True:
        # 画面クリア
        SURFACE.fill((255,255,255))

        # イベントハンドル
        for event in pygame.event.get():
            if event.type == QUIT: # 終了イベント
                pygame.quit()
                sys.exit()

        # UPDATE
        pygame.display.update()

if __name__ == '__main__':
    main()
