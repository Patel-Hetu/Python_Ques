#part 2 question 1


def search(a,num):
    if num not in a:
        return False 
    mid = len(a)//2
    if a[mid] == num:
        return mid
    elif a[mid]<num:
        return search((a[mid+1:],num))
    else:
        return search((a[:mid],num))
    
print(search([4,9,13,303,3000],13))


    