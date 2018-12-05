id = []
len = int (input("please enter your length id"))
print("enter your id")
for i in range (0,len):
    id.append(int(input("enter your digit:"))) ##add new values id (append)
    if len == 8:
    id.insert(0,0) 
    print("your id:",id)

count = [1,2,1,2,1,2,1,2,1]
print()
print("print the first order")
print(id)
print(count)
print()
for i in range (0,9):
 id[i] =id[i]*count[i]
 print(id)
 print()
 print("after the 1 round")
print("fix the numbers above 9")
for i in range(0,9):
if id[i] > 9:
id  = id(int(id[i]%10))+(int(id[i]/10)
print(id)
print(calculation:)
sum =0
for i in range(0,9):
    sum sum + id[i]
    print(sum)
    if(sum%10) != 0:
    print("this is not VALID")
    else:
    print("this is VALID ")




