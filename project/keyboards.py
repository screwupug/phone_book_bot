from aiogram.types import KeyboardButton

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder


def get_log_in_out():
    kb = [
        [KeyboardButton(text="Записать контакт")],
        [KeyboardButton(text="Посмотреть контакт")],
        [KeyboardButton(text="Удалить контакт")],
        [KeyboardButton(text="Показать файл")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Выберите действие')
    return keyboard


def get_log_out():
    kb = [
        [KeyboardButton(text="Показать контакт одной строкой")],
        [KeyboardButton(text="Показать контакт в несколько строк")],
        [KeyboardButton(text="Назад")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Выберите действие')
    return keyboard


def choose_contact():
    keyboard = KeyboardBuilder(KeyboardButton)
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for line in file:
            keyboard.add(KeyboardButton(text=line))
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)
