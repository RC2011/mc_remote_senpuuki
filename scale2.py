import sys
import pygame
from pygame.locals import Rect
from LCD_font_senpuuki import LCD_font_styles_se
from LCD_font_senpuuki import LCD_font_se
from pygame.locals import *
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
from time import sleep

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

x, y, z = -21, 0, 17

for _i in range(5):
    for _i in range(5):
        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
        z += 1
    x -= 1
    z -= 5
y += 1
x += 4
z += 1
for _i in range(3):
    for _i in range(3):
        mc.setBlock(x, y, z, block.WHITE_CONCRETE)
        z += 1
    x -= 1
    z -= 3
y += 1
x += 2
z += 1
for _i in range(4):
    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
    y += 1
y -= 1
x -= 2
for _i in range(5):
     mc.setBlock(x, y, z, block.WHITE_CONCRETE)
     z += 1
y += 1
mc.setBlock(x, y, z, block.WHITE_CONCRETE)
y += 1
z += 1
for _i in range(5):
    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
    y += 1
x -= 1
mc.setBlock(x, y, z, block.WHITE_CONCRETE)
x -= 1
y += 1
for _i in range(5):
    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
    z -= 1
y -= 1
mc.setBlock(x, y, z, block.WHITE_CONCRETE)
y -= 1
x -= 1
for _i in range(5):
    mc.setBlock(x, y, z, block.WHITE_CONCRETE)
    y -= 1
x += 2
