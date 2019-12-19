from base_inplace_sort import Inplace_sort

class Selection_sort(Inplace_sort):
        
    def sort(self):
        for i in range(len(self.items)-1):
            j = self.find_smallest(i)
            self.swap(i, j)
        return None


    def find_smallest(self, start):
        smallest_val, smallest_index = self.items[start], start

        for j in range(start,len(self.items)):
            if self.items[j] < smallest_val:
                smallest_val, smallest_index = self.items[j], j
        return smallest_index