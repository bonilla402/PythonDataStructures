def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dictionary = {}

    for ltr in phrase:
        if ltr in dictionary.keys():
            dictionary[ltr] = dictionary[ltr] + 1
        else:
            dictionary[ltr] = 1

    return dictionary