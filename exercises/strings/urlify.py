"""
1.3
Write a method to replace all spaces in a string with '%20'.
[The rest of the description strongly suggests a requirement to transform
in-place, which I am interpreting as a strict O(n) space requirement.]
"""


def urlify(s, size):
    """
    In order to execute this in place, we use the extra buffer that is
    provided for us at the end of the input string, as a stack.
    I convert to a list here, for clarity.
    First, locate the last character from the end of string.
    Then, insert characters from the end of string, to the start.
    When a space character is encountered, enter '0', '2', '%' while
    decrementing the index of the write pointer.
    """
    s_list = list(s)
    read = size - 1
    write = size - 1

    while read >= 0:
        if not s_list[read].isspace():
            break

        read = read - 1

    while read >= 0:
        if s_list[read].isspace():
            s_list[write] = '0'
            write = write - 1
            s_list[write] = '2'
            write = write - 1
            s_list[write] = '%'
        else:
            s_list[write] = s_list[read]

        read = read - 1
        write = write - 1

    return ''.join(s_list)
