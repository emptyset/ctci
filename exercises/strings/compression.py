'''
1.6
Implement a method to perform basic string compression using the counts of
repeated characters.  For example, the string aabcccccaaa would become
a2b1c5a3.  If the "compressed" string would not become smaller than the
original string, your method should return the original string.  You can
assume the string has only uppercase and lowercase letters (a-z).
'''


def compress(s):
    if len(s) < 3:
        return s

    s_list = list(s)
    compressed = []

    while len(s_list) > 0:
        character = s_list.pop(0)
        count = 1

        while True:
            if len(s_list) == 0:
                break

            current = s_list[0]

            if current != character:
                break

            s_list.pop(0)
            count = count + 1

        compressed.append(f'{character}{count}')

    compressed = ''.join(compressed)
    if len(s) <= len(compressed):
        return s
    else:
        return compressed
