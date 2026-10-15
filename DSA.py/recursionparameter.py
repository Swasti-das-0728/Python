
x=15
N = 4
def para(x,N):

    if N == 0:
        return
    print(x)
    para(x,N-1)
para(x,N)