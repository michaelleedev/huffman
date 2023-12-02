from node import node
import os.path


def main(input):
    data = extract_data(input)
    root = create_tree(data)




def encode(root):
    # creating dictionary of all characters' count in the argument/file
    


# determines the type of input entered and extracts data
# returns dictionary of counts
# param: user argument
# return: dictionary(key : str, value : int)
def extract_data(input):
    if input is None:
        raise TypeError

    if os.path.isfile(input):
        file_name, file_ext = os.path.splitext(input)
        if file_ext != ".txt":
            raise TypeError
        else:
            data = read_file(input)

    else:
        if type(input) is str:
            data = read_arg(input)
        else:
            raise TypeError


# iterates throught the user argument and returns a dictionary
# param: str
# return: dictionary(key: str, value: int)
def read_arg(input):
    data = {}
    for c in input:
        data[c] += 1
    return data


# reads the file and returns a dictionary of character and count
# param: text file
# return: dictionary(key : str, value : int)
def read_file(file):
    data = {}
    with open(input, "r") as file:
        while True:
            c = file.read(1)
            data[c] += 1
            if not c:
                break

    return data


# takes a dictionary of character counts and returns another dictionary
# with huffman code for each character
# param: dictionary
# return: dictionary(key: str, value: str)
def create_tree(data):
    l = []
    keys = data.keys()

    # turn dictionary element into node and append it to a list
    for i in keys:
        l.append(node(i, data[i]))

    # create tree
    while len(l) > 1:
        l.sort(key=lambda n: n.value)
        a = l.pop(0)
        b = l.pop(0)

        if ord(a.char) > ord(b.char):
            c = b
            b = a
            a = c

        new_node = node(b.char, (a.value + b.value), a, b)
        l.append(new_node)

    root = l.pop()
    return root


if __name__ == "__main__":
    main()
