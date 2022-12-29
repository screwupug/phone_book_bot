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

class LoggerTextEnum(enum.StrEnum):
    """
    Logger's enum
    """
    STARTED_BOT = "started_bot"
    PUSHED_BACK = "pushed_back_button"
    PUSHED_BACK_IN_MAIN_MENU = "used_back_in_main_menu_command"
    PUSHED_WRITE_CONTACT = "pushed_write_contact_button"
    PUSHED_SHOW_CONTACT = "pushed_show_contact_button"
    PUSHED_CHANGE_CONTACT = "pushed_change_contact_button"
    PUSHED_DELETE_CONTACT = "pushed_delete_contact_button"
    PUSHED_DOWNLOAD_FILE = "pushed_download_button + downloaded file"
    HAS_WRITTEN_CONTACT = "has_written_new_contact"
    PUSHED_SHOW_CONTACT_ONE_LINE = "pushed_show_contact_in_one_line_button"
    PUSHED_SHOW_CONTACT_IN_LINES = "pushed_show_contact_in_lines_button"
    PUSHED_SHOW_CONTACT_CARD = "pushed_show_contact_card_button"
    PUSHED_SHOW_ALL_CONTACTS = "pushed_show_all_contacts_button"
    GET_CONTACT_ONE_LINE = "get_contact_in_one_line"
    GET_CONTACT_IN_LINES = "get_contact_in_lines"
    GET_CONTACT_CARD = "get_contact_card"
    PUSHED_CHANGE_FIRST_NAME = "pushed_change_first_name_button"
    PUSHED_CHANGE_LAST_NAME = "pushed_change_last_name_button"
    PUSHED_CHANGE_PHONE_NUMBER = "pushed_change_phone_number_button"
    PUSHED_CHANGE_DESCRIPTION = "pushed_change_description_button"
    HAS_CHANGED_FIRST_NAME = "has_changed_contact_first_name"
    HAS_CHANGED_LAST_NAME = "has_changed_contact_last_name"
    HAS_CHANGED_PHONE_NUMBER = "has_changed_contact_phone_number"
    HAS_CHANGED_DESCRIPTION = "has_changed_contact_description"
    HAS_DELETED_CONTACT = "has_deleted_contact"




