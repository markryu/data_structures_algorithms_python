
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
def main():
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



if __name__ == '__main__':
    main()
