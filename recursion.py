##Natural number addition with Recursion
def natural_recursive(n):
    if n==0:
        return 0
    return n + natural_recursive(n-1)
N= natural_recursive(10)
print(N)