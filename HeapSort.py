def heapify(array,size,root):
    largest=root                                                    #checks whether the parent element is less than its child
    left=2*root+1
    right=2*root+2

    if left<size and array[left]>array[largest]:
        largest=left

    if right<size and array[right]>array[largest]:
        largest=right

    if largest!=root:
        array[largest],array[root]=array[root],array[largest]       #swaps if parent element is less than its child
        heapify(array,size,largest)                                 #Recursively heapifies the affected sub tree

def heapsort(array):
    n=len(array)
    for i in range((n//2)-1,-1,-1):                               #Build heap
        heapify(array,n,i)

    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]                       #move current node to root
        heapify(array,i,0)                                        #max_heapify the reduced tree


size=int(input("Enter the size of the array:"))
array=[]
for i in range(0,size):
    element=int(input("Enter the numbers:"))
    array.append(element)

heapsort(array)

print("The sorted array is:")
for i in range(0,size):
    print(array[i],end='  ')