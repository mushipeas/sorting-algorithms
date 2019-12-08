class Quick_sort():
    def sort(self, items, left = 0, right = None):
        if right == None: right = len(items) - 1

        if left < right:
            pivot_ind = self.select_pivot(items, left, right)
            i = self.partition(items, left, right, pivot_ind)

            self.sort(items, left, i-1)
            self.sort(items, i+1, right)
        return None


    def partition(self, items, left, right, pivot_ind):
        if not pivot_ind == right: self.swap(items, pivot_ind, right)
        pivot = items[right]

        i = left - 1
        for j in range(left, right + 1):
            if items[j] <= pivot:
                i += 1
                self.swap(items, i, j)
        # self.swap(items, i, right)
        return i

    def select_pivot(self, items, left, right):
        return right
    
    def swap(self, items, j, k):
        items[j], items[k] = items[k], items[j]
        return None


if __name__ == "__main__":
    
    from random import randint
    
    qs = Quick_sort()

    # items = [6, 1, 3, 2, 9, 5, 1, 10, 6, 7, 3, 2, 6, 8, 2, 2, 2, 0, 10, 1]
    items = [10, 7, 8, 9, 1, 5]
    print('Original: ' + str(items))
    qs.sort(items)
    print('Sorted:   ' + str(items))
    
    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    qs.sort(items)
    print('Sorted:   ' + str(items))

    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    qs.sort(items)
    print('Sorted:   ' + str(items))
    