'''Write a python program which takes a list of ‘n’ numbers as an input, then gives the index as input and it should display the element at the index'''
try:
    n=int(input("Enter the range :  "))
    list_=[]
    for i in range(0,n):
        num=int(input())
        list_.append(num)
    a=int(input("Enter the index : "))
    print("The element at ",a," is ",list_[a])
except IndexError:
    print("index exceeds limit !")
    print("the last index is  : ",len(list_) -1)
