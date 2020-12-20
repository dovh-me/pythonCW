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
import time
import Modules.calculations
import Modules.validations
import Modules.histograms
import Modules.header
import Modules.inputFileHandling

option = ''
inputs = ['1','2','3','4','5','q']
Modules.header.header_prnt()
print("_"*100 + "\n")
while(option != 'q'):
    Modules.header.intro()
    while(True):
        print("_"*100)
        option = input("\tChoose the Version you want to run from the given option: ").lower()
        if(option in inputs):
            break
        else:
            print("\tPlease enter a number relevent to a given option.\n")
    if(option == '1'):
        #SutdentVersion-------------------------------------
        pass_credits = int(input("Please enter your credits at pass: "))
        defer_credits = int(input("Please enter your credits at defer: "))
        fail_credits = int(input("Please enter your credits at fail: "))
        Modules.calculations.prog_outcome_student(pass_credits, defer_credits, fail_credits)
        ##---------------------------------------------------
    elif(option == '2'):
        #StaffVersion---------------------------------------
        temp = Modules.validations.inputs()
        Modules.calculations.prog_outcome_student(temp[0],temp[1],temp[2])
        ##--------------------------------------------------
    elif(option == '3'):
        #StaffVersion-extended(Horizontal Histogram)--------
        loop = 'y'
        hist_dat = [0,0,0,0]
        while(loop == 'y'):
            temp = Modules.validations.inputs()
            hist_dat_temp = Modules.calculations.prog_outcome_staff(temp)
            for i in range(4):
                hist_dat[i] += hist_dat_temp[i] #adding progress type of each set of inputs
            loop = ''
            while(loop != 'y' or loop != 'q'):
                loop = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
                if(loop == 'y' or loop == 'q'):
                    break
                else:
                    print("Please enter a valid input")

        Modules.histograms.hist_horizontal(hist_dat)
        ##--------------------------------------------------
    elif(option == '4'):
        #StaffVersion-extended(Vertical Histogram)----------
        loop = 'y'
        hist_dat = [0,0,0,0]
        while(loop == 'y'):
            temp = Modules.validations.inputs()
            hist_dat_temp = Modules.calculations.prog_outcome_staff(temp)
            for i in range(4):
                hist_dat[i] += hist_dat_temp[i] #adding progress type of each set of inputs
            loop = ' '
            while(loop != 'y' and loop != 'q'):
                loop_temp = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
                if(loop_temp == 'y' or loop_temp == 'q'):
                    loop = loop_temp
                else:
                    print("Please enter a valid input\n")

        Modules.histograms.hist_vertical(hist_dat)
        ##--------------------------------------------------
    elif(option == '5'):
        #StaffVersion-AlternateStaffVersion(File input)-----

        list_data = Modules.inputFileHandling.read_file()


        #2-D array for storing input data
        rows = len(list_data)
        cols = 3
        data = [[0 for y in range(cols)] for x in range(rows)]


        data = Modules.inputFileHandling.splts(list_data,data,rows,cols)

        hist_data = Modules.calculations.calc_outcome(data)
        Modules.histograms.hist_horizontal(hist_data)
        ##--------------------------------------------------
    else:
        print("Thank you for using PROGCAL")
        print("~</DOVH>~")
        time.sleep(1)
