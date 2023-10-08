from functools import wraps
import time

def my_decorator_func(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        start_time = time.time()
        result = func(*args, **kwargs)
        # Do something after the function.
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper_func

@my_decorator_func
def mergeSort(array):
    if len(array) > 1:
        length = len(array)
        r = length // 2
        arr1 = array[:r]
        arr2 = array[r:]
        mergeSort(arr1)
        mergeSort(arr2)

        i = j = k = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array[k] = arr1[i]
                i += 1
            else:
                array[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            array[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            array[k] = arr2[j]
            j += 1
            k += 1
    return array

result = mergeSort([10, 11, 13, 4, 56, 7])
print(result)


print(sorted([10, 11, 13, 4, 56, 7]))