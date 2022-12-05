print('hello\n world')
# Find The Output
#Input = "the sky is blue"
#Output = "blue is sky the
s = "the sky is blue"
l= s.split()
l = l[::-1]
l = ' '.join(l)
print (l)
l="My Name is lalit"
print(l[2:5:2])
items=[int,float,"harry",5,7,9,67]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)

# for i in range(4):
#     for j in range(4):
#         print("#",end="")
#     print()


# for i in range(4):
#     for j in range(4-i):
#         print("#",end="")
#     print()