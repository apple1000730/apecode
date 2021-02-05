from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z=mc.player.getPos()
y-=1
for i in range(10):
    z-=1
    x+=10
    for j in range(10):
        color=random.randrange(0,16)
        mc.setBlock(x,y,z,35,color)
        x-=1
           