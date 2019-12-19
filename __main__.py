from random import seed
from random import randint

from bubblesort import Bubble_sort as bsort
from insertionsort import Insertion_sort as isort
from selectionsort import Selection_sort as ssort
from quicksort import Quick_sort as qsort
from mergesort import Merge_sort as msort

RUNS = 2

def try_sort(sort_method):

    attempts = []
    sm = sort_method()

    for _ in range(RUNS):
        input_array = [randint(0, 10) for x in range(1000)]
        
        try:
            sorted_builtin = sorted(input_array)
            sm(input_array)
            attempts.append(sorted_builtin == input_array)
        except:
            pass
    
    resolution = 'correctly sorted' if all(attempts) and len(attempts) == RUNS else 'did NOT sort'
    print('Method {}.'.format(resolution))

print('Insertion Sort:')
try_sort(isort)

print('Bubble Sort:')
try_sort(bsort)

print('Selection Sort:')
try_sort(ssort)

print('Quick Sort:')
try_sort(qsort)

print('Merge Sort:')
try_sort(msort)
