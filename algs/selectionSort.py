import time

def selection_sort(the_list):

    start = time.time()

    for i in range(len(the_list)):

        # Run through the unsorted elements in the input, finding
        # the smallest one.
        smallest_index = i
        for j in range(i + 1, len(the_list)):
            if the_list[j] < the_list[smallest_index]:
                smallest_index = j

        # Move the smallest element to the front of the unsorted portion
        # of the input (swapping with whatever's already there).
        the_list[i], the_list[smallest_index] = the_list[smallest_index], the_list[i]

    end = time.time()
    print(the_list)
    print(f"Finished in {end - start}")

    return the_list


selection_sort([0, 5, 4, 67, 93, 1])