from matplotlib import pyplot as plt
from sympy import Symbol, solve, N

time = 0

print('화학 반응식은 aA+bB <=> cC +dD 입니다')
print('반응 계수를 입력해주세요(없는 반응물/생성물은 0)')
a = 1
b = 1
c = 1
d = 1

print('평형 상수를 입력해주세요')
k = 4

print('추가할 반응물/생성물의 몰 농도를 입력해주세요')
A = 3
B = 2
C = 0
D = 0

q = (C**c*D**d)/(A**a*B**b)
x = Symbol('x')
equation = x
rx = 0

if q>k:
        equation = (((C-c*x)**c)*((D-d*x)**d)/((A+a*x)**a)*((B+b*x)**b)-k)
if q<k:
        equation = (((C+c*x)**c)*((D+d*x)**d)/((A-a*x)**a)*((B-b*x)**b)-k)

for r in solve(equation, rational=True, positive=True):
        rx = r
print(rx)
plt.xlabel('a')
plt.ylabel('b')

xArr = [[],[],[],[]]
yArr = [[],[],[],[]]

elArr = [A, B, C, D]
nArr = [a, b, c, d]

for i in range(4):
        dtime = time
        for t in range(1,11):
                dtime += t
                
                xArr[i].append(dtime)
                
                if q<k:
                        if i>=2:
                                yArr[i].append(elArr[i]+nArr[i]*t*(rx/10))
                        else:
                                yArr[i].append(elArr[i]-nArr[i]*t*(rx/10))
                if q>k:
                        if i>=2:
                                yArr[i].append(elArr[i]-nArr[i]*t*(rx/10))
                        else:
                                yArr[i].append(elArr[i]+nArr[i]*t*(rx/10))      
time = dtime

plt.plot(xArr[0], yArr[0])
plt.plot(xArr[1], yArr[1])
plt.plot(xArr[2], yArr[2])
plt.plot(xArr[3], yArr[3])
plt.show()