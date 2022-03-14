# ❤️in name of god❤️

from pyautogui import alert
from colorama import Fore
from os import system

def encode(data):
    txt = str(data)
    passwd_1 = txt.replace("1", "0").replace("s", "'").replace("10", "9").replace("c", ",").replace("4", ":").replace(" ", ";").replace("$", "&").replace("m", "-").replace("i", "@").replace("+", "!").replace("y", ".").replace("n", "l").replace("(", "_").replace(")", "12").replace("a", "%").replace("b", "*").replace("s", "_")
    password = "wuf8chw871y78qbsvusifhcow10{"+ passwd_1 + "d4sfucledisfoesl`1"
    print(Fore.RED + f"\n\tHash: [' {password} ']")

def decode(data):
    password = str(data)
    txt = password.replace("wuf8chw871y78qbsvusifhcow10{", "").replace("0", "1").replace("d4sfucledisfoesl`1", "").replace("'", "s").replace("9", "10").replace(",", "c").replace(":", "4").replace(";", " ").replace("&", "$").replace("-", "m").replace("@", "i").replace("!", "+").replace(".", "y").replace("l", "n").replace("_", "(").replace("12", ")").replace("%", "a").replace("*", "b").replace("_", "s")
    print(Fore.GREEN + f"\n\tText: [' {txt} ']")

alert("❤️In Name Of God❤️")
system("cls")
print(Fore.BLUE + """ | | | |  / \  / ___|| | | |  / ___/ _ \/ ___|_   _/ _ \|  \/  |
 | |_| | / _ \ \___ \| |_| | | |  | | | \___ \ | || | | | |\/| |
 |  _  |/ ___ \ ___) |  _  | | |__| |_| |___) || || |_| | |  | |
 |_| |_/_/   \_\____/|_| |_|  \____\___/|____/ |_| \___/|_|  |_|
                                                                
1. encode [' HASH '] costom;
-----------------------------------------------------------------
0- decode [' HASH '] costom;""")

while True:
    select_h = input(Fore.WHITE + "\n? ")
    if select_h == "1":
        encode( input(Fore.CYAN + "\nText To HASH Costom :>> ") )
    elif select_h == "0":
        decode( input(Fore.CYAN + "\nHASH To Text: ") )
    else:
        print(Fore.YELLOW + "\nUnfifune!")


