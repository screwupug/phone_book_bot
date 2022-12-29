import enum


class BotTextEnum(enum.StrEnum):
    """
    Bot's messages
    """
    INITIAL_MESSAGE = """Привет, это бот - телефонная книга
Я могу хранить и показывать контакты
Пожалуйста, выберите, что вы хотите сделать:"""

    LOG_IN_CONTACT = """Отлично!
Введите фамилию, имя, телефон и описание в одну строчку через запятую
Например:
Василий, Пупкин, +79999999999, домашний"""

    LOG_OUT_FORMAT = """Отлично!
Пожалуйста, выберете нужный формат вывода"""

    DELETE_CONTACT = """Отлично
Пожалуйста, выберите контакт, который хотите удалить:"""

    LOGGED_IN_SUCCESS = """Контакт успешно записан"""

    LOGGED_IN_ERROR = """Ошибка!
Возможно вы ввели не все данные или номер в неправильном формате
Попробуйте еще раз:"""

    LOG_OUT_CONTACT = """Пожалуйста, введите фамилию и имя контакта
Например: Пупкин, Василий"""

    CONTACT_NOT_FOUND = """Введенный номер не найден"""
    BACK_IN_MAIN_MENU = """Возвращаемся в главное меню"""
    GO_BACK = """Идем назад"""
    DELETED_SUCCESS = """Контакт успешно удален"""
    ERROR_TEXT = "Ошибка: {}"
    CHOOSE_CONTACT = "Пожалуйста, выберите контакт:"
    CHOOSE_FILE_FORMAT = "Пожалуйста, выберите формат файла:"
    CHOOSE_FIELD_TO_CHANGE = "Пожалуйста, выберите, что вы хотите изменить:"
    TYPE_NEW_VALUE = "Введите новое значение:"
    CHANGED_SUCCESS = "Контакт успешно изменен"


class UserTextEnum(enum.StrEnum):
    """
    User's buttons text
    """
    WRITE_CONTACT = """Записать контакт"""
    SHOW_CONTACT = """Посмотреть контакт"""
    DELETE_CONTACT = """Удалить контакт"""
    DOWNLOAD_FILE = """Скачать файл"""
    SHOW_CONTACT_IN_ONE_LINE = """Показать контакт одной строкой"""
    SHOW_CONTACT_IN_LINES = """Показать контакт в несколько строк"""
    SHOW_CONTACT_CARD = """Показать карточку контакта"""
    SHOW_ALL_CONTACTS = """Посмотреть все контакты"""
    CHANGE_CONTACT = "Изменить контакт"
    CHANGE_FIRST_NAME = "Изменить имя"
    CHANGE_LAST_NAME = "Изменить фамилию"
    CHANGE_PHONE_NUMBER = "Изменить номер телефона"
    CHANGE_CONTACT_DESCRIPTION = "Изменить описание"
    BACK = """Назад"""
    PLACEHOLDER = """Выберите действие"""
    DOWNLOAD_TXT_FILE = "TXT"
    DOWNLOAD_CSV_FILE = "CSV"

