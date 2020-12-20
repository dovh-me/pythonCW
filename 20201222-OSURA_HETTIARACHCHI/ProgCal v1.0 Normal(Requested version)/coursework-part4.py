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
progress = 0
trailer = 0
retriever = 0
exclude = 0
cont = 'y'
#Range validation
def rng(C):
    if(C%20 != 0 or C < 0 or C > 120):
        print("Out of range")
        return 0
    else:
        return 1
#-------------------------------------------------------------------------

#Getting inputs and validations                
def inputs():
    global pass_credits, defer_credits, fail_credits
    err = 1
    
    '''ValueError handling'''
    while(err > 0):
        err = 0
        try:
            PC = int(input("\nPlease enter your credits at pass: "))
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
            continue
        
        '''Total validation'''
        if(PC + DC + FC != 120):
            print("Total incorrect")
            err += 1
        else:
            pass_credits = PC
            defer_credits = DC
            fail_credits = FC
#-------------------------------------------------------------------------

#Printing the progression outcome
def prog_outcome():
    global pass_credits, defer_credits, fail_credits, progress, retriever, trailer, exclude
    if(pass_credits >= 100):
        if(fail_credits == 20 or defer_credits == 20):
            print("Progress (module trailer)")
            trailer += 1
        else:
            print("Progress")
            progress += 1
    else:
        if(fail_credits >= 80):
            print("Exclude")
            exclude += 1
        else:
            print("Do not progress - module retriever")
            retriever += 1
#-------------------------------------------------------------------------
#calling functions
while(cont == 'y'):
    inputs()
    prog_outcome()
    cont2 = ' '
    while(cont2 != 'y' or cont2 != 'q'):
        cont2 = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
        if(cont2 == 'y' or cont2 == 'q'):
            cont = cont2
            break
        else:
            print("Please enter a valid input\n")
    
#Histogram borders
def hist_border():
    i = 0
    while(i < 80):
        print("-", end="")
        i += 1
    else:
        print("", end="\n");



#Histogram - number of lines to print
def find_max():
    global progress, trailer, retriever, exclude
    crdts = [progress, trailer, retriever, exclude]
    m = 0
    for i in range(4):
        if crdts[i] > m:
            m = crdts[i]
    return m
#Histogram print   
hist_border()
max_hist = find_max() #to find the number of lines that must be printed
print("Vertical Histogram\n")
print("Progress   Trailing   Retriever   Excluded")
i = 0
while(i <= max_hist):
    if(progress > 0):
        prgrs_prnt = "*"
        progress -= 1
    else:
        prgrs_prnt = " "
    if(trailer > 0):
        trlr_prnt = "*"
        trailer -= 1
    else:
        trlr_prnt = " "
    if(retriever > 0 ):
        rtrvr_prnt = "*"
        retriever -= 1
    else:
        rtrvr_prnt = " "
    if(exclude > 0):
        xclud_prnt = "*"
        exclude -= 1
    else:
        xclud_prnt = " "
    i += 1

    print("   " + prgrs_prnt + "           " + trlr_prnt + "          " + rtrvr_prnt + "           " + xclud_prnt)
hist_border()
