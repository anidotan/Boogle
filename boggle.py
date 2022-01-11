
def get_dimensions(board):
    return len(board), len(board[0])


def get_board_letters(words):
    # todo: do i really need this?
    rows = len(words)
    columns = len(words[0])
    return [words[row][col] for col in range(columns) for row in range(rows)]


def get_all_locations(board):
    rows = len(board)
    cols = len(board[0])
    return [(x, y) for x in range(cols) for y in range(rows)]


def dict_words_game(file_path):
    """
    creats a dict of dicts - first key is the length of the word,
    second key is the first char of the word and then you'll reach a list
    of all the words in the given length, starting with the relevant char
    :param file_path: path to file txt with all the words
    :return: dict
    """
    final_dict = {}
    list_words = list_from_file(file_path)
    for word in list_words:
        word_length = len(word)
        first_char = word[0]
        if word_length not in final_dict:
            final_dict[word_length] = {}

        dict_by_len = final_dict[word_length]
        if first_char not in dict_by_len:
            dict_by_len[first_char] = []

        dict_char_and_len = dict_by_len[first_char]
        dict_char_and_len.append(word)

    return final_dict


def list_from_file(filepath):
    """
    :param filepath: path to file
    :return: list of all the words in the file
    """
    with open(filepath) as data_file:
        words_list = []
        for line in data_file:
            words_list.append(line.strip())
        return words_list


if __name__ == '__main__':
    # print(list_from_file("boggle_dict.txt"))
    x= dict_words_game("boggle_dict.txt")
    # print(sorted(x[3]["A"]))
    print(get_all_locations())
