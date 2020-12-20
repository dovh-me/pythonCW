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


#Range validation-----------------------------------------------------------
def rng(C):
    if(C%20 != 0 or C < 0 or C > 120):
        print("Out of range")
        return False
    else:
        return True
#---------------------------------------------------------------------------


#Getting inputs and validations---------------------------------------------               
def inputs():
    while(True):
        '''ValueError handling'''
        while(True):
            try:
                PC = int(input("\nPlease enter your credits at pass: "))
                x = rng(PC)
                if(x):
                    break
            except:
                print('Integer required')
        while(True):
            try:
                DC = int(input("Please enter your credits at defer: "))
                x = rng(DC)
                if(x):
                    break
            except:
                print('Integer required')
        while(True):
            try:
                FC = int(input("Please enter your credits at fail: "))
                x = rng(FC)
                if(x):
                    break
            except:
                print('Integer required')
            
            '''Total validation'''
        if(PC + DC + FC != 120):
            print("Total incorrect")
            continue
        else:
            break
    return [PC,DC,FC]
#---------------------------------------------------------------------------
