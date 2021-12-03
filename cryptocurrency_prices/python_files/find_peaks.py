def find_peaks(values: list) -> tuple:
    """Return the position from the end of the last low peak and the last high peak in [values]

    Parameters
    ----------
    values : list

    Returns
    -------
    tuple
    """

    # if the first peak if the high
    if values[-2] > values[-1]:

        # increment the high index while the curve decreases (+1)
        high_index = 2
        while values[-high_index] > values[-high_index + 1]:
            high_index += 1
            if high_index == len(values):
                break

        # if the values are always decreases
        if high_index == len(values) and values[0] > values[1]:
            low_index = None

        else:

            # start the low peak research from the high peak index (+1)
            low_index = high_index
            while values[-low_index] < values[-low_index + 1]:
                low_index += 1
                if low_index >= len(values):
                    break

        # decrement low index and high index if the curve is not always decreases
        if not (high_index == len(values) and values[0] >= values[1]):
            high_index -= 1
        if low_index is not None:
            low_index -= 1

    # if the first peak if the low
    else:

        # increment the low index while the curve is growing (+1)
        low_index = 2
        while values[-low_index] < values[-low_index + 1]:
            low_index += 1
            if low_index == len(values):
                break

        # if the values are always growing
        if low_index == len(values) and values[0] < values[1]:
            high_index = None

        else:

            # start the high peak research from the low peak index (+1)
            high_index = low_index
            while values[-high_index] > values[-high_index + 1]:
                high_index += 1
                if high_index <= len(values):
                    break

        # decrement low index and high index if the curve is not always growing
        if not (low_index == len(values) and values[0] <= values[1]):
            low_index -= 1
        if high_index is not None:
            high_index -= 1

    return low_index, high_index
