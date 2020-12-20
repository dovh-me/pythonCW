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
import Modules.inputFileHandling

#Printing the progression outcome
def prog_outcome_staff(validated:list):
    progress = trailer = retriever = exclude = 0
    if(validated[0] >= 100):
        if(validated[1] == 20 or validated[2] == 20):
            print("Progress (module trailer)")
            trailer += 1
        else:
            print("Progress")
            progress += 1
    else:
        if(validated[2] >= 80):
            print("Exclude")
            exclude += 1
        else:
            print("Do not progress - module retriever")
            retriever += 1
    return [progress, trailer, retriever, exclude]
#-------------------------------------------------------------------------
##--StudentVerison.prog_outcome()
#this function is used for the 1st part only since it doesn't require any validations
def prog_outcome_student(pass_credits, defer_credits, fail_credits):
    if(pass_credits >= 100):
        if(fail_credits == 20 or defer_credits == 20):
            print("Progress (module trailer)")
        else:
            print("Progress")
    else:
        if(fail_credits >= 80):
            print("Exclude")
        else:
            print("Do not progress – module retriever")

##-------------------------------
#Calling prog_outcome function for each input line
#(Used only in the Alternative Staff Version[File input])
def calc_outcome(data:list):
    input_val = Modules.inputFileHandling.validations(data)
    hist_data = [0,0,0,0]
    for i in range(len(data)):
        if(data[i][3]):
            hist_data_temp = prog_outcome_staff(input_val[i])
            for j in range(4):
                hist_data[j] += hist_data_temp[j]
    else:
        return hist_data
#------------------------------------------------------------------------
