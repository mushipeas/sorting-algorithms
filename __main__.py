from random import seed
from random import randint

from bubblesort import Bubble_sort as bsort
from insertionsort import Insertion_sort as isort
from selectionsort import Selection_sort as ssort

def trysort(sort_method):
    seed(50)
    input_array = [randint(0, 10) for x in range(20)]
    sorted_builtin = sorted(input_array)

    sort_method(input_array)

    resolution = 'correctly sorted' if sorted_builtin == input_array else 'did NOT sort'
    print('Method {}.'.format(resolution))

print('Insertion Sort:')
trysort(isort().sort)

print('Bubble Sort:')
trysort(bsort().sort)

print('Selection Sort:')
trysort(ssort().sort)