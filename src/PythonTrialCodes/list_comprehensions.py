from collections import Counter
def reverse(string):
    i = len(string)
    
    newString = ""
    while i != 0:
        newString = newString +  string[i-1]
        i = i-1;
    print(newString)
    
reverse("Preeti")
##############################################################################
def rever_in_place(string):
    splitString = string.split(" ")
    print(splitString);
    newString = ""
    
    for str in splitString:
        i = len(str)
        newString = newString + " "
        while i!=0:
            newString = newString +str[i-1]
            i=i-1;
    print(newString)
rever_in_place("Shaunak lives in San Jose")

##############################################################################

def compare(string1 , string2):
    comparison = False
    if Counter(string1) == Counter(string2):
        comparison =True;
        print(comparison);
    else:
        print(comparison)
compare("Shaunak", "Preeti")
compare("Preeti", "Preeti")
    

##############################################################################
def compare3(string1 , string2):
    comparison = False
    i = len(string1);
    j = len(string2);
    if i==j:
        for n in string1:
            if(string1 == string2):
                comparison = True;
           
    print("Third Comparison" , comparison)
    
compare3("Aditi", "Preeti")
compare3("Sharad", "Sharad")
##############################################################################

def compare2(string1 , string2):
    comparison = False
    len1= len(string1)
    print(len1)
    len2= len(string2)
    if len1==len2:
        str1 = set(string1.split(" "))
        print(str1)
        str2 = set(string2.split(" "))
        if(str1==str2):
            comparison = True;
            print("Second Compare",comparison);
        else:
            print("Second Compare",comparison);     
   
compare2("Sharad", "Preeti")
compare2("Preeti", "Preeti")
##############################################################################    