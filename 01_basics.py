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

#字典
#创建加查
tinydict1={"abc":123}
tinydict2={"abc":123,"xyz":456}
print("tinydict1:",tinydict1)
print("length of tinydict1:",len(tinydict1))
print("type of tinydict1:",type(tinydict1))
tinydict3={'Name':"tht","Age":6,"class":"Second"}
print("tinydict3['Name']:",tinydict3["Name"])
print("tinydict3['Age']",tinydict3["Age"])
print("tinydict3['qq']",tinydict3["qq"])
tinydict3["qq"]="123456"
print("更新后的字典：",tinydict3)
del tinydict3["class"]
print("删除后的字典：",tinydict3)
tinydict3.clear()
print("清空后的字典：",tinydict3)
del tinydict3
print("删除后的字典：",tinydict3)
#重复出现时记住后值
tinydict4={"abc":123,"xyz":456,"abc":789,"xyz":452}
print("tinydict4:",tinydict4)
#不能用列表作为字典的key
tinydict={["wc"]:666}
print("tinydict['wc']:",tinydict["wc"])

