def is_primo(n):
    for i in range(2, n//2):
#        print(i)
        if n%i == 0:
            return False
    
    return True

def define_primo_proximo(n):
    while True:
        if is_primo(n) == True:
            return n
        n = n + 1