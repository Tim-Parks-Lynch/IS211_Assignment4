import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    return found, end - start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()
    return found, end - start


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end - start


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1 :], item)


def main():
    the_size = [500, 1000, 10000]

    for size in the_size:
        total_time1 = 0
        total_time2 = 0
        total_time3 = 0
        total_time4 = 0

        for i in range(100):
            mylist = get_me_random_list(size)

            # Sequential Search
            start1 = time.time()
            sequential_search(mylist, 99999999)
            time_spent1 = time.time() - start1
            total_time1 += time_spent1

            mylist = sorted(mylist)

            # Ordered Sequential Search
            start2 = time.time()
            ordered_sequential_search(mylist, 99999999)
            time_spent2 = time.time() - start2
            total_time2 += time_spent2

            # Binary Search Iterative
            start3 = time.time()
            binary_search_iterative(mylist, 99999999)
            time_spent3 = time.time() - start3
            total_time3 += time_spent3

            # Binary Search Recursive
            start4 = time.time()
            binary_search_recursive(mylist, 99999999)
            time_spent4 = time.time() - start4
            total_time4 += time_spent4

        avg_time1 = total_time1 / 100
        avg_time2 = total_time2 / 100
        avg_time3 = total_time3 / 100
        avg_time4 = total_time4 / 100

        print(
            f"Sequential Search took {avg_time1:10.7f} seconds to run, on average for a list of {size} elements\n"
            f"Ordered Sequential Search took {avg_time2:10.7f} seconds to run, on average for a list of {size} elements\n"
            f"Binary Search Iterative took {avg_time3:10.7f} seconds to run, on average for a list of {size} elements\n"
            f"Binary Search Recursive took {avg_time4:10.7f} seconds to run, on average for a list of {size} elements\n"
        )


if __name__ == "__main__":
    """Main entry point"""
    main()
