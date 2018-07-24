#-* -coding:UTF-8-* -#
#中文注释模板
import shelve
import pygame, sys 
from pygame.locals import *

class Game:
    def __init__(self,path="./init/load"):
        self.set = shelve.open(path)
        windows = self.set['windows']
        print(windows)
        print(pygame.init())
        # 设置窗口的大小，单位为像素 
        screen = pygame.display.set_mode((windows['w'], windows['h']))   
        # 设置窗口标题 
        pygame.display.set_caption(windows['caption'])
        background = pygame.image.load(windows['background'])
        screen.blit(background, (windows['w'], windows['h']))                                 
        pass
    def Loop(self):
        # 程序主循环 
        while True:     
        # 获取事件   
            for event in pygame.event.get():     
                # 判断事件是否为退出事件     
                if event.type == QUIT:       
                    # 退出pygame       
                    pygame.quit()       
                    # 退出系统       
                    sys.exit() 
            self.draw
        pass
    def draw(self):
        pygame.display.update()  
if __name__ == '__main__':
    game = Game()
    game.Loop()