# Закодируйте любую строку по алгоритму Хаффмана.
# превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.


from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def get_code(root, codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def haffman_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    print(res)


string = 'Encode any string using the Huffman algorithm'
coding(string, get_code(haffman_tree(string)))
