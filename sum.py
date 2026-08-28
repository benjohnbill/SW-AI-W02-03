def sum(n):
    total = 0
    i = 0
    while i <= n :
        total += i
        i += 1
    return total

# sum(3) = 0 + 1 + 2 + 3 = 4

def recursion_sum(n):
    if n == 0:
        return 0
    return n + recursion_sum(n-1)

# sum(3)
# = 3 + recursion_sum(2)
# = 3 + (2 + recursion_sum(1))
# = 3 + (2 + (1 + recursion_sum(0)))
# = 3 + (2 + (1 + 0))

def tail_recursion_sum(n, buffer=0):
    if n == 0:
        return buffer
    return tail_recursion_sum(n-1, n+buffer)

# sum(3)
# = tail_recursion_sum(3, 0)
# = tail_recursion_sum(2, 3)
# = tail_recursion_sum(1, 5)
# = tail_recursion_sum(0, 6)
# = 6
