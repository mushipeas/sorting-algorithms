from base_inplace_sort import Inplace_sort

class Insertion_sort(Inplace_sort):

    def sort(self, items):
        for i in range(1,len(items)):
            j = i
            while j and items[j] < items[j-1]:
                self.swap(items, j, j-1)
                j -= 1