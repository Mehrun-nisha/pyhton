#list

list1=[1,2]
#print(list1)

list2=[]
#list2.extend(list1)
#list2.append(list1)
list2.insert(0,"fruits")
list2.append(1)
#print(list2)

#list1.pop()
list1.remove(1)
#print(list1)

list3=[2,3,1,9,7]
#list3.sort()
#print(list3)

#list3.reverse()
#print(list3)



a=max(list3)
#print(a)
b=min(list3)
#print(b)

list4=[2,3,4,5,6,7]
sum=0
for i in range(0,len(list4)):
    sum=sum+list4[i]
#print(sum)
#print(sum/len(list4))

list5=[6,4,7,2,8]
list5.sort()
list5.reverse()
#print(list5)

list6=[4,3,5,3,1,5]
lst=[]
for i in list6:
  if list6[i] not in lst:
    lst.append(list6[i])
#print(list6)

#for i,j in enumerate(list6):
   #print("index=",i,"value=",j)

 #tupple----------------------
#1
tup1=(1,)
#print(tup1)
#print(type(tup1))
#2
#print(tup1.append(2))--cant be done because tupples are immutable
tup2=(2,)
tup3=tup1+tup2
#print(tup3)

#3
tup4=(2,3,4)
#del tup4
#print(tup4)#gives an error
#lst=list(tup4)
#print(lst)
#lst.remove(0)
#lst.pop()
#print(lst)
#tup=tuple(lst)
#print(tup)


#4
tup5=(7,6,8,4,2)
lst=list(tup5)
#lst.sort()
#print(lst)
#tup=tuple(lst)
#print(tup)

#5
tup6=(7,6,8,4,2)
#lst=list(tup6)
#lst.reverse()
#print(lst)
#tup7=tuple(lst)
#print(tup7)
tup=(7,6,7,4,3)
#tup10=reversed(tup)
#print(tup10)
tup10=tup[::-1]
print(tup10)
#6
tup8=(6,4,8,3)
tup9=tup8[0]
#for i in range(len(tup8)):
  
  #if tup8[i]>tup9 :
  #   tup9=tup8[i]
     
#print(tup9)

#7
tup8=(6,4,8,3)
tup9=tup8[0]
#for i in range(len(tup8)):
  
 # if tup8[i]<tup9 :
   #  tup9=tup8[i]
     
#print(tup9)

#8
tup9=(7,6,9,5,4)
#sum=0
#for i in range(len(tup9)):
 #  sum=sum+tup9[i]
#print(sum)
   
#9
tup9=(7,6,9,5,4)
sum=0
#for i in range(len(tup9)):
  # sum=sum+tup9[i]
 #  avg=sum/len(tup9)
#print(avg)

#set-----------------

#1
set={"",}
print(set)
print(type(set))

#2
set2={2,3,4}
set3={2,6,7,8}
#set2.update(set3)--method1
#print(set2)

#set2= set2.union(set3)--method2
#print(set2)

#3
#set2.remove(3)
#print(set2)
#4
#set2= set2.union(set3)--method2
#print(set2)

#5
#set2= set2.intersection(set3)
#print(set2)

#6
#print(set3.difference(set2))
#print(set3-set2)

#7
#print(set3.symmetric_difference(set2))

#8
#set4={5,6,7}
#for i in range(len(set4)):
  # if 8 in set4:
 #   print("element is present")

#9
set5={4,5,6,7}
for i,j in enumerate(set5):
        print("index=",i ,"value=",j)


















