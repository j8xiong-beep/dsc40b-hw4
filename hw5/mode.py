def mode(numbers):
    '''
    Efficiently finds the mode of a list of numbers.
    '''
    #TODO: Implement the mode function
    counts = {}
    best = numbers[0]

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > counts[best]:
            best = num

    return best

