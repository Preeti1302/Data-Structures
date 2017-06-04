from array import array
def remDups():
    array1 = [-6, -12,7,-6, 0, 2,8,3, 3, 6,2]
    
    array2 = [];
    for i in array1:
        if i not in array2:
            array2.append(i);
    array2.sort();
    print(array2)
    
remDups();