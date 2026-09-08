from senses import voice as vc
from senses import translator as tl
from commands import battery as bt
def brain():
    
    vc.recorder()
    command = tl.trancribe_small()
    print("You:" + command)
    bt.change_power_mode(command)
    
brain()

