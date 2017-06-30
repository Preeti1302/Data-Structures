from _collections import deque
 
def pal_checker(newString):
    char_queue = deque();
     
    for char in newString:
        char_queue.append(char);
         
    still_live = True;
     
    while char_queue.__len__() > 1 and still_live :
        firstVar = char_queue.popleft();
        secondVar = char_queue.pop();
        if(firstVar != secondVar):
            still_live = False;
     
    return still_live;
 
x = input("Enter the String you want to Search:");
 
print(pal_checker("x"));

##############################################################################

def check_anagram(str1 , str2):
       
    str1list = sorted(str1)   
    print(str1list)      
    str2List = sorted(str2)          
            
    i = 0;
    anagrams = False;
    while i < len(str1):
        if (str1list[i] == str2List[i]):
            i=i+1
            anagrams = True;
    print("Anagrams" , anagrams);
           
check_anagram("preeti", "iterp")