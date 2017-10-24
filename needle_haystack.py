#!/usr/bin/env python

def is_found_in(needle, haystack):
    """
    Finds 'needle' string in the 'haystack' string.
    """
    needle_len = len(needle)
    hay_len = len(haystack)

    for i in range(0, hay_len):
        j = 0

        while j < needle_len and i + j < hay_len:
            if (needle[j] != haystack[i + j]):
                break

            j = j + 1

        if (j == needle_len):
            return True

    return False

if __name__ == '__main__':
    print ""

    haystack = raw_input("Please enter a string: ")

    print ""

    needle = raw_input("Enter a string to find in that: ")

    print ""

    if is_found_in(needle, haystack):
        print('"{0}" was found in string "{1}".'.format(needle, haystack))
    else:
        print('"{0}" was not found in string "{1}".'.format(needle, haystack))

    print ""
