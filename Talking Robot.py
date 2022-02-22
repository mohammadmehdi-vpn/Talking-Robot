
import os 
from colorama import Fore , init
os.system('cls')
init()
import pyttsx3

print(Fore.RED + '''┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                 ██╗   ██╗██████╗ ███╗   ██╗                 │
│                 ██║   ██║██╔══██╗████╗  ██║                 │
│                 ██║   ██║██████╔╝██╔██╗ ██║                 │
│                 ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║                 │
│                  ╚████╔╝ ██║     ██║ ╚████║                 │
│                   ╚═══╝  ╚═╝     ╚═╝  ╚═══╝                 │
│                                       by mohammadmehdi.vpn  │
└─────────────────────────────────────────────────────────────┘''')

i = int(input(Fore.YELLOW + '15 + 20 ? '))

hr = ['a' , 'b' , 'c' , 'd' , 'e' ,
      'f' , 'g' , 'h' , 'i' ,'j' ,
      'k' , 'l' , 'm', 'm' , 'n' , 
      'o' , 'p' , 'q' , 's' , 'r' ,
      't' , 'u' , 'v' , 'w' , 'x' ,
      'y' , 'z']

if i == 35:
    text = 'aly'
    sound = pyttsx3.init()
    sound.setProperty('rate' , 110)
    sound.say(text)
    sound.runAndWait()
    
    while True:

        text = input(Fore.RED + 'enter text: ')
        mtn2 = pyttsx3.init()
        mtn2.setProperty('rate' , 110)
        mtn2.say(text)
        mtn2.runAndWait()
        
else:
    
    text = 'eshtba'
    sound = pyttsx3.init()
    sound.setProperty('rate' , 110)
    sound.say(text)
    sound.runAndWait()
    exit()
    
    