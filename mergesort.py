
class Merge_sort:
    def sort(self, items):
        sorted_list = self.sort_helper(items)
        items.clear()
        items.extend(sorted_list)

    def sort_helper(self, items):
        if len(items) <= 1: return items

        left =  self.sort_helper(items[ :(len(items)//2) ])
        right = self.sort_helper(items[ (len(items)//2): ])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_subarray = []
        i = 0
        for j in range(len(left)):
            while i < len(right) and right[i] < left[j]:
                sorted_subarray.append(right[i])
                i += 1
            sorted_subarray.append(left[j])

        if i < len(right): sorted_subarray += right[i:]

        return sorted_subarray


if __name__ == "__main__":
    
    from random import randint
    
    ms = Merge_sort()

    items = [6, 1, 3, 2, 9, 5, 1, 10, 6, 7, 3, 2, 6, 8, 2, 2, 2, 0, 10, 1]
    print('Original: ' + str(items))
    ms.sort(items)
    print('Sorted:   ' + str(items))
    
    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    ms.sort(items)
    print('Sorted:   ' + str(items))

    items = [randint(0,10) for x in range(20)]
    print('Original: ' + str(items))
    ms.sort(items)
    print('Sorted:   ' + str(items))