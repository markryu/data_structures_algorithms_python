
"""
Dictionary is maintaining a single data structure while accessing an interest data using an associated index/key.

Syntax
=========================================
    create_dict = {}
    create_dict = dict()
    <dict_name>['<key>'] = <value>
=========================================

Constraints
=========================================
    - keys are unique
    - keys must be immutable type
    - float as a key may give you problems due to accuracy issues
    - there are no orders in using dictionaries
=========================================

"""
grades = {
    'A': 99,
    'B': 93,
    'C': 93,
    'D': 91,
    'E': 98,
}
print ('Is F in grades? ', 'F' in grades)
print ("grades['A']: ", grades['A'])
print ('grades: ', grades)
print ("del(grades['E'])")
del(grades['E'])
print ("grades['E'] is deleted.", grades)
print ("grades.keys(): ", grades.keys())
print ("grades.values(): ", grades.values())

print ('==================================================')

"""
Using a dictionary it is easy to count a frequency of each occurring instances.
"""

def lyrics_to_frequencies(lyrics):
    """
    takes in a lyrics of any song
    iterates to each word of the lyrics
    if the word is already in the dictionary then add a count for it
    else that the word is not yet in the dictionary - add it and count it as valued to 1

    if you have a song lyrics - split each word with a space or a new line then add it into a list
    """
    lyricsDictionary = dict()
    for each_word in lyrics:
        if each_word in lyricsDictionary:
            lyricsDictionary[each_word] += 1
        else:
            lyricsDictionary[each_word] = 1
    return lyricsDictionary


"""
Challenge to self:
    Get the highest occurring word and how many times it shows.
"""

def get_most_occurring(dictionary):
    """
    1. Process #1 the data structure of the dictionary would look like this - { 'THE WORD': 'NUMBER', 'ANOTHER WORD': 'NUMBER' }
    2. Getting the max value should be easy using max( dictionary.values() )
    3. Saving it into a variable like highest_number = max( dictionary.values() )
    4. Now the goal is to find the key which has the same highest_number value
    5. Iterating to each of the keys of the dictionary and then checking if the value is the same
    6. If it is then return the value with the key.
    """
    highest_number = max( dictionary.values() )
    for each_key in dictionary:
        if dictionary[each_key] == highest_number:
            return (each_key, highest_number)
        else:
            print ('There was an error.')






