from base_inplace_sort import Inplace_sort

class Quick_sort(Inplace_sort):
        
    def sort(self, left = 0, right = None):
        if right is None: right = len(self.items) - 1

        if left < right:
            pivot_ind = self.select_pivot(left, right)
            i = self.partition(left, right, pivot_ind)

            self.sort(left, i-1)
            self.sort(i+1, right)
        return None

# current method has recursion issues for large arrays. Needs fixing
    def partition(self, left, right, pivot_ind):
        if not pivot_ind == right: self.swap(pivot_ind, right)
        pivot = self.items[right]

        i = left - 1
        for j in range(left, right + 1):
            if self.items[j] <= pivot:
                i += 1
                self.swap(i, j)
        return i

    def select_pivot(self, left, right):
        return right

if __name__ == "__main__":
    
    from random import randint
    
    qs = Quick_sort()

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
    