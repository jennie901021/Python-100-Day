#找出10000以内的完美数
import math
for num in range(1,10000):
    result = 0
    for factor in range(1,int(math.sqrt(num))+1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num// factor != factor:
                result += num//factor
            if result == num:
                print(num)

#生成非波那契數列的前20個數
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

for i in range(20):
    print(Fibonacci(i))