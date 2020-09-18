def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
def isComposite(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
    return False

n=int(input())
string=list(input())
    
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if isPrime(ord(string[j])) and isComposite(ord(string[i])):
            string[i],string[j]=string[j],string[i]
        elif isPrime(ord(string[i])) and isPrime(ord(string[j])):
            if ord(string[j]) < ord(string[i]):
                string[i],string[j]=string[j],string[i]
        elif isComposite(ord(string[j])) and isComposite(ord(string[i])):
            if ord(string[j]) > ord(string[i]):
                string[i],string[j]=string[j],string[i]
string=''.join(string)
string
