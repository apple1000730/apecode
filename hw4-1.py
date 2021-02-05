from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Calafornia=[]
Florida=[]
Washington=[]

for i in range(1,4):
    Calafornia.append(1*i)
for i in range(1,4):
    Florida.append(2*i)
for i in range(1,4):
    Washington.append(3*i)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,8,str(Calafornia),str(Florida),str(Washington))
