import enum


class Messages(enum.StrEnum):
    INITIAL_MESSAGE = "Привет, это бот-телефонная книга.\nЯ могу хранить и показывать контакты.\nПожалуйста, " \
                      "выберите, что вы хотите сделать "

    LOG_IN_CONTACT = "Отлично!\nВведите фамилию, имя, телефон и описание в одну строчку через запятую\nНапример, " \
                     "Василий, Пупкин, +79999999999, домашний\nВажно: номер должен состоять из 11 цифр и иметь знак" \
                     " + в начале"

    LOG_OUT_FORMAT = "Отлично!\nПожалуйста, выберете нужный формат вывода"

    DELETE_CONTACT = "Отлично\nПожалуйста, введите номер телефона контакта, который хотите удалить"

    LOGGED_IN_SUCCESS = "Контакт успешно записан"

    LOGGED_IN_ERROR = "Ошибка!\nВозможно вы ввели не все данные или номер в неправильном формате\nПопробуйте еще раз"

    LOG_OUT_CONTACT = "Пожалуйста, введите фамилию и имя контакта\nНапример:\nПупкин, Василий"

    CONTACT_NOT_FOUND = "Введенный номер не найден"