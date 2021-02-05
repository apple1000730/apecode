from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

answer=randrange(0,16)
ID=mc.getPlayerEntityId("VHOvho")
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data>answer:
             mc.postToChat('猜錯了！')
        if data<answer:
             mc.postToChat('猜錯了！')
        else:
            mc.setBlock(hit.pos,57)
            mc.postToTitle(ID,"答對了，恭喜！")
            break