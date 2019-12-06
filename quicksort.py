 
class Quick_sort:
    def sort(self, items, left=0, right=None):
        if not right: right = len(items) - 1
        print(sum(items))
        if left < right and right - left > 1:
            pivot = self.select_pivot(items, left, right)
            p = self.partition(items, left, right, pivot)
            self.sort(items, left, p)
            self.sort(items, p+1, right)
        return None

    def partition(self, items, curr_left, curr_right, pivot):
        while curr_left < curr_right:
            if curr_right == pivot: curr_right -= 1
            if curr_left == pivot: curr_left += 1
            
            if items[curr_left] <= items[pivot]:
                curr_left += 1
            if items[curr_right] > items[pivot]:
                curr_right -= 1
            

            if curr_right > 0 and curr_left < curr_right:
                self.swap(items, curr_left, curr_right)
                curr_left += 1
                curr_right -= 1
        self.swap(items, pivot, curr_left)
        return curr_left

    def select_pivot(self, items, left, right):
        return right
    
    def swap(self, items, j, k):
        items[j], items[k] = items[k], items[j]
        return None