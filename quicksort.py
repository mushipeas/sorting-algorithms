from random import seed
from random import randint

class Quick_sort:
    def quicksort(self, items, left, right):
        pivot_index = self.select_pivot(items, left, right)
        i = self.partition(items, left, right, pivot_index)

        print(items)
        if i > left:
            self.quicksort(items, left, i-1)
        if i < pivot_index:
            self.quicksort(items, i, right)
            
        return None

    def partition(self, items, left, right, pivot_index):
        while left < right:
            while items[left] < items[pivot_index]:
                left += 1

            while items[right] > items[pivot_index]:
                right -= 1

            if left < right:
                items[left], items[right] = items[right], items[left]
                left += 1
                right -= 1

        return left

    def select_pivot(self, items, left, right):
        return int((left + right)/2)