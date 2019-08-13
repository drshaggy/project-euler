def multipleOf(multiple,max):
    #Find array of multiples up to a maximum limit
    arr = []
    for x in range(1,max):
        new = x*multiple
        if new < max:
            arr.append(new)
    return arr

def combineArray(arr1,arr2):
    #Combines arrays and remove duplicates and sorts
    for x in arr1:
        arr2.append(x)
    arr2.sort()
    new = list(set(arr2))
    return new

x=1000
three=multipleOf(3,x)
five=multipleOf(5,x)
com=combineArray(three,five)
ans=sum(com)
print(ans)
