import abc

class Inplace_sort:

    def __call__(self, items):
        self.items = items
        return self.sort()

    @abc.abstractmethod
    def sort(self):
        """
        Initiate the in-place sorting of self.items and return None when finished
        """    
    
    def swap(self, j, k):
        self.items[j], self.items[k] = self.items[k], self.items[j]
        return None
