'''
Name       : Do Not Sink My Cargo Ship Game
Author     : Torri Baptista
Version    : 1.0
Due Date   : 12/13/2021
Filename   : CargoShip_Class_Rev2.py
'''

import torri_Library1 as Lib1
from Baptista_Linked_List import LinkedList
import random
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

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
        window1 = Tk()
        window1.title("Do not sink my cargo ship." )

        self.canvas1 = Canvas(window1, bg="white", width = 800, height = 600)
        self.canvas1.pack()

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
        self.canvas1.delete("crateBox", "crateText")
        
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
        
        self.canvas1.delete("panel")
        font1 = "Courier 11"
        x1, x2, x3, x4 = 10, 150, 375, 550
        y1, y2, y3, y4 = 500, 520, 540, 560
        #
        self.canvas1.create_text(x1, y1, text = "Game Status", anchor = SW, font = font1, tags = "panel")
        self.canvas1.create_text(x2, y1, text = self.status, anchor = SW, font = font1, tags = "panel")
        #
        if self.flagEnd == True:
            self.canvas1.create_text(x1, y2, text = "Hidden Word", anchor = SW, font = font1, tags = "panel")
            self.canvas1.create_text(x2, y2, text =  self.hiddenWord,  anchor = SW, font = font1, tags = "panel")
            if self.flagSink == True:
                stringOut = "Game Lost"
            else:
                stringOut = "Game Won"
            print(f'\n\n hiddenWord ({self.hiddenWord} is printed in the panel. {stringOut}\n')
        #
        self.canvas1.create_text(x1, y3, text =  "Display Word", anchor = SW, font = font1, tags = "panel")
        self.canvas1.create_text(x2, y3, text =  self.displayWord, anchor = SW, font = font1, tags = "panel")
        #============================ first 3 on the left side ====================
        
        self.canvas1.create_text(x3, y1, text = "Available Letters", anchor = SW, font = font1, tags = "panel")
        self.canvas1.create_text(x4, y1, text = self.letters, anchor = SW, font = font1, tags = "panel")
        #
        self.canvas1.create_text(x3, y2, text = "Letters Guessed", anchor = SW, font = font1, tags = "panel")
        self.canvas1.create_text(x4, y2, text = self.guesses, anchor = SW, font = font1, tags = "panel")
        #
        self.canvas1.create_text(x3, y3, text = "Incorrect Letters", anchor = SW, font = font1, tags = "panel")
        self.canvas1.create_text(x4, y3, text = self.misses, anchor = SW, font = font1, tags = "panel")
        #
        
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
        listColors = ["yellow", "light green", "cyan", "light blue", "pink", "orange", "salmon"]
        
        if size1 == 0:
            pass
        else:
            yy1 = 280 - 38 * index1
            yy2 = yy1 - 38
            xx1 = 100
            xx2 = 500
            self.canvas1.create_rectangle(
                                            xx1, yy1, xx2, yy2, tags = "crateBox",
                                            fill = listColors[index1],
                                            width = 2, outline = "black"

                                        )
        
            self.canvas1.create_text(
                
                                     300, yy1 - 18, text = self.listCrates[index1], 
                                     font = "Courier 18 bold",
                                     tags = "crateText",

                                     )
            print()
    def printShip(self):

        self.canvas1.delete("shipBody", "shipSink", "shipName")
        myName = "Cargo of the Sea"
        blanks = " "
            
        #create a polygon
        self.canvas1.create_polygon (
                                      50, 280, 150, 460,
                                      450, 460, 550, 280,
                        
                                                        tags = "shipBody",     fill = "red",
                                                        width = 2,         outline = "black"
                                    )
        self.canvas1.create_text(
                
                                     300,425, text = "Cargo of Sea",
                                     font = "Times 18 bold",
                                     tags = "shipName"

                                     )
        

        if self.flagSink == True:
            self.canvas1.create_text(
                
                                     300,350, text = "Your ship is sinking!",
                                     font = "Times 18 bold",
                                     tags = "shipSink"

                                    )
            
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
                    print(f'flagSink = {self.flagSink}')
                    print(f'self.misses = {self.misses} and size1 = {size1}')
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
        # in_prompt = "Do you wish to play another game? (y=yes or n=no)"
        # out_value = self.inputStringRange(in_prompt, "yn")
        in_prompt = f'\n\n{"Do you wish to play another game?":60}\n\n'
        dialogTitle = f'{"Continue the game?":60}'
        out_value = tkinter.messagebox.askyesno(dialogTitle, in_prompt)
        msg = f'\n\nPlay again-user entered -->{out_value}<--\n'
        print(msg)
        return out_value
     
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
                # input_str = input(input_prompt)
                dialogTitle = "Get letter from user."
                input_str = tkinter.simpledialog.askstring(dialogTitle, input_prompt)
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

        errorMsg = f'\n\n' + inErrorMsg + f'\n\n'
        print(errorMsg)
        tkinter.messagebox.showerror(f'{"Error Message":90}', errorMsg)
      
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
        
 
  



























        

            
   
