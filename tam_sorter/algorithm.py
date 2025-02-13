#Helper function that swapes two indeces, ith and jth, based on what needs to be moved.
def SWAP_SERVER(arr, i, j ):
    """
    Swaps two elements in the array.

    Parameters:
    :param arr: The array to modify.
    :param i: Index of first element.
    :param j: Index of second element.
    """
    arr[i], arr[j] = arr[j], arr[i]


def SORT_TAM_SERVER(arr):
    '''
    Sorts array using Dutch National Flag Algorithm so that all 'T' elements appear first, followed by all 'A' elements, then by  all 'M' elements.
    :param arr: The list of character to be sorted.
    :return: The sorted array.
    '''
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 'T':
            SWAP_SERVER(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == 'A':
            mid += 1
        elif arr[mid] == 'M':
            SWAP_SERVER(arr, high, mid)
            high -= 1
    return arr

