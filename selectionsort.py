
class Selection_sort:
    def sort(self, items):
        for i in range(len(items)-1):
            j = self.find_smallest(items,i)
            self.swap(items,i, j)
        return None


    def find_smallest(self, items, start):
        smallest_val, smallest_index = items[start], start

        for j in range(start,len(items)):
            if items[j] < smallest_val:
                smallest_val, smallest_index = items[j], j
        return smallest_index

    def swap(self, items, j, k):
        items[j], items[k] = items[k], items[j]
        return None