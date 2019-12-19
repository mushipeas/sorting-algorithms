from base_inplace_sort import Inplace_sort

class Insertion_sort(Inplace_sort):

    def sort(self):
        for i in range(1,len(self.items)):
            j = i
            while j and self.items[j] < self.items[j-1]:
                self.swap(j, j-1)
                j -= 1