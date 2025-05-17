def encode_integer(N):
    """
    Encodes an integer between -121 and 121 using a balanced ternary system
    with coefficients -1, 0, or 1 for powers of 3: [81, 27, 9, 3, 1].

    Parameters:
    :param N: The integer to encode.
    :return: A list of coefficients representing the encoded form.
    """
    if N == 0:
        return [0, 0, 0, 0, 0]

    powers = [81, 27, 9, 3, 1]
    coefficients = [0] * 5

    value = N
    for i in range(5):
        remainder = value % 3
        if remainder == 0:
            coefficients[i] = 0
        elif remainder == 1:
            coefficients[i] = 1
            value -= 1
        elif remainder == 2:  # 2 in base 3 balanced ternary becomes -1 with carry
            coefficients[i] = -1
            value += 1
        value //= 3

    # Convert to match order: [81, 27, 9, 3, 1] = [0] * 5
    return coefficients[::-1]  # Reverse to match highest power first