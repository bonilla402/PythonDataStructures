def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    prev = ' '
    phrase = phrase.lower()
    capitalized = ''

    for letter in phrase:
        if prev == ' ':
            letter = letter.upper()
        capitalized += letter
        prev = letter

    return capitalized



    # there's a built-in method for this!
    #return phrase.title()

    # or, if you didn't know that, could capitalize each word by hand
    # return ' '.join([s.capitalize() for s in phrase.split(' ')])
