print("Welcome to our restaurant")
n= input("Enter a list of items seprate by ',': ").split(",")
print(n)
b=n.copy()
# method one
c= n.copy()
c.reverse()
print("Reversal method",c)
# method 2
listl = n
p=listl[::-1]
print("Slicing method",p)
# method 3
# z=-1
# a=0
# print(b[-3])
# while b[a]!=b[z]:
for i in range(len(b)//2):
    b[len(b)-i-1], b[i] = b[i], b[len(b)-i-1]
    # a+=1
    # z=len(b)-a-1
    # print(a,z,b)
    # break
print("Third reversal",b)
if c==p and c==b:
    print("All three method give the same result")
else:
    print("All methods give Different results")
# print(list.append(n))