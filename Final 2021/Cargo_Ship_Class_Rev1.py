'''
Name       : Do Not Sink My Cargo Ship Game
Author     : Torri Baptista
Version    : 1.0
Due Date   : 12/13/2021
Filename   : CargoShip_Class_Rev1.py
'''
import torri_Library1 as Lib1
from Baptista_Linked_List import LinkedList
import random

class CargoShip:
    def __init__(self, inFileName):
        self.fileName = inFileName
        self.letters = ""
        self.guesses = ""
        self.misses= ""
        self.hiddenWord = ""
        self.displayWord = ""
        self.status = ""
        #
        self.flagEnd = False
        self.flagSink = False
        #
        self.listWords = []
        self.listCrates = ["","","","","","",""]
        #
        #=================================================================
        self.hiddenWord = "time"
        self.displayWord = "time"
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.status = "Sorry, you lost! "
        self.flagSink = True
        self.flagEnd = True
        self.listCrates = ["a","b","c","d","x","y","z"]
        self.misses = "abcdxyz"
        #============================================================

        flagCheck = self.readFileName()
        if flagCheck == True:
            # print(self.listWords)  
            self.game()
    #===============================

    def initializeGame(self):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.guesses = ""
        self.misses= ""
        self.hiddenWord = ""
        self.displayWord = ""
        self.status = "Begin game."
        #
        self.flagEnd = False
        self.flagSink = False
        # 
        self.listCrates = ["","","","","","",""]
        #
        self.getHiddenWord()
        
    def printPanel(self):
        strGS = self.status
        strDW = self.displayWord
        lblGS = "game status  :"
        lblDW = "display word :"
        
        if self.flagEnd == True:
            strHW = self.hiddenWord
            lblHW = "hidden word  :"
        else:
            strHW = " "
            lblHW = "              "
            
        
        
        lblDD = "=============="
        strDD = "========================="
          
        #print("====================================================================================================")
        print(f'=={lblDD}={strDD:<20}====================================================')
        print(f'| {lblGS} {strGS:<20}    | avaliable letters : {self.letters}  ')
        print(f'| {lblHW} {strHW:<20}    | letters guessed   : {self.guesses} ')
        print(f'| {lblDW} {strDW:<20}    | incorrect letters : {self.misses} ')
        print(f'=={lblDD}={strDD:<20}====================================================')
        #print("====================================================================================================")
        
    def printDisplay(self):

        self.printPanel()
        Lib1.twoBlankLines()
        for i in range(6, -1, -1):
            crateNum = i + 1
            self.printCrate(crateNum)
            
        self.printShip()
    

    def printCrate(self, inNum):  
        index1  =   inNum -1 # counting from (0-6)
        char1   =   self.listCrates[index1]
        size1 = len(char1)
        
        if size1 == 0:
            pass
        else:
            print(f'           ********** {char1} **********')
        

    def printShip(self):
        
        myName = "Cargo of the Sea"
        blanks = " "
        if self.flagSink == True:
            ifSink = "Your ship is sinking!"
        else:
            ifSink = " "
        
        print(f'    \- -- --- --- --- --- --- -- --- -- -/')
        print(f'     \      {ifSink:^21}       /')
        print(f'      \     {blanks:^21}      /')
        print(f'       \    {blanks:^21}     /')
        print(f'        \   {myName:^21}    /')
        print(f'         \  {blanks:^21}   /')
        print(f'     \-----------------------------------/')
        print()
        print()

    def game(self):
        
        flagCont = True
        self.initializeGame()
        self.printDisplay()

        while flagCont == True:
            my_prompt = "Please guess a letter"
            my_guess = self.inputStringRange(my_prompt, self.letters)
            self.guesses = self.guesses + my_guess
            self.letters = self.letters.replace(my_guess, "")

            if my_guess in self.hiddenWord: # current guess is correct? 
                self.checkWord(my_guess)
                if self.displayWord.count("*") == 0:
                    self.status = "Great, you won!"
                    self.flagEnd = True
                    self.printDisplay()
                    print()
                    flagCont = self.playAgain()
                    print()
                    print()
                    if flagCont == True:
                        self.initializeGame()
                    # end_if__
                # end_if__
            else:
                self.misses = self.misses + my_guess
                size1 = len(self.misses)
                if size1 > 0 and size1 < 7:
                    self.status = "Continue game. "
                # end_if__
                index1 = size1 - 1
                self.listCrates[index1] = my_guess # replace the * 
                if size1 == 7:
                    self.status = "Sorry, you lost! "
                    self.flagEnd = True
                    self.flagSink = True
                    self.printDisplay()
                    flagCont = self.playAgain()
                    print()
                    print()
                    if flagCont == True:
                        self.initializeGame()
                    # __end_if
                #__end_if
            #__end_if_else
                    
            self.printDisplay()
            
        #__end__While__
    #__end__game()__
            
    def playAgain(self):
        in_prompt = "Do you wish to play another game? (y=yes or n=no)"
        out_value = self.inputStringRange(in_prompt, "yn")

        if out_value == "y":
            return True
        else:
            return False       
    def getHiddenWord(self):

        lenList = len(self.listWords)
        index1 = random.randrange(lenList) 
        self.hiddenWord = self.listWords[index1]

        lenWord = len(self.hiddenWord)
        if lenWord == 4:
            self.displayWord = "****"
        elif lenWord == 5:
            self.displayWord = "*****"
        elif lenWord == 6:
            self.displayWord = "******"

    def replaceChar(self, inChar, inIndex):
        temp1 = self.displayWord
        len1 = len(temp1)
        
        if inIndex == 0:
            self.displayWord = inChar + temp1[1:]
        elif inIndex == (len1 - 1):
            self.displayWord = temp1[:-1] + inChar    
        else:
            plus1 = inIndex + 1
            self.displayWord = temp1[:inIndex] + inChar + temp1[plus1:]
            
    def checkWord(self, inChar):
        size1 = len(self.hiddenWord)

        for i in range(size1):
            chr1 = self.hiddenWord[i]
            if chr1 == inChar: 
                self.replaceChar(chr1, i)  

    def inputStringRange (self, inPrompt = "ERROR", inLetters =""):
        #
        if inPrompt == "ERROR":
            input_prompt = f'ERROR  No input prompt entered (String, length_range = {inLow} to {inHigh}): '
        else:
            input_prompt = f'{inPrompt} (String, length=1): '
        #
        while True:
            try:
                input_str = input(input_prompt)
                input_len = len(input_str)

                # check that the input_len is in the specified range (or default range)
                if input_len == 1:
                    if input_str in inLetters:
                        return input_str

                    else:
                        ErrorMsg = (
                            f'Your input value was not in the list of available letters ({inLetters}).\n' +
                            f'The input value that was entered was (-->value<--):  -->{input_str}<--\n' +
                            f'You will remain in this input loop until you enter a valid String value.\n'
                        )
                        self.printErrorMsg(ErrorMsg)
                        
                else:
                    ErrorMsg = (
                        f'Your input value was not in of specified string length=1. \n' +
                        f'The input value that was entered was (-->value<--):  -->{input_str}<-- \n' +
                        f'You will remain in this input loop until you enter a valid String value.'
                    )
                    self.printErrorMsg(ErrorMsg)
            except:
                ErrorMsg = (
                    f'You have not entered a valid String value.\n' +
                    f'The input value that was entered was (-->value<--):  -->{input_str}<-- \n' +            
                    f'You will remain in this input loop until you enter a valid String value.\n'
                )
                self.printErrorMsg(ErrorMsg)
                
            # end try/except structure
        # end while
 
    def printErrorMsg(self, inErrorMsg):

        Lib1.twoBlankLines()
        print(inErrorMsg)
        Lib1.twoBlankLines()
      
    def readFileName(self):
        list1 = []
        flagOk = False
        self.listWords = []
        
        try:
            inFile = open(self.fileName,"r")
            list1 = inFile.readlines()
            inFile.close()
            #
        except:
            errMsg = f' Error - There was trouble opening your file. '
            self.printErrorMsg(errMsg)

        else:
            
            for line1 in list1:
                str1 = line1.strip() # gets rid of whitespace
                if str1.isalpha() == True and len(str1) >= 4 and len(str1) <= 6:
                    self.listWords.append(str1)
                    flagOk = True
                #__end_if
            #__for__
                
        finally:
            return flagOk
        
 
  



























        

            
   
