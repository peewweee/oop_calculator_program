# Creating a calculator program using OOP concepts
# Phoebe Rhone L. Gangoso | BSCPE 1-4

import pyfiglet

# Header
def Header():
    print("\033[0;33m ")
    title_text = " Welcome to Phoebe's Calculator! "
    title_line = title_text.center(150, "*")
    print(title_line)
    print("")

# Loading animation
def Loading():
    import time
    for i in range(3):
        print("\033[0;34m Calculating ", end="\N{slightly smiling face}")
        for j in range(4):
            print(".", end="")
            time.sleep(0.25)
        print("\r", end="")
    print("\033[0;32m DONE!\N{grinning face}")
    print("")

# Thank you prompt
def Exit():
    print("\033[0;35m ")
    print(pyfiglet.figlet_format("Thank you!", font="isometric3", width=150))