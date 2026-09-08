from senses import voice as vc
from senses import translator as tl
from commands import battery as bt
from datetime import datetime as dt
import os
from memory import memory as mm


def brain():
    
    vc.recorder()
    command = tl.trancribe_tiny()
    mm.save_memory(command)
    print("You:" + command)
    bt.change_power_mode(command)


brain()

