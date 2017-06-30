def fibonacci(x):
    if x == 0:
        return 0;
    elif x == 1:
        return 1;
    else:
        return fibonacci(x-2)+fibonacci(x-1);
    

n = 10    
for a in range(n):
    print(fibonacci(a))