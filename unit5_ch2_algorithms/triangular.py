# Tn = n + (n-1) + (n-2) + .. + 3 + 2 + 1

def tri(n):
    if n > 1:
        return n + tri(n-1)
    else:
        return 1



print(tri(4))
print(tri(1))
print(tri(0))