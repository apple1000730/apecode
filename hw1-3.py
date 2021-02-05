from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    mc.postToChat('Hello,my friend!!!')
    x,y,z=mc.player.getPos()
    mc.postToChat('You are at X:' +str(x)+'y：'+str(y)+'z:'+str(z))
    time.sleep(1)
    
