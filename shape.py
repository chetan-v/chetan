n = int(input("Enter number: "))
sum = 0
order =0
m = n
p=n
while(n):
    d=n%10
    order+=1
    n=n//10

while (m):
    digit = m % 10
    sum = sum+digit**order
    m = m//10
if sum == p:
    print("Armstrong")
else:
    print("Not a Armstrong Number")
