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
#No validations are done in this part
pass_credits = int(input("Please enter your credits at pass: "))
defer_credits = int(input("Please enter your credits at defer: "))
fail_credits = int(input("Please enter your credits at fail: "))

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

