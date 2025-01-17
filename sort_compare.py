import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end = time.time()
    return a_list, end - start


def shellSort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)

        # print("After increments of size", sublistcount, "The list is", a_list)

        sublistcount = sublistcount // 2

    end = time.time()
    return a_list, end - start


def gapInsertionSort(a_list, start, gap):

    for i in range(start + gap, len(a_list), gap):
        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue


def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    return sorted(a_list)


def main():
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time = 0
        for i in range(10):
            mylist = get_me_random_list(the_size)
            start = time.time()
            python_sort(mylist)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 10
        print(
            f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements"
        )

        total_time = 0
        for i in range(10):
            mylist = get_me_random_list(the_size)
            start = time.time()
            insertion_sort(mylist)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 10
        print(
            f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements"
        )

        total_time = 0
        for i in range(10):
            mylist = get_me_random_list(the_size)
            start = time.time()
            shellSort(mylist)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 10
        print(
            f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements"
        )


if __name__ == "__main__":
    """Main entry point"""
    main()
