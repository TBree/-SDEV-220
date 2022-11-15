'''
Name       :  Torri
Assignment :  18.5 Prime Numbers
Version    : 1.0
DueDate    : Dec 13,2022

(Use the Stack class) Write a program that displays the
first 50 prime numbers in descending order.
Use a stack to store prime numbers.
'''

import random
import torri_Library1 as Lib1
from Final_Stack import Stack
from Baptista_Linked_List import LinkedList

NUMBER_OF_ELEMENTS = 50

def main():# append the random elements in a list

    for i in range(1, NUMBER_OF_ELEMENTS+1):
       randomNum = random.randint(1, 50)
       print(f'| {randomNum:>2}', end='')
       
       myList = []
       even = []
       odd = []
       
       myList.append(randomNum)
       print(f'| {myList}')
       print()

       if(myList[j] % 2 == 0):
           even.append(myList[j)
        else:
            randomNumodd.append(myList[j])

        
                print(odd)

    
    Lib1.printHeader(__doc__)
           
if __name__ == "__main__":
    main()


