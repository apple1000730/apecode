from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

Position = mc.player.getPos()
x=Position.x
y=Position.y
z=Position.z

time.sleep(10)
mc.player.setPos(x,y,z)