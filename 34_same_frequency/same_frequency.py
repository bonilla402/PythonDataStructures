def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    txt1 = str(num1)
    txt2 = str(num2)

    if len(txt1) != len(txt2):
        return False
    
    dictionary1 = {}
    dictionary2 = {}


    for i in range(0, len(txt1)):
        digit = txt1[i]
        dictionary1[digit] = dictionary1.get(digit, 0) + 1

        digit = txt2[i]
        dictionary2[digit] = dictionary2.get(digit, 0) + 1


    return dictionary1 == dictionary2