from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getPos()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,89)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,
    
    plantTree(x,y,z)
     