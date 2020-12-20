#ref : https://stackoverflow.com/questions/6357361/alternative-to-execfile-in-python-3
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student Name: Don Osura Visnaka Hettiarachchi
# Student ID: 20201222        
  
# Date:  19/11/2020
import time

option = ''
inpts = ['1','2','3','4','5','q']
print("="*101)
print("|   _ _ _ _ _    _ _ _ _ _    _ _ _ _ _     _ _ _ _ _   _ _ _ _ _        _         _                |")
print("|   \         \  \         \  \   _ _   \  \   _ _ _ _\ \    _ _ \      \  \      \  \              |")
print("|    \    _ _ _\  \    _   _\  \  \   \  \  \  \   _ _   \  \   \_\     \    \     \  \             |")
print("|     \   \        \   \\  \     \  \   \  \  \  \  \_  \  \  \    _     \      \    \  \            |")
print("|      \   \        \   \ \  \   \  \_ _\  \  \  \_ _\  \  \  \_ _\ \   \    _   \   \  \_ _ _ _    |")
print("|       \_ _\        \_ _\  \ _\  \ _ _ _ _ \  \ _ _ _ _ \  \_ _ _ _ \  \ _ \  \ _ \  \_ _ _ _ _\   |")
print("="*101)
print("\n")
print("_"*100 + "\n")
while(option != 'q'):
    print("\t" + "="*89)
    print("\t|\t\t\tStudentVersion                          : [1]\t\t\t|")
    print("\t|\t\t\tStudent Version (Validation)            : [2]\t\t\t|")
    print("\t|\t\t\tStaff Version with Horizontal Histogram : [3]\t\t\t|")
    print("\t|\t\t\tStaff Version with Vertical Histogram   : [4]\t\t\t|")
    print("\t|\t\t\tAlternative Staff Version (File Input)  : [5]\t\t\t|")
    print("\t|\t\t\tQuit PROGCAL                            : [q]\t\t\t|")
    print("\t" + "="*89)
    while(True):
        print("_"*100)
        option = input("\tChoose the Version you want to run from the given option: ").lower()
        if(option in inpts):
            break
        else:
            print("\tPlease enter a number relevent to a given option.\n")
    if(option == '1'):
        #SutdentVersion-------------------------------------
        exec(open('coursework-part1.py').read())
        ##---------------------------------------------------
    elif(option == '2'):
        #StaffVersion---------------------------------------
        exec(open('coursework-part2.py').read())
        ##--------------------------------------------------
    elif(option == '3'):
        #StaffVersion-extended(Horizontal Histogram)--------
        exec(open('coursework-part3.py').read())
        ##--------------------------------------------------
    elif(option == '4'):
        #StaffVersion-extended(Vertical Histogram)----------
        exec(open('coursework-part4.py').read())
        ##--------------------------------------------------
    elif(option == '5'):
        #StaffVersion-AlternateStaffVersion(File input)-----
        exec(open('coursework-part5.py').read())
        ##--------------------------------------------------
    else:
        print("Thank you for using PROGCAL")
        print("~</DOVH>~")
        time.sleep(1)
        break
