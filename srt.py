# This code helps to print ascii art in terminal
import pyfiglet
from termcolor import colored

msg = input("What word would you like to print in ASCII?: ")
clr = input("What color should it be in?: ")
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=clr)
print(colored_ascii)
