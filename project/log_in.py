import re


def log_in(data):
    pattern = re.compile(r'\+\d{11}')
    try:
        line = data.split(', ')
        assert len(line) == 4
        if pattern.findall(line[2]):
            with open('phone_book.txt', 'a', encoding='utf-8') as file:
                file.write(", ".join(line) + '\n')
            return True
        else:
            return False
    except Exception as error:
        print(error)
        return False
