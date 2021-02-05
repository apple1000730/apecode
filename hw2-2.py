from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
Block = random.randrange(0,150)
x,y,z = mc.player.getPos()

mc.setBlocks(x-10,y-50,z-60,x+10,y+50,z+60,Block)