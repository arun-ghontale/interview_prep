def reverse_string_recurse(string, ind):
    if ind < 0:
        return ''

    return string[ind] + reverse_string_recurse(string, ind=ind-1)

# arun
# func('arun', ind=3) = 'n' + func('aru', ind=2) -> 'n' + 'ura' -> 'nura'
# func('aru', ind=2) = 'u' + func('ar', ind=1) -> 'u' + 'ra' -> 'ura'
# func('ar', ind=1) = 'r' + func('a', ind=0) -> 'r' + 'a' = 'ra'
# func('a', ind=0) = 'a' + func('', ind=-1) -> '' = 'a'
# func('', ind=-1) = ''


def reverse_string(string, recurse=False):
    if not recurse:
        reversed_string = ''
        for ind in range(len(string)-1, -1, -1):
            reversed_string += string[ind]

    else:
        reversed_string = reverse_string_recurse(string=string, ind=len(string) - 1)

    return reversed_string


def main():
    strings = ['this is a string', 'this is another string']
    print("# Iterative")
    for string in strings:
        print(reverse_string(string=string, recurse=False))

    print("\n# Recursive")
    for string in strings:
        print(reverse_string(string=string, recurse=True))


if __name__ == '__main__':
    main()