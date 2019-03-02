import sys
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def div(n):
    res=10/n
    return res
def main(n):
    res=fact(n)
    print(res)
    res1=div(n)
    print(res1)
if __name__=='_main_':
    if len(sys.argv)>1:
        main(int(sys.argv[1]))


