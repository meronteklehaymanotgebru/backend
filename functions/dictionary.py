def adding_dic(lst):
    hash={}
    count=1
    for i in lst:
        hash[i]=count 
        if i in hash:
            hash[i]+=count
return hash
# print(addingDic([1,2,3,4,3,5]))