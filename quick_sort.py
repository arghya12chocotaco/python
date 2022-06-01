def quick_sort(arr):
    leng=len(arr)
    if leng<=1:
        return(arr)
    else:
        key=arr.pop()
    item_greater =[]
    item_lower =[]
    for item in arr:
        if item>key:
            item_greater.append(item)
        else:
            item_lower.append(item)
    return quick_sort(item_lower)+[key]+quick_sort(item_greater)
arr=[2,5,3,7,8,1]
print(quick_sort(arr))
