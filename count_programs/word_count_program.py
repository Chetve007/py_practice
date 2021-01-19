"""
Read files and return count of strings, words and symbols
"""
import sys


def main():
    """Initial counts"""
    line_count = 0
    word_count = 0
    char_count = 0

    option = None
    params = sys.argv[1:]
    if len(params) > 1:
        option = params.pop(0).lower().strip()
    filename = params[0]
    with open(filename) as infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count = len(words)

    if option == '-c':
        print(f'File has {char_count} characters')
    elif option == '-w':
        print(f'File has {word_count} words')
    elif option == '-l':
        print(f'File has {line_count} lines')
    else:
        print(f'File has {line_count} lines, {word_count} words, {char_count} characters')


if __name__ == '__main__':
    main()
