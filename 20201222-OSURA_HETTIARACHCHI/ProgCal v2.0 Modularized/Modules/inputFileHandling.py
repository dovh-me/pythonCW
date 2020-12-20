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
#Please note that I have assigned the read data into an array. So i hope 

#Read file
def read_file():
    file = open("input.txt", "r")
    input_temp = file.readlines()
    file.close()
    return input_temp
#------------------------------------------------------------------------

#Spliting the strings
#I have stored all the inputs inside input.txt and here the data read is
#being added in to an array. 
def splts(list_data:list,data:list,rows:int,cols:int):
    for i in range(rows):
        temp = list_data[i].split()
        for j in range(cols):
            data[i][j] = temp[j]
    return data
#------------------------------------------------------------------------

#Range validation
def validations(data:list):
    #------ type val --------
     
    for j in range(len(data)):
        C = [data[j][0],data[j][1],data[j][2],False]
        for i in range(3):
            try: 
                data[j][i] = int(C[i])
            except:
                print("Inputs are not of the required type.")
                C[3] = False
                break
        else:
            C[3] = True
    #----- range val--------            
        if(C[3]):
            for i in range(3):
                if(data[j][i]%20 != 0 or data[j][i] < 0 or data[j][i] > 120):
                    print("Out of range.")
                    C[3] = False
                    break
                else:
                    C[3] = True
    #----- total val -------
            else:
                if(sum(data[j][:3]) != 120):
                    print("Incorrect Credit total.")
                    C[3] = False
        data[j].append(C[3])
    return data
        
#-------------------------------------------------------------------------

