import ctypes as ct
import array as arr

def main():
    # fibonachi()
    # string_mutation()
    extra()

def extra():
    a = arr.array('i', [1,2,3,4,5,6,7])
    a.append(58)
    a.insert(3, 938)
    a.extend([34, 45])

    for n in a:
        print(n)

def string_mutation():
    str = 'simple python string'
    m_str = ct.create_string_buffer(3, 8)
    print(ct.sizeof(m_str), repr(m_str.raw))
    
    my_char = ct.create_string_buffer(b'single line')
    my_char.len = b'single line plue multi line \n this is in second line'
    print(ct.sizeof(my_char), repr(my_char.raw))


def fibonachi():
    (one, two) = (0, 1)

    limit = 1000

    while one < limit:
        print(one)
        (one, two) = (two, one+two)


if __name__ == "__main__":
    main()