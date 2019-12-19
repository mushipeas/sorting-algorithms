from base_inplace_sort import Inplace_sort

class Bubble_sort(Inplace_sort):

    def sort(self):
        for _ in range(len(self.items)):
            # print('Iteration {}'.format(_ + 1) )
            flag = False
            for j in range(len(self.items)-1):
                if self.items[j] > self.items[j+1]:
                    self.swap(j, j+1)
                    flag = True
            if not flag: break
        return None