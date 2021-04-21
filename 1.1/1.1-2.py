arr = [591, 451, 274, 982, 422, 61, 649, 860]

def main():
    for i in range(len(arr)):
        tmp = arr[i]
        j = i
        
        while (j>0 and tmp > arr[j-1]):
            arr[j]=arr[j-1]
            j = j-1
        arr[j]= tmp
        print(arr)
    print(arr)
    
main()