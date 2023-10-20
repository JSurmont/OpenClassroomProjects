def to_absolute(number):
    """
        >>> to_absolute(3)
        3

        Volontairement en erreur
        >>> to_absolute(-10)
        -10
    """
    if number <= 0:
        return -number
    return number


def reverse_str(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        # final_string += initial_string[index - 2]  # ligne en erreur
        final_string += initial_string[index - 1]
        index = index - 1
    return final_string
