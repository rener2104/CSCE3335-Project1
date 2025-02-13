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
