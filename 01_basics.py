list1=['Google','Runoob',1997,2000]
list2=[1,2,3,4,5]
list3=["a",'b','c','d']
list4=['red','green','blue','yellow','white','black']
list=['red','green','blue','yellow','white','black']
#读
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])
nums=[10,4,3,2,3,2]
print(nums[0:4])
print("list[1]:",list[1])
print("list[1:-2]:",list[1:-2])
#更新列表
list1=['Google','Runoob',1997,2000]
print("list1的第二个元素为：",list1[1])
list[1]=11111
print("更新后的第三个元素为：",list1[1])
list1.append("1234")
print("更新后的列表：",list1)
#删除
list1=['Google','Runoob',1997,2000]
print("原始列表：",list1)
del list1[1]
print("删除第二个元素之后：",list1)
#拼接
list2+=[1,2,3,4,5]
print(list2)
#循环
for x in list1:
    print(x)
    if x==1997:
        print("1997 is in the list")
    else:
        print("1997 is not in the list")    
        break    


