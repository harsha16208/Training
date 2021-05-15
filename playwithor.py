def game_with_number (arr,  n) :
    for i in range(1,len(arr)):
        val=arr[i-1] | arr[i]
        arr[i-1]=val
    return arr
