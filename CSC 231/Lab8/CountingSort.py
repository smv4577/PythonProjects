def countSort(myList, upper):
    """
    Sorts the list of integers which range from 0 to range
    :param myList: The list to sort
    :param upper: The maximum integer value
    :return: Nothing
    """
    buckets = (upper + 1) * [0]
    for number in myList:
        buckets[number] += 1
    counter = 0
    for index in range(len(buckets)):
        value = buckets[index]
        for x in range(value):
            myList[counter] = index
            counter += 1
