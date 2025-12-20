import numpy as np

#Creating a list of 100 random numbers from 0 to 1000
num_list = np.random.randint(0, 1001, size=100).tolist()

#sort list from smallest to largest without using sort() function (Bubble sort)
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
    # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

 #calculate avg of the list
def calculate_average(arr):
    #sort the list
    bubble_sort(arr)

    #calculate avg for odd numbers

    #step 1: sum of odd numbers
    odd_sum = sum(arr[i] for i in range(len(arr)) if arr[i] % 2 != 0)
    #step 2: count of odd numbers
    odd_count = sum(1 for i in range(len(arr)) if arr[i] % 2 != 0)
    #step 3: average of odd numbers
    odd_avg = odd_sum / odd_count if odd_count != 0 else 0

    #calculate avg for even numbers

    #step 1: sum of even numbers
    even_sum = sum(arr[i] for i in range(len(arr)) if arr[i] %2 == 0)
    #step 2: count of even numbers
    even_count = sum(1 for i in range(len(arr)) if arr[i] % 2 == 0)
    #step 3: average of even numbers
    even_avg = even_sum / even_count if even_count != 0 else 0

    #print results
    print(f'Average of odd numbers: {odd_avg}')
    print(f'Average of even numbers: {even_avg}')

#call the func to calculate avg
calculate_average(num_list)


