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

#Histogram data (Creating the string to print '*')
def hist_dat(x):
    dat = "*" * x
    return dat
#Histogram borders
def hist_border():
    i = 0
    while(i < 80):
        print("-", end="")
        i += 1
    else:
        print("", end="\n");

#Horizontal Histogram print
def hist_horizontal(data = [0,0,0,0]):
    ax_hist = find_max(data)
    progress = data[0]
    trailer = data[1]
    retriever = data[2]
    exclude = data[3]
    hist_border()
    print("Horizontal Histogram\n")
    prgrs_prnt = hist_dat(progress)
    print("Progress " , progress, "  :  " + prgrs_prnt)
    trl_prnt = hist_dat(trailer)
    print("Trailer " , trailer, "   :  " + trl_prnt)
    rtrvr_prnt = hist_dat(retriever)
    print("Retriever " , retriever, " :  " + rtrvr_prnt)
    xcld_prnt = hist_dat(exclude)
    print("Exclude" , exclude, "    :  " + xcld_prnt)
    print("\n",sum(data), "outcomes in total")
    hist_border()

#Vertical Histogram -----------------------------------------------------
#Histogram - number of lines to print
def find_max(crdts):

    m = 0
    for i in range(4):
        if crdts[i] > m:
            m = crdts[i]
    return m
#printing the vertical histogram
def hist_vertical(data = [0,0,0,0]):
    max_hist = find_max(data)
    progress = data[0]
    trailer = data[1]
    retriever = data[2]
    exclude = data[3]
    hist_border()
    print("Vertical Histogram\n")
    print("| Progress "+str(progress)+" | Trailing "+str(trailer)+" | Retriever "+str(retriever)+" | Excluded "+str(exclude)+" |")
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

        print("     " + prgrs_prnt + "            " + trlr_prnt + "             " + rtrvr_prnt + "            " + xclud_prnt)
    print(sum(data), "outcomes in total")
    hist_border()
