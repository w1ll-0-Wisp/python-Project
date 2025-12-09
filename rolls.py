import random
import argparse


#hello sir, here is my project! ive been practicing argparse for a bit, on my pc so that why you dont see it in the github account, these practices were not for this project but for personal use
#this was very fun to do, i watched a few videos for argparsing and what you can do with random! thank you for the great semester and hope that we can speak again in the future!
#script by Eric Carriere 000906679 
# ^w^


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
