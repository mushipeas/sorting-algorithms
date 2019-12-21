from random import seed
from random import randint

from bubblesort import Bubble_sort as bsort
from insertionsort import Insertion_sort as isort
from selectionsort import Selection_sort as ssort
from quicksort import Quick_sort as qsort
from mergesort import Merge_sort as msort

from helpers import clock_maker

def try_sort(sort_method, runs=5, array_len=1000, r_start=0, r_end=50):

    attempts = []
    cm_decorator = clock_maker(runs=0)
    sort_method = cm_decorator(sort_method())

    for _ in range(runs):
        input_array = [randint(r_start, r_end) for x in range(array_len)]
        
        try:
            sorted_builtin = sorted(input_array)
            sort_method(input_array)
            attempts.append(sorted_builtin == input_array)
        except:
            pass
    
    avg_runtime = cm_decorator.avgtime()

    resolution = 'correctly sorted' if all(attempts) and len(attempts) == runs else 'did NOT sort'
    print('Method {}. Avg time: {:.4f}s'.format(resolution, avg_runtime))
    
    return avg_runtime


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
