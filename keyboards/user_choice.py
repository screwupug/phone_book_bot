from aiogram.types import KeyboardButton

from aiogram.types import ReplyKeyboardMarkup


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
