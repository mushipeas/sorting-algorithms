from random import seed
from random import randint

from bubblesort import Bubble_sort as bsort
from insertionsort import Insertion_sort as isort
from selectionsort import Selection_sort as ssort
from quicksort import Quick_sort as qsort
from mergesort import Merge_sort as msort

def trysort(sort_method):
    # seed(50)
    attempts = []
    for _ in range(20):
        input_array = [randint(0, 10) for x in range(20)]

        try:
            sorted_builtin = sorted(input_array)
            sort_method(input_array)
            attempts.append(sorted_builtin == input_array)
        except:
            pass
    
    resolution = 'correctly sorted' if all(attempts) else 'did NOT sort'
    print('Method {}.'.format(resolution))

print('Insertion Sort:')
trysort(isort().sort)

print('Bubble Sort:')
trysort(bsort().sort)

print('Selection Sort:')
trysort(ssort().sort)

print('Quick Sort:')
trysort(qsort().sort)

print('Merge Sort:')
trysort(msort().sort)