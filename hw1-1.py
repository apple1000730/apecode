from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x=90
y=90
z=90
mc.player.setPos(x,y,z)
time.sleep(5)
mc.player.setPos(x,y,z+100)
time.sleep(5)
mc.player.setPos(x,y,z+200)