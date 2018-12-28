#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def temps(time):
    """float->str
    time >=0
    renvoie une chaine de caracteres de la forme de HH:MM:SS
    à partir du nombre de seconde time"""

    #heure:str
    heure=""
    #h:number
    h=math.floor(time//3600)

    if h == 0:
        heure="00"
    elif h <10:
        heure="0"+str(h)
    else :
        heure=str(h)

    #minute:str
    minute=""
    #m:number
    m=math.floor((time%3600)//60)

    if m == 0:
        minute="00"
    elif m < 10 :
        minute="0"+str(m)
    else:
        minute=str(m)
        
    #seconde:str
    seconde=""
    #s:number
    s=math.floor(time%60)

    if s ==0:
        seconde="00"
    elif s <10:
        seconde="0"+str(s)
    else:
        seconde=str(s)
    
    return heure+":"+minute+":"+seconde
    
