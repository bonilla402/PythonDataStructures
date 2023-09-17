def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    stringList = list(phrase)

    stringList[0] = stringList[0].upper()

    return "".join(stringList)