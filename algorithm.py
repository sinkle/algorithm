# with add memory
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
        
def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = l[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return None

def heap_sort(a):
    def parent(i):
        return int(i / 2) 

    def left_child(i, l):
        guess_child = (i + 1) * 2
        if guess_child <= l:
            return guess_child - 1

    def right_child(i, l):
        guess_child = (i + 1) * 2 + 1
        if guess_child <= l:
            return guess_child - 1

    def swap(a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        return a
    
    def heapify(a, i, l=None):
        if l is None:
            l  = len(a) 
        lc = left_child(i, l)
        rc = right_child(i, l)
        if (lc is None) & (rc is None):
            return a
        elif (lc is not None) & (rc is not None):
            if (a[i] >= a[lc]) & (a[i] >= a[rc]):
                return a
            elif a[lc] >= a[rc]:
                swap(a, i, lc)
                heapify(a, lc, l)
            else:
                swap(a, i, rc)
                heapify(a, rc, l)
        elif lc is not None:
            if a[i] >= a[lc]:
                return a
            else:
                swap(a, i, lc)
                heapify(a, lc, l)
        else:
            if a[i] >= a[rc]:
                return a
            else:
                swap(a, i, rc)
                heapify(a, rc, l)
        

    def heap_make(a):
        i = int(len(a) / 2) - 1
        l = len(a)
        while i >= 0:
           heapify(a, i)
           i -= 1
    
    def start_sort(a):
        l = len(a) - 1
        while l > 0:
            swap(a, 0, l)
            heapify(a, 0, l - 1)
            l -= 1
    
    heap_make(a)
    start_sort(a)
    print(a)

test_array = [2, 1, 5, 4, 1, 7, 3, 9, 5]

# print(quick_sort([2,1,5,4,1,7,3,9,5]))
heap_sort([2, 1, 5, 4, 1, 7, 3, 9, 5])

# print(binary_search([0, 3 , 6 , 10, 12], 6))
