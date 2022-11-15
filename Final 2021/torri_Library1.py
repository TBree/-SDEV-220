'''
Torri Baptista
Library
Has Data
'''


def twoBlankLines():
    print()
    print()

def printHeader(inHeader = "empty"):
    twoBlankLines()
    print(inHeader) # this passesthe header to the other file
    twoBlankLines()

def printTitle(inTitle = "empty"):
    print()
    print(inTitle)
    print()

def printError3(s1 = "empty", s2 = "empty", s3 = "empty"):
    print()
    print(s1)
    print(s2)
    print(s3)
    print()

    
def inputIntegerRange ( inPrompt = "ERROR", inLow = -999999999, inHigh=999999999 ):
    #
    if inPrompt == "ERROR":
        input_prompt = f'ERROR  No input prompt entered (Integer, range = {inLow} to {inHigh}): '
    else:
        input_prompt = f'{inPrompt} (Integer, range = {inLow} to {inHigh}): '
    #
    while True:
        try:
            input_str = input(input_prompt)
            input_int = int(input_str)

            # check that the input_int is in the specified range (or default range)
            if input_int >= inLow and input_int <= inHigh:
                return input_int
            else:
                printError3(
                    f'Your input value was not in the specified range from {inLow} to {inHigh}.',
                    f'The input value that was entered was (-->value<--):  -->{input_str}<--',
                    f'You will remain in this input loop until you enter a valid Integer value.'
                )
        except:
            printError3(
                f'You have not entered a valid integer value.',
                f'The input value that was entered was (-->value<--):  -->{input_str}<--',            
                f'You will remain in this input loop until you enter a valid Integer value.'
            )
        # end try/except structure
    # end while
#======================================
def inputStringRange ( inPrompt = "ERROR", inLow = 1, inHigh=999 ):
    #
    if inPrompt == "ERROR":
        input_prompt = f'ERROR  No input prompt entered (String, length_range = {inLow} to {inHigh}): '
    else:
        input_prompt = f'{inPrompt} (String, length_range = {inLow} to {inHigh}): '
    #
    while True:
        try:
            input_str = input(input_prompt)
            input_len = len(input_str)

            # check that the input_len is in the specified range (or default range)
            if input_len >= inLow and input_len <= inHigh:
                return input_str
            else:
                printError3(
                    f'Your input value was not in the specified String length range from {inLow} to {inHigh}.',
                    f'The input value that was entered was (-->value<--):  -->{input_str}<--',
                    f'You will remain in this input loop until you enter a valid String value.'
                )
        except:
            printError3(
                f'You have not entered a valid String value.',
                f'The input value that was entered was (-->value<--):  -->{input_str}<--',            
                f'You will remain in this input loop until you enter a valid String value.'
            )
        # end try/except structure
    # end while
#======================================
def inputFloatRange ( inPrompt = "ERROR", inLow = -999999999.999, inHigh=999999999.999 ):
    #
    if inPrompt == "ERROR":
        input_prompt = f'ERROR  No input prompt entered (Float,range={inLow}-{inHigh}): '
    else:
        input_prompt = f'{inPrompt} (Float,range={inLow}-{inHigh}): '
    #
    while True:
        try:
            input_str = input(input_prompt)
            input_flt = float(input_str)

            # check that the input_flt is in the specified range (or default range)
            if input_flt >= inLow and input_flt <= inHigh:
                return input_flt
            else:
                print()
                
                print(f'Your input value was not in the specified range from {inLow} to {inHigh}.')
                print(f'The input value that was entered was (-->value<--):  -->{input_str}<--')
                print(f'You will remain in this input loop until you enter a valid Float value.')

                print()
        
        except:
            print()
            
            print(f'You have not entered a valid integer value.')
            print(f'The input value that was entered was (-->value<--):  -->{input_str}<--')            
            print(f'You will remain in this input loop until you enter a valid Float value.')

            print()
    
        # end try/except structure
    # end while
#=========================================
    
