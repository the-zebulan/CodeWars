def collatz(n):
    result = [str(n)]
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        result.append(str(n))
    return '->'.join(result)

assert collatz(4) == '4->2->1'
assert collatz(3) == '3->10->5->16->8->4->2->1'
