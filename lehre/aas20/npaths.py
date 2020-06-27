from pprint import pprint

def compute_N(upper_bound=5):
    N = [[1] * (upper_bound+1) for _ in range(upper_bound+1)]
    for i in range(1, upper_bound+1):
        for j in range(1, upper_bound+1):
            N[i][j] = N[i-1][j-1] + N[i-1][j] + N[i][j-1]
    return N


def all_cigars(m,n):
    if m == 0:
        yield ['I'] * n
    elif n == 0:
        yield ['D'] * m
    else:
        for c in all_cigars(m-1,n-1):
            yield c + ['M']
        for c in all_cigars(m-1, n):
            yield c + ['D']
        for c in all_cigars(m, n-1):
            yield c + ['I']
    


for c in all_cigars(2,2):
    print("".join(c))
    
N = compute_N(5)
pprint(N)
