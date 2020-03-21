def PPRRIINNTT(num,size):
    for i in range(0,size,1):
        temp = num[i]
        if(temp>=0 and temp<=9):
            temp = temp + 48
            print(    chr(temp),end='')
        else:
            temp = temp - 10 + 65
            print(    chr(temp),end='')
    print("-->",end='')

def minuss(num1, num2, n, size):
    num3 = [0]*size
    for i in range(size-1,-1,-1):
        if(num1[i]-num2[i] < 0):
            num3[i] = num1[i] + n - num2[i]
            num1[i-1] = num1[i-1] - 1
        else:
            num3[i] = num1[i]- num2[i]
    return num3

def plus_add(num1,num2,n,size):
    num3 = [0]* size
    for i in range(size-1,-1,-1):
        if(num3[i] + num1[i] + num2[i] >= n):
            num3[i] = num3[i] + num1[i] + num2[i] - n
            num3[i-1] = 1
        else:
            num3[i] = num3[i] + num1[i] + num2[i]
    return num3

def s_o_s_f(num,n,size): # название функции six_one_seven_for
    num1 = [0]*size
    num2 = [0]*size

    for i in range(0,size,1):
        num1[i] = num[i]
        num2[i] = num[i]
    num1.sort(reverse = True)
    num2.sort(reverse = False)
    num3 = minuss(num1, num2, n, size)
    return num3


def Kaprekara(n, size):
    num = [0]*size
    h = [0]*size
    h[size-1] = 1
    k = 1
    flag = 0
    print("n ==",n,"size ==",size)
    for i in range(1,n**size,1):
        num = plus_add(num,h,n,size)

        num1 = s_o_s_f(num,n,size)
        while(num1 != num and k < 10):
            num1 = s_o_s_f(num1,n,size)
            k = k + 1
        if(k < 10):
            flag = 1
            for j in range(1,k + 2,1):
                num1 = s_o_s_f(num1, n, size)
                PPRRIINNTT(num1, size)
            print()
        k = 1
    if(flag == 0):
        print("Ничего нет")



def mmaaiinn_main():
    for n in range(2,11,1): #  n :: система счисления 2 3 4 5 6 7 8 9 10
        for size in range(2,8,1): # size :: разряд числа 2 3 4 5 6 7
            Kaprekara(n,size)

mmaaiinn_main()