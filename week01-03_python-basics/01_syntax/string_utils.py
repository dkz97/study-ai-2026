# A simple custom module

__all__ = ['del_space', 'count_word']


def del_space(string: [str]):
    return string.strip()


def to_lower(string):
    return string.lower()

def count_word(string, s):
    return string.count(s)



if __name__ == '__main__':
    print(count_word("sdad", "s"))