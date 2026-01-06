import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    管理游戏资源和行为的类
    """
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # 暂时注释掉全屏，改用固定分辨率
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # 设置背景色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # 监听键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """"响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  # 👈 最后退出 Python


    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并且运行
    ai = AlienInvasion()
    ai.run_game()