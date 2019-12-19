import abc

class Inplace_sort:
    def __call__(self, items):
        return self.sort(items)

    @abc.abstractmethod
    def sort(self, items):
        """
        Initiate the in-place sorting and return None when finished
        """    
    
    @staticmethod
    def swap(items, j, k):
        items[j], items[k] = items[k], items[j]
        return None
