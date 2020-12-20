# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student Name: Don Osura Visnaka Hettiarachchi
# Student ID: 20201222        
  
# Date:  19/11/2020
# coding: utf-8
"""
|*******************************|
|                               |
|Don Osura Visnaka Hettiarachchi|
|20201222  w1810807             |
|                               |
|*******************************|

"""
pass_credits = 0
defer_credits = 0
fail_credits = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
PC = DC = FC = 0



#Read file
def read_file():
    file = open("input.txt", "r")
    input_temp = file.readlines()
    file.close()
    return input_temp
#------------------------------------------------------------------------


#Spliting the strings
#I have stored all the inputs inside input.txt and here the data read is
#being added in to am array 
def splts():
    global list_data, data, cols, rows
    for i in range(rows):
        temp = list_data[i].split()
        for j in range(cols):
            data[i][j] = temp[j]
#------------------------------------------------------------------------
            

#Range validation
def validations(A=[0,0,0]):
#------ tye val --------
    C = [0,0,0,False]
    for i in range(3):
        try: 
            C[i] = int(A[i])
        except ValueError:
            print("Inputs are not of the required type")
            C[3] = False
            break
    else:
        C[3] = True
#----- range val--------            
    if(C[3]):
        for i in range(3):
            if(C[i]%20 != 0 or C[i] < 0 or C[i] > 120):
                print("Out of range. ")
                C[3] = False
                break
            else:
                C[3] = True
#----- total val -------
        else:
            if(sum(C[:3]) != 120):
                print("Incorrect Credit total.")
                C[3] = False

    return C
        
#-------------------------------------------------------------------------


#Printing the progression outcome
def prog_outcome():
    global pass_credits, defer_credits, fail_credits, progress, retriever, trailer, exclude
    cont = validations([pass_credits, defer_credits, fail_credits])
    if(cont[3]):
        if(cont[0] >= 100):
            if(cont[1] == 20 or cont[2] == 20):
                print("Progress (module trailer)")
                trailer += 1
            else:
                print("Progress")
                progress += 1
        else:
            if(cont[2] >= 80):
                print("Exclude")
                exclude += 1
            else:
                print("Do not progress - module retriever")
                retriever += 1
#-------------------------------------------------------------------------


#Histogram data
def hist_dat(x):
    i = 1
    dat = ""
    while(x >= i):
        dat = dat + "*"
        i += 1
    return dat
#------------------------------------------------------------------------


#Histogram borders
def hist_border():
    print("-"*80)

#------------------------------------------------------------------------



#Calling prog_outcome function for each input line
def calc_outcome():
    global data, pass_credits, defer_credits, fail_credits
    for i in range(len(data)):
        pass_credits = data[i][0]
        defer_credits = data[i][1]
        fail_credits = data[i][2]

        prog_outcome()
#------------------------------------------------------------------------

list_data = read_file()


#2-D array for storing input data
rows = len(list_data)
cols = 3
data = [[0 for y in range(cols)] for x in range(rows)]


splts()
calc_outcome()
        
#Histogram print
hist_border()
print(":HISTOGRAM:\n")
prgrs_prnt = hist_dat(progress)
print("Progress   " , progress, ":  " + prgrs_prnt)
trl_prnt = hist_dat(trailer)
print("Trailer    " , trailer, ":  " + trl_prnt)
rtrvr_prnt = hist_dat(retriever)
print("Retriever  " , retriever, ":  " + rtrvr_prnt)
xcld_prnt = hist_dat(exclude)
print("Exclude    " , exclude, ":  " + xcld_prnt + "\n")
print(progress + trailer + retriever + exclude, "outcomes in total")
hist_border()    



