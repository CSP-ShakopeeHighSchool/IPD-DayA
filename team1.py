####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Ty' # Only 10 chars displayed.
strategy_name = 'CopyCat until betray twice'
strategy_description = 'How does this strategy decide? idk you tell me'
    




'''
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
=============================================Start of custom code=====================================================
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
#import Collections
import random

my_his = []
their_his = []
my_sco = 0
their_sco = 0
beys = 0
cons = 0
turns = 0
'''
def movie(my_history, their_history, my_score, their_score):
    attack = 'c'

    my_his = my_history
    their_his = my_history
    my_sco = my_score
    their_sco = their_score

    return attack


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv--My Char pattern actions--vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def cc_ME(): # Personal Copy Cat model - - Does what you did last time
    if their_his[-1] == 'c':
        return 'c'
    else:
        return 'b'

def ach_ME(): # Personal Always cheat model - - Always cheats
    return 'b'

def aco_ME():  # Personal Always coop model - - Always coops
    return 'c'

def grudge_ME(): # Personal Grudger model - - ACO until cheat than ACH
    for i in their_his:
        if 'b' in their_his:
            return 'b'
        else:
            return 'c'

def det_ME(): # Personal Detective model - - c,b,c,c, If b, then copy. If c, than ACH
    didbet = False
    for i in their_his:
        if 'b' in their_his:
            didbet = True
    
    if turns == 0:
        return 'c'
    elif turns == 1:
        return 'b'
    elif turns == 2:
        return 'c'
    elif turns == 3:
        return 'c'
    elif didbet == True:
        cc_ME()
    elif didbet == False:
        ach_ME()
    

def ck_ME(): # Personal Copy Kitten model - - ACO until you cheat twice
    bey = 0
    for i in their_his:
        if 'b' in their_his[i]: # Test to see if this works on most recent
            bey += 1
    if bey > 1:
        return 'b'
    else:
        cc_ME()

def simp_ME(): # Personal Simpliton model - - Starts to coop, if you cheat, does oppoisite of last move
    bey = False
    for i in their_his:
        if 'b' in their_his:
            bey = True
    if bey == False:
        return 'c'
    else:
        if their_his[-1] == 'c':
            return 'b'
        else:
            return 'c'


def ran_ME(): # Personal Random model - - 50/50 Random
    if random.randint(0,1) == 1:
        return 'c'
    else:
        return 'b'

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv--Pattern Detection--vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
'''
'''
	2. Try to find patterns
		a. Number patterns
			i. Every other --
			ii. X many times
		b. Reaction patterns
			i. Compare to what I do
			ii. Find if pattern relates to me
		c. Char patterns
			i. Does it follow a Char's move
				1) If not, random
	3. After so many rounds or "confidence" level
		a. Change pattern to exploit
			i. Find pattern and work around it
'''
'''
def numPat_eo_ENI():
    c = 0
    b = 0
    lst = ['c','b','c','c','b','b','c']
    for i in lst: # Check to make sure its in order
        if i == 'c':
            c += 1
        else:
            b += 1
    print(c, ' ', b)

    if  c == b or (c >= b-1 and c <= b+1) or (b >= c-1 and b <= c+1):
        print('Hello')
    else:
        print('Bye')

    return None

switchOffNum = []
switchOfLetter = []

def numPat_pack_ENI():
    '''
'''
    ### Packs switch lists to what the opponent has enteterd
    \n Goes through list by counting in which order does it
    change and appends how long it took
    '''
'''
    countss = 0
    tempC = 0
    tempB =  0
    currentChoice = ''

    lst = ['c','b','c','c','b','b','c']
    

    for i in lst: #Makes list of freq with num & alpha lists
        print('I equals, ', i)
        if currentChoice == '': # If its first or reseted
            if i == 'c':
                tempC += 1
                currentChoice = 'c'
            elif i == 'b':
                tempB += 1
                currentChoice = 'b'
            print(' |On first or reset| ')
        elif i == currentChoice: # Adds to temp till can't
            if currentChoice == 'c':
                tempC += 1
            elif currentChoice == 'b':
                tempB += 1
            print('|Adding to consis alpha| ')
        elif i != currentChoice: # Once let change, append to list and reset 
            if currentChoice == 'c':
                switchOfLetter.append('c')
                switchOffNum.append(tempC)
                tempC = 0
                tempB += 1
                currentChoice = 'b'
            elif currentChoice == 'b':
                switchOfLetter.append('b')
                switchOffNum.append(tempB)
                tempB = 0
                tempC += 1
                currentChoice = 'c'
            #tempB = 0
            #tempC = 0
            #currentChoice = ''
            print(' |Change, reseting list| ')
        print('\n Starting next index \n')
    if tempC > 0: #If theirs a single left then add that
        switchOfLetter.append('c')
        switchOffNum.append(tempC)
    elif tempB > 0:
        switchOfLetter.append('b')
        switchOffNum.append(tempB)
    print(switchOffNum, 'spaceing \n ', switchOfLetter)
                



    return None

def numPat_na_ENI():
    '''
'''
    ### Trys to find basic numeric pattern
    Enter text here
    \n sd
    ### How to write
    check if 
    '''
'''
    ans = ''

    # Every other --------------
    current = 0
    everyotherQ = True
    #blank = 1
    for i in switchOffNum:
        if i == 1:
            everyotherQ = True
        elif i != current:
            everyotherQ = False
            break
    if everyotherQ == True:
        ans = 'EO'
    # End of Every other -------

    # Every so often ------------

    everySoQ = True
    everysoQA = ''
    num = 1
    tempNumList = switchOffNum
    while any in tempNumList:
        while num in tempNumList:
            tempNumList.remove(num)
        num += 1

    # End

    skipping = 1
    currentPlace = switchOffNum[0]
    iPlacer = 1
    for i in switchOffNum:
        if iPlacer == i:
            None
            # True
        else:
            None
            # False
        
import prisoners_dilemma

def ert():
    lst = ['c','b','c','c','b','b','c']
    lst2 = [1,3,5,1,2,3]
    for i in lst:
        for h in lst2:
            print(i, h)
    


'''
#prisoners_dilemma.scores



# numPat_pack_ENI()


'''
////////////////////////////////////////////////////////////////////////////////////////////////////
'''


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    my_his = my_history
    their_his = my_history
    my_sco = my_score
    their_sco = their_score

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    # return 'c'
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    elif 'b' not in their_history and len(their_history)>10:
        return 'b'
        
    else:
        bey = 0
        for i in their_history:
            if i == 'b' : # Test to see if this works on most recent
                bey += 1
        if bey > 1:
            return 'b'
        else:
            if their_history[-1] == 'c':
                return 'c'
            else:
                return 'b'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')