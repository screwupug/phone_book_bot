import os
import datetime
from pathlib import Path


def get_path_txt(user_name: str) -> str:
    """
    Generate filepath
    :param user_name: User-name
    :return: filepath
    """
    return os.path.join('phone_books', f'phone_book_{user_name}.txt')


def handle_line(line: str) -> list[str, ...]:
    """
    Handling line and deleting backspaces and punctuation marks
    :param line: line with contact info
    :return: handle result
    """
    lst = line.split(', ')
    return lst


def check_line_list(line: list[str, ...]) -> bool:
    """
    Checking line list length
    """
    assert len(line) == 4, "Ошибка ввода! Попробуйте еще раз"


def checked_handle_line(line: str) -> list[str, ...]:
    """
    Handling and checking contact line
    :param line: contact line
    :return: contact line
    """
    line = handle_line(line)
    check_line_list(line)
    return line


def checked_line_str(line: str) -> str:
    """
    Checking line str length
    """
    line = handle_line(line)
    check_line_list(line)
    return ", ".join(line)


def write_line(line: list[str, ...], user_name: str):
    """
    Write contact in file
    :param line: contact info
    :param user_name: user-name
    """
    if not os.path.isdir("phone_books"):
        os.mkdir("phone_books")
    with open(get_path_txt(user_name), 'a', encoding='utf-8') as file:
        file.write(', '.join(line) + '\n')


def show_line(line: str, user_name: str) -> list:
    """
    Show contact from file
    :param line: name and surname
    :param user_name: user-name
    :return: contact line in file
    """
    line = handle_line(line)
    assert len(line) == 2, \
        "Ошибка ввода! Попробуйте еще раз"
    with open(get_path_txt(user_name), 'r', encoding='utf-8') as file:
        for item in file.readlines():
            if item.count(line[0]) > 0 and item.count(line[1]) > 0:
                return handle_line(item)
            else:
                raise ValueError('Контакт не найден')


def delete_contact(line: str, user_name: str):
    """
    Delete contact from file
    :param line: contact line
    :param user_name: user-name
    """
    line = checked_line_str(line)
    with open(get_path_txt(user_name), 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for item in lines:
        if line in item:
            lines.remove(item)
    lines = list(filter(None, lines))
    with open(get_path_txt(user_name), 'w', encoding='utf-8') as F:
        F.writelines(lines)


def change_contact(line: str, user_name: str, field_number: int, field_for_change: str):
    """
    Change contact line
    :param line: contact line
    :param user_name: user-name
    :param field_number: number of field to change
    :param field_for_change: changed string
    """
    line = checked_handle_line(line)
    with open(get_path_txt(user_name), 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    for item in file_lines:
        if item.count(line[2]) > 0:
            file_lines.remove(item)
            line_to_change = item.split(', ')
    line_to_change[field_number] = field_for_change
    file_lines.append(", ".join(line_to_change) + '\n')
    file_lines = list(filter(None, file_lines))
    with open(get_path_txt(user_name), 'w', encoding='utf-8') as file:
        file.writelines(file_lines)


def logger(user_name: str, action_name: str):
    """
    Log all actions in file
    :param user_name: user-name
    :param action_name: action-name
    """
    path = os.path.join('logger', 'logs.txt')
    if not os.path.isdir("logger"):
        os.mkdir("logger")
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                   f"user - {user_name} | action - {action_name}\n")
