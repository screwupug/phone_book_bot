from aiogram.types import KeyboardButton

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder
from project.constants import UserTextEnum
from project.logic import get_path_txt


CHOOSE_OPERATION_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=UserTextEnum.WRITE_CONTACT)],
        [KeyboardButton(text=UserTextEnum.SHOW_CONTACT)],
        [KeyboardButton(text=UserTextEnum.CHANGE_CONTACT)],
        [KeyboardButton(text=UserTextEnum.DELETE_CONTACT)],
        [KeyboardButton(text=UserTextEnum.DOWNLOAD_FILE)]
    ],
    resize_keyboard=True,
    input_field_placeholder=UserTextEnum.PLACEHOLDER
)


CHOOSE_CONTACT_VIEW_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=UserTextEnum.SHOW_CONTACT_IN_ONE_LINE)],
        [KeyboardButton(text=UserTextEnum.SHOW_CONTACT_IN_LINES)],
        [KeyboardButton(text=UserTextEnum.SHOW_CONTACT_CARD)],
        [KeyboardButton(text=UserTextEnum.SHOW_ALL_CONTACTS)],
        [KeyboardButton(text=UserTextEnum.BACK)]
    ],
    resize_keyboard=True,
    input_field_placeholder=UserTextEnum.PLACEHOLDER
)

CHOOSE_CHANGE_CONTACT_OPTION_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=UserTextEnum.CHANGE_FIRST_NAME)],
        [KeyboardButton(text=UserTextEnum.CHANGE_LAST_NAME)],
        [KeyboardButton(text=UserTextEnum.CHANGE_PHONE_NUMBER)],
        [KeyboardButton(text=UserTextEnum.CHANGE_CONTACT_DESCRIPTION)],
        [KeyboardButton(text=UserTextEnum.BACK)]
    ],
    resize_keyboard=True,
    input_field_placeholder=UserTextEnum.PLACEHOLDER
)

BACK_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=UserTextEnum.BACK)]
    ],
    resize_keyboard=True,
    input_field_placeholder=UserTextEnum.PLACEHOLDER
)


def choose_contact_for_operation(user_name: str):
    """
    Keyboard for choosing contact to delete
    """
    keyboard = KeyboardBuilder(KeyboardButton)
    with open(get_path_txt(user_name), 'r', encoding='utf-8') as file:
        for line in file:
            keyboard.add(KeyboardButton(text=line))
        keyboard.add(KeyboardButton(text=UserTextEnum.BACK))
    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)
