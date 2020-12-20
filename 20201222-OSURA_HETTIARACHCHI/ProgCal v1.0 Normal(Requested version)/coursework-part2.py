# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student Name: Don Osura Visnaka Hettiarachchi
# Student ID: 20201222        
  
# Date:  19/11/2020
"""
 _______________________________
|                               |
|Don Osura Visnaka Hettiarachchi|
|20201222  w1810807             |
|_______________________________|

"""

pass_credits = 0
defer_credits = 0
fail_credits = 0

#Range validation(divisbles by 20 and in range of 0 and 120)
def rng(C):
    if(C%20 != 0 or C < 0 or C > 120):
        print("Out of range")
        return 0
    else:
        return 1
#-------------------------------------------------------------------------

#Getting inputs and validations(rng function is used for validations)                
def inputs():
    global pass_credits, defer_credits, fail_credits
    err = 1
    
    '''ValueError handling'''
    while(err > 0):
        err = 0
        try:
            PC = int(input("Please enter your credits at pass: "))
            x = rng(PC)
            if(x == 0):
                err += 1
                continue
            else:
                DC = int(input("Please enter your credits at defer: "))
                x = rng(DC)
                if(x == 0):
                    err += 1
                    continue
                else:
                    FC = int(input("Please enter your credits at fail: "))
                    x = rng(FC)
                    if(x == 0):
                        err += 1
                        continue

        except ValueError:
            print('Integer required')
            err += 1
            
        '''Total validation'''
        if(PC + DC + FC != 120):
            print("Total incorrect")
            err += 1
        else:
            pass_credits = PC
            defer_credits = DC #Global variables are updated
            fail_credits = FC
#-------------------------------------------------------------------------

#Printing the progression outcome
def prog_outcome():
    global pass_credits, defer_credits, fail_credits
    if(pass_credits >= 100):
        if(fail_credits == 20 or defer_credits == 20):
            print("Progress (module trailer)")
        else:
            print("Progress")
    else:
        if(fail_credits >= 80):
            print("Exclude")
        else:
            print("Do not progress - module retriever")
#-------------------------------------------------------------------------

inputs()
prog_outcome()
