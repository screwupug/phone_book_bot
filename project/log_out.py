def log_out_one_line(data):
    lst = []
    try:
        msg = data.split(', ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.count(msg[0]) > 0 and line.count(msg[1]) > 0:
                    lst.append(line)
        return lst
    except Exception as error:
        print(error)
        return False


def log_out_lines(data):
    lst = []
    try:
        msg = data.split(', ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.count(msg[0]) > 0 and line.count(msg[1]) > 0:
                    line = line.split(', ')
                    for i in line:
                        lst.append(i)
                        print(lst)
        return lst
    except Exception as error:
        print(error)
        return False
