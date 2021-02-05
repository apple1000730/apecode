from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()

Block = random.randrange(0,150)
mc.setBlocks(x-10,y-10,z-10,x+10,y+10,z+10,1)
mc.setBlocks(x-9,y-9,z-9,x+9,y+9,z+9,0)