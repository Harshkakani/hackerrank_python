def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        octal = (oct(i)[2:]).rjust(w,' ')
        hexa = (hex(i)[2:]).upper().rjust(w,' ')
        binary  = (bin(i)[2:]).rjust(w,' ')
        y = print(str(i).rjust(w,' '), octal, hexa, binary)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)