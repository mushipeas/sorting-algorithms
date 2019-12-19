from base_inplace_sort import Inplace_sort

class Insertion_sort(Inplace_sort):

    def sort(self):
        for i in range(1,len(self.items)):
            j = i
            while j and self.items[j] < self.items[j-1]:
                self.swap(j, j-1)
                j -= 1

        return None

if __name__ == "__main__":
    
    from random import randint
    
    qs = Insertion_sort()

    items = [6, 1, 3, 2, 9, 5, 1, 10, 6, 7, 3, 2, 6, 8, 2, 2, 2, 0, 10, 1]
    print('Original: ' + str(items))
    qs(items)
    print('Sorted:   ' + str(items))
    
    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    qs(items)
    print('Sorted:   ' + str(items))

    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    qs(items)
    print('Sorted:   ' + str(items))
    