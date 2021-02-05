from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

a = input('你是誰？')
mc.postToChat('Hello'+a+',歡迎來偶家！')
mc.setBlocks(x,y,z,x+10,y+15,z+10,1)
mc.setBlocks(x+1,y+1,z+1,x+9,y+14,z+9,0)
mc.setBlocks(x+2,y+1,z,x+2,y+2,z,0)
mc.setBlocks(x+1,y+7,z+1,x+9,y+7,z+9,1)