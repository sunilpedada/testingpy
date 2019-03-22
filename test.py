import sys
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def div(n):
    g=n/2
    return g
def ex(n):
    print(fact(n))
    print(div(n))
if __name__=="__main__":
    ex(int(sys.argv[1]))