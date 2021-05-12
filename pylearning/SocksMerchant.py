
import os


###make it as set then count how much is in the array

def sockMerchant(n, ar):
    c = 0
    ars = set(ar)
    for i in ars:
        c = c + ar.count(i) // 2
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
