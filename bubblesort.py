
class Bubble_sort:
    def sort(self, items):
        for _ in range(len(items)):
            # print('Iteration {}'.format(_ + 1) )
            flag = False
            for j in range(len(items)-1):
                if items[j] > items[j+1]:
                    self.swap(items, j, j+1)
                    flag = True
            if not flag: break
        return None

    def swap(self, items, j, k):
        items[j], items[k] = items[k], items[j]
        return None
