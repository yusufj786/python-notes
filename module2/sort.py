
#Q3 : Sorting in Ascending order
# a =[1,0,10,30,23,78,100,4,2,43,52,67]
# a.sort()
# print(a)

a =[1,0,10,30,23,78,100,4,2,43,52,67]
# a =[1,10,0,30,23,78,100,4,2,43,52,67]
# a =[1,10,30,0,23,78,100,4,2,43,52,67]
# a =[1,10,30,23,0,78,100,4,2,43,52,67]
# a =[1,10,30,23,78,0,100,4,2,43,52,67]
# a =[1,10,30,23,78,100,0,4,2,43,52,67]
# a =[1,10,30,23,78,100,4,0,2,43,52,67]
# a =[1,10,30,23,78,100,4,2,0,43,52,67]
# a =[1,10,30,23,78,100,4,2,43,0,52,67]
# a =[1,10,30,23,78,100,4,2,43,52,0,67]
# a =[1,10,30,23,78,100,4,2,43,52,67,0]
n = len(a)
#             (0 till 11)
for i in range(n):
    print('i updated going for next round')
    for j in range(n):
        print('i=',i,' j=',j)
        if(a[i] < a[j]):
            s = a[i]
            a[i] = a[j]
            a[j] = s
    print(a)
