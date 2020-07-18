def wrap(string, max_width):
    out = [(string[i:i+max_width]) for i in range(0, len(string), max_width)]
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for element in result:
        print(element)
    