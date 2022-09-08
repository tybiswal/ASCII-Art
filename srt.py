# This code helps to print ascii art in terminal
import pyfiglet
from termcolor import colored, cprint

color_array = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

msg = input("What word would you like to print in ASCII?: ")
clr = input("What color should it be in?:\nType your selection from the following: " + str(color_array) + "\n")
# font_ascii = input("What font should it be in?:\nType your selection from the following")

ascii_art = pyfiglet.figlet_format(msg, font='6x10')
colored_ascii = colored(ascii_art, clr)
cprint(ascii_art, clr)

print(pyfiglet.FigletFont.getFonts())
