from random import seed
from random import randint

from bubblesort import Bubble_sort as bsort
from insertionsort import Insertion_sort as isort

def trysort(sort_method):
    seed(50)
    input_array = [randint(0, 10) for x in range(20)]

    print('Unsorted: {}'.format(input_array))
    sort_method(input_array)
    print('Sorted:   {}'.format(input_array))

print('Insertion Sort:')
trysort(isort().sort)

print('Bubble Sort:')
trysort(bsort().sort)
