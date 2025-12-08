import random
import csv
import argparse

#need to finish argparse mostly for the rolls and how it takes the numbers
#and puts them in a table or list
parser = argparse.ArgumentParser(description="this script is a D20, a 20 sided dice that will show you what you get, 1 is low 20 is high ")

parser.add_argument (
'rolls',
roll=int,
help="how many dice you want to roll"
)
#need to add a argparse for excel sheet export

low = 1
high = 20



number= random.randint(low, high)




print(number)