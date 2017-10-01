import matplotlib.pyplot as pyplot


def bad_hashfunction(s, size):
    '''
    Returns the ordinal value of the first character modulo size of hash table
    :param s: The string to be hashed
    :param size The size of the hash table
    :return: The ordinal value of the first character modulo size
    '''
    return ord(s[0]) % size


def better_hashfunction(s, size):
    sum = 0
    for ch in s:
        sum += ord(ch)
    return sum % size


def even_better_hashfunction(s, size):
    sum = 0
    count = 1
    for ch in s:
        sum += count*ord(ch)
        count += 1
    return sum % size


def best_hashfunction(s, size):
    sum = 0
    prime = 31
    for ch in s:
        sum += prime*ord(ch)
        prime *= 31
    return sum % size


def average_collisions(table):
    '''
    Given a hash table, compute an average size of each non-empty bin
    :param table: The hash table
    :return: The average size of non-empty bins
    '''
    sum = 0
    count = 0
    for value in table:
        if value > 0:
            sum += value
            count += 1

    if count == 0:
        return 0
    else:
        return sum / count

# determine which is best by counting how many times words fall into each bin in a pseudo-hash table

englishWordFile = open("wordsEn.txt", "r")
words = []
for line in englishWordFile:
    word = line.strip().lower()
    if word != "":
        words.append(word)

print("There are ", len(words), " words in the file.")


# experiment # 1
# make a table with size 100
table = 100 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = bad_hashfunction(w, len(table))
    table[h] += 1
print(table)  # just for debugging purposes
# now let's graph the table
pyplot.plot(table)
pyplot.title("Experiment 1: Use First Character")
pyplot.show()
print("Average collisions (Experiment 1)", average_collisions(table))


# experiment # 2
# make a table with size 1000
table = 1000 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = better_hashfunction(w, len(table))
    table[h] += 1
print(table)  # just for debugging purposes
# now let's graph the table
pyplot.plot(table)
pyplot.title("Experiment 2: Use All Characters")
pyplot.show()
print("Average collisions (Experiment 2)", average_collisions(table))


# experiment # 3
# make a table with size 10000
table = 10000 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = even_better_hashfunction(w, len(table))
    table[h] += 1
print(table)  # just for debugging purposes
# now let's graph the table
pyplot.plot(table)
pyplot.title("Experiment 3: Use All Characters And Their Position")
pyplot.show()
print("Average collisions (Experiment 3)", average_collisions(table))


# experiment # 4
# make a table with size 100000
table = 100000 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = best_hashfunction(w, len(table))
    table[h] += 1
print(table)  # just for debugging purposes
# now let's graph the table
pyplot.plot(table)
pyplot.title("Experiment 4: Use All Characters And 31**Their Position")
pyplot.show()
print("Average collisions (Experiment 4)", average_collisions(table))
