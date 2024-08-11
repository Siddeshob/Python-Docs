# from start import chai


# sq={x:x**2 for x in range(6)}

# chai("imtd")
# tea=['t1','t2','t3']
# for t in tea:
#     if t in 't2':
#         print('true')
#-----------------------------------------------
# li=[int(input("enter all ages"))]
# child=[]
# teen=[]
# adult=[]
# for i in li:
#     if i<13:
#         child.append(i)
#     elif i>=13 and i<=19:
#         teen.append(i)
#     elif i>20:
#         adult.append(i)
# print("child = " + str(child))
# print("teen = " + str(teen))
# print("adult = " + str(adult))
#---------------------------------------------------
# age=12
# day='w'
# price=12 if age>=18 else 8
# print(price)
# if day=='w':
#     price=price-2
# print(price)
#--------------------------------------------------
# res=int(input('enter score : '))
# if res >=90 and res<=100:
#     print('a')
# elif res >=80 and res<=89:
#     print('b')
# elif  res >100:
#     print('invalid')
#     exit
        
# print("---end---")
#--------------------------------------------
# dist=int(input("enter the distance : "))
# if dist<=3:
#     print('walk')
# elif dist>=3 and dist<=5:
#     print('bike')
# else:print("car")
#-------------------------------------------------
# express=True
# while(express):
#     typeC=input('select S or L')
#     CE=input('expresso Y or N')
#     print('u r order is: '+typeC+" extra Expresso: "+CE)
#     again=input('order again Y or N')
#     if again.lower()=='n':
#         express=False
#         print('loop end')
#---------------------------------------------------
# list=[1,2,3,5,-5,-8]
# li2=[]
# li3=[]
# for i in list:
#     if(i>0):
#         li2.append(i)
#     else: li3.append(i)
# print(li2)
# print(li3)
#-----------------------------------------
# n=10
# count=0
# for i in range(0,n+1):
#     if i==5:
#         continue
#     if i%2==0:
#         print(i)
#----------------------------------------------
# num=2
# for i in range(1,11):
#     if i==5:
#         continue
#     print(num,'x',i,'=',num*i)
#-------------------------------------------- 
# name="siddu"
# rev=''
# for i in name:
#     rev=i+rev #s,is,dis,ddis,eddis,ueddis
# print(rev)

# for i in name:
#     print('-',i)
#     if name.count(i)==1:
#         print(i)
#         break

# n=3
# ans=1
# while n>=1:
#     ans=ans*n
#     n=n-1
# print(ans)
#_-------------------------------------------------------
# while True:
#     n=int(input("enter num b/w 1-10 -exit theloop enter *99* "))
#     if n>=1 and n<=10:
#         print(n,' is valid')
#     elif n==99:
#         break
#     else:
#         print(n,' is not valid')
#-----------------------------------------------
# n=3
# count=0
# for i in range(2,n):
#     if (n%i)==0:
#         print('not prime')
#         break
#     else:
#         print(' prime')


# li=['a','b','c','c','d','d','f']
# l2=set()
# for i in li:
#     if li.count(i)>1:
#         l2.add(i)
# print(l2)
#-----------------------------------------------------
# import time

# w_time=1
# attempts=1  
# max_retrives=5

# while attempts<=max_retrives:
#     print('attempts ',attempts,'witing-time',w_time)
#     time.sleep(w_time)
#     w_time*=2
#     attempts+=1
#---------------------------------------------------------
# import math

# def length(n):
#     cir=math.pi*n
#     sqr=n*n+1
#     return int(cir),sqr

# a,b=length(2)
# print(a,b)
#------------------------------------------------
# def name(n='obs'):
#     print(n)

# name()
#------------------------------------------
# cu=lambda x:x+1
# print(cu(99))
#------------------------------------------
def cube(*args):
    return sum(args)

print(cube(1,2,3,4,5))
print(cube(1,4,5))
print(cube(1,2,3))