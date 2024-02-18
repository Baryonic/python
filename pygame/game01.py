import pygame as p
import random as r

PS = 50
ES = PS / 2
ER = 5000
EH = 2
ED = 0
EA = 1
RP = 10

p.init()
i = p.display.Info()
SW, SH = i.current_w, i.current_h
sc = p.display.set_mode((SW, SH))
cl = p.time.Clock()

class E(p.sprite.Sprite):
    def __init__(self, s, h, d, a, c, x, y):
        super().__init__()
        self.i = p.Surface((s, s))
        self.i.fill(c)
        self.r = self.i.get_rect(center=(x, y))
        self.h = h
        self.d = d
        self.a = a

    def td(self, amt):
        self.h -= max(0, amt - self.d)
        if self.h <= 0:
            self.kill()

class P(E):
    def __init__(self, x, y):
        super().__init__(PS, 10, 1, 1, (0, 255, 0), x, y)
        self.s = 5

    def u(self):
        k = p.key.get_pressed()
        if k[p.K_a]:
            self.r.x -= self.s
        if k[p.K_d]:
            self.r.x += self.s
        if k[p.K_w]:
            self.r.y -= self.s
        if k[p.K_s]:
            self.r.y += self.s

class P2(E):
    def __init__(self, x, y):
        super().__init__(PS, 10, 1, 1, (0, 0, 255), x, y)
        self.s = 5

    def u(self):
        k = p.key.get_pressed()
        if k[p.K_LEFT]:
            self.r.x -= self.s
        if k[p.K_RIGHT]:
            self.r.x += self.s
        if k[p.K_UP]:
            self.r.y -= self.s
        if k[p.K_DOWN]:
            self.r.y += self.s

class En(E):
    def __init__(self):
        super().__init__(ES, EH, ED, EA, (255, 255, 255), r.choice([0, SW - ES]), r.choice([0, SH - ES]))

pl = P(SW/2 - PS, SH/2)
pl2 = P2(SW/2 + PS, SH/2)
en = p.sprite.Group()

rn = True
lst = p.time.get_ticks()
while rn:
    for e in p.event.get():
        if e.type == p.QUIT:
            rn = False

    pl.u()
    pl2.u()

    if pl.r.colliderect(pl2.r):
        pl.td(pl2.a)
        pl2.td(pl.a)
        dx = pl.r.x - pl2.r.x
        dy = pl.r.y - pl2.r.y
        dist = max(1, (dx**2 + dy**2)**0.5)
        pl.r.x += dx/dist * RP
        pl.r.y += dy/dist * RP
        pl2.r.x -= dx/dist * RP
        pl2.r.y -= dy/dist * RP

    nw = p.time.get_ticks()
    if nw - lst > ER:
        e = En()
        en.add(e)
        lst = nw

    h = p.sprite.spritecollide(pl, en, False)
    for hit in h:
        pl.td(hit.a)
        hit.td(pl.a)
        if pl.h <= 0:
            print("Player 1 died! Retry?")
            rn = False

    h2 = p.sprite.spritecollide(pl2, en, False)
    for hit in h2:
        pl2.td(hit.a)
        hit.td(pl2.a)
        if pl2.h <= 0:
            print("Player 2 died! Retry?")
            rn = False

    en.update()

    sc.fill((0, 0, 0))
    sc.blit(pl.i, pl.r)
    sc.blit(pl2.i, pl2.r)
    for e in en:
        sc.blit(e.i, e.r)
    p.display.flip()

    cl.tick(60)
p.quit()
