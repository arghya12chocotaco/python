a=[]
insert_ele=int(input("inserted element"))
pos_ele=int(input("position"))
del_ele=int(input("delete element"))
a.append(2)
a.append(4)
a.insert(pos_ele,insert_ele)
a.remove(del_ele)
a.pop(0)
print(a)