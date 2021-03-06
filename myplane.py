import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.active_flag = True
        self.image = pygame.image.load('image/hero1.png').convert_alpha()
        # 动画
        self.image2 = pygame.image.load('image/hero2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, \
                                        (self.height - self.rect.height - 60)
        self.speed = 10
        self.destory_index = 0
        self.destory_imgs = [
            pygame.image.load('image/hero_blowup_n1.png').convert_alpha(),
            pygame.image.load('image/hero_blowup_n2.png').convert_alpha(),
            pygame.image.load('image/hero_blowup_n3.png').convert_alpha(),
            pygame.image.load('image/hero_blowup_n4.png').convert_alpha()]
        self.active = True
        # 边缘精确检测
        pygame.mask.from_surface(self.image)

    # 移动函数
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    @property
    def active_img(self):
        return self.image if self.active_flag else self.image2

    @active_img.setter
    def active_img(self, active_flag):
        self.active_flag = active_flag
