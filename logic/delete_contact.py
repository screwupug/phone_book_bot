import re


def delete_contact(data):
    pattern = re.compile(r'\+\d{11}')
    lst = []
    if pattern.findall(data):
        try:
            with open('phone_book.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    lst.append(line.replace('\n', ''))
            for i in lst:
                if i.count(data) > 0:
                    print(i)
                    lst.remove(i)
            with open('phone_book.txt', 'w', encoding='utf-8') as F:
                for j in lst:
                    if j is not None:
                        print(j)
                        F.write(j + '\n')
            return True
        except Exception as error:
            print(error)
            return False
    else:
        return False
