n=int(input("enter the number of monkeys"))
k=int(input("enter the number of eatable banana"))
j=int(input("enter the number of eatable peanut"))
m=int(input("enter the number of banana"))
p=int(input("enter the number of peanut"))
if k==0 or j==0:
  print(":it is invalid")
else:
  n=n-(m//k+p//j)
  if m%k!=0 or p%j!=0:
    n-n-1
  print("number of monkeys in the tree",n)
