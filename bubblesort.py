from base_inplace_sort import Inplace_sort

class Bubble_sort(Inplace_sort):

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