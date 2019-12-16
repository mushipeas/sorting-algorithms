
class Insertion_sort:
    def __call__(self, items):
        return self.sort(items)
        
    def sort(self, items):
        for i in range(1,len(items)):
            j = i
            while j and items[j] < items[j-1]:
                self.swap(items, j, j-1)
                j -= 1


    def swap(self, items, j, k):
        items[j], items[k] = items[k], items[j]
        return None