#Nether and Overworld coordinates calculator.
#By Zhyren
import os
import colorama
from colorama import Fore
import ctypes
import math
import time

ctypes.windll.kernel32.SetConsoleTitleW("Noverworld v1.1 by ZhyrenSmile")
os.system("cls")

def menu():
	options = input(">> ")
	if options == "1":
		os.system("cls")
		return nethertoover()
	if options == "2":
		os.system("cls")
		return overtonether()
	if options == "cls":
		os.system("cls")
		return menulogo()
	else:
		print("Exitting...")
		time.sleep(2)
		os.system("cls")


print(Fore.BLUE + """ $$\   $$\                                                                           $$\       $$\ 
$$$\  $$ |                                                                          $$ |      $$ |
$$$$\ $$ | $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ | $$$$$$$ |
$$ $$\$$ |$$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\ $$ |$$  __$$ |
$$ \$$$$ |$$ /  $$ |\$$\$$  / $$$$$$$$ |$$ |  \__|$$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ |$$ /  $$ |
$$ |\$$$ |$$ |  $$ | \$$$  /  $$   ____|$$ |      $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |
$$ | \$$ |\$$$$$$  |  \$  /   \$$$$$$$\ $$ |      \$$$$$\$$$$  |\$$$$$$  |$$ |      $$ |\$$$$$$$ |
\__|  \__| \______/    \_/     \_______|\__|       \_____\____/  \______/ \__|      \__| \_______|
                                                                                                  
                                                                                                  
                                                                                                 """)


print(Fore.RED+ "1) ɴᴇᴛʜᴇʀ ᴛᴏ ᴏᴠᴇʀᴡᴏʀʟᴅ " + "\n\n" + Fore.GREEN + "2) ᴏᴠᴇʀᴡᴏʀʟᴅ ᴛᴏ ɴᴇᴛʜᴇʀ\n\n"+ Fore.CYAN + "cls: main menu\n" + Fore.RED)

def menulogo():
	print(Fore.CYAN + """
	$$$\  $$ |                                                                          $$ |      $$ |
	$$$$\ $$ | $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ | $$$$$$$ |
	$$ $$\$$ |$$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\ $$ |$$  __$$ |
	$$ \$$$$ |$$ /  $$ |\$$\$$  / $$$$$$$$ |$$ |  \__|$$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ |$$ /  $$ |
	$$ |\$$$ |$$ |  $$ | \$$$  /  $$   ____|$$ |      $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |
	$$ | \$$ |\$$$$$$  |  \$  /   \$$$$$$$\ $$ |      \$$$$$\$$$$  |\$$$$$$  |$$ |      $$ |\$$$$$$$ |
	\__|  \__| \______/    \_/     \_______|\__|       \_____\____/  \______/ \__|      \__| \_______|
                                                                                                  
                                                                                                  
                                                                                                 """)
	print(Fore.RED+ "1) ɴᴇᴛʜᴇʀ ᴛᴏ ᴏᴠᴇʀᴡᴏʀʟᴅ " + "\n\n" + Fore.GREEN + "2) ᴏᴠᴇʀᴡᴏʀʟᴅ ᴛᴏ ɴᴇᴛʜᴇʀ\n\n"+ Fore.CYAN + "cls: main menu\n" + Fore.RED)
	menu()

def nethertoover():
	n = 8
	x = input(Fore.RED+ "x coordinate: ")
	y = input(Fore.RED+"z coordinate: ")
	z = input(Fore.RED+"y coordinate: ")
	print(Fore.RED+"Nether coordinates: ")
	print(x + "\n"+y + "\n"+z)
	print(" ")
	print(Fore.GREEN+"Overworld coordinates: ")
	print(int(x) * int(n))
	print(y)
	print(int(z) * int(n))
	print(" ")
	return menu()

def overtonether():
	c = 8
	x = input(Fore.GREEN+"x coordinate: ")
	y = input(Fore.GREEN+"z coordinate: ")
	z = input(Fore.GREEN+"y coordinate: ")
	print(Fore.GREEN+"Overworld coordinates: ")
	print(int(x) / int(c))
	print(y)
	print(int(z) / int(c))
	print(" ")
	print(Fore.RED+"Nether coordinates: ")
	print(x + "\n"+y + "\n"+z)
	print(" ")
	return menu()

menu()