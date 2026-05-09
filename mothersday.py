import random
import os
import time



heart = [
"                                                 wwwww           wwwww",
"                                             wwwwwwwwwwwww   wwwwwwwwwwwww",
"                                          wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                              wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                 wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                     wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                         wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                           wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                               wwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                                 wwwwwwwwwwwwwwwwwwwwwww",
"                                                   wwwwwwwwwwwwwwwwwww",
"                                                     wwwwwwwwwwwwwww",
"                                                       wwwwwwwwwww",
"                                                         wwwwwww",
"                                                           www",
"                                                           ",
"                                                            !"]



frame = 0

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clearscreen()
    for row in heart:
        newrow = ""
        for pos, char in enumerate(row):
            if char == "w":
                letter_index = (pos + frame) % len("iloveyoumom")
                newrow = newrow + "iloveyoumom"[letter_index]
            else:
                newrow = newrow + char
        print("\033[91m" + newrow + "\033[0m")
    frame = frame + 1
    time.sleep(0.1)
