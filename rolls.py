import random
import argparse

Parser=argparse.ArgumentParser(
    description= "this is a D20 dice roll a D20 is a 20 sided dice, you can change the max dice face from 20 to anything, the script will roll a dice and export it to a .txt file"
)
Parser.add_argument("high", type=int, nargs="?", default="20", help="change the max dice face number")
                    
Myargs= Parser.parse_args()

low = 1




rolls= random.randint(low, Myargs.high)
print(rolls)




file_path = "rolls.txt"


try:
    with open(file_path, "x") as file:
         file.write(f"{rolls}")

         print(f"The file {file_path} was written succesfully go look at your roll!")
except FileExistsError:
    print("this file already exists")