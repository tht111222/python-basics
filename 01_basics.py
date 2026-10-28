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

if 1997 in list:
    print("1997 is in the list")
else:
    print("1997 is not in the list")    


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
del tinydict3["class"]
print("删除后的字典：",tinydict3)
tinydict3.clear()
print("清空后的字典：",tinydict3)
del tinydict3
#print("删除后的字典：",tinydict3)
#重复出现时记住后值
tinydict4={"abc":123,"xyz":456,"abc":789,"xyz":452}
print("tinydict4:",tinydict4)
#不能用列表作为字典的key
#tinydict={["wc"]:666}
#print("tinydict['wc']:",tinydict["wc"])

#词频统计
#split()方法对字符串进行切片
text = "the cat and the hat"
split_text = text.split()
print("split_text:",split_text)
print("text.split('-'):",text.split("-"))
len_split_text=len(split_text)
print("len_split_text:",len_split_text)
#dict.get()方法获取字典中指定键的值，如果键不存在，则返回默认值
d={"the":11}
d.get("the",0)
#定义函数进行词频统计
def word_count(text):
    split_text=text.split()
    word_freq={}
    for word in split_text:
        word_freq[word]=word_freq.get(word,0)+1
    return word_freq
result = word_count("the cat and the dog and the bird")
print(result)

