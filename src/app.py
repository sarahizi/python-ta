import sys
import os


def prime(s):
    # your code goes here
    if int(s)>1:
        for i in range(2, int(int(s)/2)+1):
            if (int(s) % i)==0:
                print(s, 'is not a prime number')
                break
                
        else:
            print(s, 'is a prime number')
    else:
        print(s, 'is not a prime number')

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
