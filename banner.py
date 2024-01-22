from util.color import Color

from sys import stdout
from time import sleep
import time

def show_banner():
    txt = f"""


   {Color.CPURPLE2}▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄· ▄▄▄ .    ·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄  ▄▄▄ .▄▄▄  
  {Color.CPURPLE2}▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▀▄.▀·    ██▪ ██ ▪     ██· █▌▐█•█▌▐███•  ▪     ▐█ ▀█ ██▪ ██ ▀▄.▀·▀▄ █·
  {Color.CPURPLE2}▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐▀▀▪▄    ▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
   {Color.CPURPLE2}▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█▐█▄▄▌    ██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ ▐█▄▄▌▐█•█▌
    {Color.CPURPLE2}▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀
                                                    {Color.CRED2}                    By Atta ul Munim
                                                                                                                                                       


    
                   """
    
    credit = f">{Color.ENDC} Download Youtube Playlist and Videos{Color.ENDC}\n\n"
    
    
    for col in txt:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
    
    for col in credit:
        print(col, end="")
        stdout.flush()
        sleep(0.028)

        {Color.CPURPLE2}