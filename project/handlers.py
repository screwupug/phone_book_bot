from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.handlers import ErrorHandler
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.filters.command import Command
from project.constants import BotTextEnum, UserTextEnum, LoggerTextEnum
from project import logic
from project.keyboards import BACK_KEYBOARD, CHOOSE_OPERATION_KEYBOARD, CHOOSE_CONTACT_VIEW_KEYBOARD, \
    choose_contact_for_operation, CHOOSE_CHANGE_CONTACT_OPTION_KEYBOARD
import os

router = Router()
line_to_change = ''


class UserState(StatesGroup):
    """
    User's states
    """
    CHOOSE_OPERATION_TYPE = State()
    DELETE_CONTACT = State()
    WRITE_CONTACT_OPERATION = State()
    SHOW_CONTACT_OPERATION = State()
    SHOW_CONTACT_ONE_LINE = State()
    SHOW_CONTACT_CARD = State()
    SHOW_CONTACT_IN_LINES = State()
    SHOW_ALL_CONTACTS = State()
    CHANGE_CONTACT = State()
    CHOOSING_CHANGE_OPTION = State()
    CHANGE_FIRST_NAME = State()
    CHANGE_LAST_NAME = State()
    CHANGE_PHONE_NUMBER = State()
    CHANGE_CONTACT_DESCRIPTION = State()


@router.errors()
class RouterErrorHandler(ErrorHandler):
    async def handle(self):
        """
        Обработчик ошибок в хэндлерах бота
        """
        logic.logger('error', str(self.event.exception))
        await self.bot.send_message(
            chat_id=self.event.update.message.chat.id,
            text=BotTextEnum.ERROR_TEXT.format(self.event.exception),
            reply_to_message_id=self.event.update.message.message_id,
            reply_markup=CHOOSE_OPERATION_KEYBOARD
        )
        await self.data['state'].set_state(UserState.CHOOSE_OPERATION_TYPE)


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    """
    Start command handler
    """
    await message.answer(
        BotTextEnum.INITIAL_MESSAGE,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.STARTED_BOT)


@router.message(Command('back'))
async def cmd_back(message: Message, state: FSMContext):
    """
    Back command handler
    """
    await message.answer(
        BotTextEnum.BACK_IN_MAIN_MENU,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_BACK_IN_MAIN_MENU)


@router.message(Text(text=UserTextEnum.BACK))
async def cmd_back(message: Message, state: FSMContext):
    """
    Back button handler
    """
    await message.answer(
        BotTextEnum.GO_BACK,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_BACK)


@router.message(
    UserState.CHOOSE_OPERATION_TYPE,
    Text(text=UserTextEnum.WRITE_CONTACT)
)
async def choose_write_operation(message: Message, state: FSMContext):
    """
    Log in contact button handler
    """
    await message.reply(
        BotTextEnum.LOG_IN_CONTACT,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.WRITE_CONTACT_OPERATION)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_WRITE_CONTACT)


@router.message(
    UserState.CHOOSE_OPERATION_TYPE,
    Text(text=UserTextEnum.SHOW_CONTACT)
)
async def choose_show_operation(message: Message, state: FSMContext):
    """
    SHOW_CONTACT button handler
    """
    assert os.path.exists(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    assert os.path.getsize(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    await message.reply(
        BotTextEnum.LOG_OUT_FORMAT,
        reply_markup=CHOOSE_CONTACT_VIEW_KEYBOARD
    )
    await state.set_state(UserState.SHOW_CONTACT_OPERATION)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_SHOW_CONTACT)


@router.message(
    UserState.CHOOSE_OPERATION_TYPE,
    Text(text=UserTextEnum.CHANGE_CONTACT)
)
async def choose_change_operation(message: Message, state: FSMContext):
    """
    CHANGE_CONTACT button handler
    """
    assert os.path.exists(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    assert os.path.getsize(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    await message.reply(
        BotTextEnum.CHOOSE_CONTACT,
        reply_markup=choose_contact_for_operation(message.chat.username)
    )
    await state.set_state(UserState.CHANGE_CONTACT)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_CHANGE_CONTACT)


@router.message(
    UserState.CHOOSE_OPERATION_TYPE,
    Text(text=UserTextEnum.DELETE_CONTACT)
)
async def choose_delete_operation(message: Message, state: FSMContext):
    """
    DELETE_CONTACT button handler
    """
    assert os.path.exists(logic.get_path_txt(message.chat.username)), \
        "В книге нет ни одного контакта"
    assert os.path.getsize(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    await message.answer(
        BotTextEnum.DELETE_CONTACT,
        reply_markup=choose_contact_for_operation(message.chat.username)
    )
    await state.set_state(UserState.DELETE_CONTACT)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_DELETE_CONTACT)


@router.message(UserState.WRITE_CONTACT_OPERATION)
async def write_operation(message: Message, state: FSMContext):
    """
    Handling WRITE_CONTACT_OPERATION state
    """
    logic.write_line(
        logic.checked_handle_line(message.text),
        message.chat.username)
    await message.reply(
        BotTextEnum.LOGGED_IN_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_WRITTEN_CONTACT)


@router.message(
    UserState.SHOW_CONTACT_OPERATION,
    Text(text=UserTextEnum.SHOW_CONTACT_IN_ONE_LINE)
)
async def show_contact_one_line(message: Message, state: FSMContext):
    """
    Handling command "Show contact in one line"
    """
    await message.reply(
        BotTextEnum.LOG_OUT_CONTACT,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.SHOW_CONTACT_ONE_LINE)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_SHOW_CONTACT_ONE_LINE)



@router.message(
    UserState.SHOW_CONTACT_OPERATION,
    Text(text=UserTextEnum.SHOW_CONTACT_IN_LINES)
)
async def show_contact_in_lines(message: Message, state: FSMContext):
    """
    Handling command "Show contact in lines"
    """
    await message.reply(
        BotTextEnum.LOG_OUT_CONTACT,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.SHOW_CONTACT_IN_LINES)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_SHOW_CONTACT_IN_LINES)


@router.message(
    UserState.SHOW_CONTACT_OPERATION,
    Text(text=UserTextEnum.SHOW_CONTACT_CARD)
)
async def show_contact_card(message: Message, state: FSMContext):
    """
    Handling command "Show contact card"
    """
    await message.reply(
        BotTextEnum.LOG_OUT_CONTACT,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.SHOW_CONTACT_CARD)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_SHOW_CONTACT_CARD)


@router.message(
    UserState.SHOW_CONTACT_OPERATION,
    Text(text=UserTextEnum.SHOW_ALL_CONTACTS)
)
async def show_all_contacts(message: Message, state: FSMContext):
    """
    Handling command "Show all contacts"
    """
    await message.reply(
        BotTextEnum.CHOOSE_CONTACT,
        reply_markup=choose_contact_for_operation(message.chat.username)
    )
    await state.set_state(UserState.SHOW_ALL_CONTACTS)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_SHOW_ALL_CONTACTS)


@router.message(
    UserState.SHOW_CONTACT_ONE_LINE
)
async def show_contact_in_one_line_final(message: Message, state: FSMContext):
    """
    Handling SHOW_CONTACT_ONE_LINE state
    """
    await message.reply(
        text=', '.join(logic.show_line(
            message.text,
            message.chat.username)),
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.GET_CONTACT_ONE_LINE)


@router.message(
    UserState.SHOW_CONTACT_IN_LINES
)
async def show_contact_in_lines_final(message: Message, state: FSMContext):
    """
    Handling SHOW_CONTACT_IN_LINES state
    """
    line = logic.show_line(
        message.text,
        message.chat.username
    )
    for item in line:
        await message.answer(
            item,
            reply_markup=CHOOSE_OPERATION_KEYBOARD
        )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.GET_CONTACT_IN_LINES)


@router.message(
    UserState.SHOW_CONTACT_CARD
)
async def show_contact_card_final(message: Message, state: FSMContext):
    """
    Handling SHOW_CONTACT_CARD state
    """
    first_name, last_name, phone_number, description = logic.show_line(
        message.text,
        message.chat.username
    )
    await message.answer_contact(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        vcard=description,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.GET_CONTACT_CARD)


@router.message(
    UserState.CHANGE_CONTACT,
)
async def choose_contact_to_change(message: Message, state: FSMContext):
    """
    Choosing contact to change
    """
    global line_to_change
    line_to_change = message.text
    print(line_to_change)
    await message.reply(
        BotTextEnum.CHOOSE_FIELD_TO_CHANGE,
        reply_markup=CHOOSE_CHANGE_CONTACT_OPTION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSING_CHANGE_OPTION)


@router.message(
    UserState.CHOOSING_CHANGE_OPTION,
    Text(text=UserTextEnum.CHANGE_FIRST_NAME)
)
async def choose_change_first_name(message: Message, state: FSMContext):
    """
    Handling CHANGE_FIRST_NAME command
    """
    await message.reply(
        BotTextEnum.TYPE_NEW_VALUE,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.CHANGE_FIRST_NAME)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_CHANGE_FIRST_NAME)


@router.message(
    UserState.CHOOSING_CHANGE_OPTION,
    Text(text=UserTextEnum.CHANGE_LAST_NAME)
)
async def choose_change_last_name(message: Message, state: FSMContext):
    """
    Handling CHANGE_LAST_NAME command
    """
    await message.reply(
        BotTextEnum.TYPE_NEW_VALUE,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.CHANGE_LAST_NAME)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_CHANGE_LAST_NAME)


@router.message(
    UserState.CHOOSING_CHANGE_OPTION,
    Text(text=UserTextEnum.CHANGE_PHONE_NUMBER)
)
async def choose_change_phone_number(message: Message, state: FSMContext):
    """
    Handling CHANGE_PHONE_NUMBER command
    """
    await message.reply(
        BotTextEnum.TYPE_NEW_VALUE,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.CHANGE_PHONE_NUMBER)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_CHANGE_PHONE_NUMBER)


@router.message(
    UserState.CHOOSING_CHANGE_OPTION,
    Text(text=UserTextEnum.CHANGE_CONTACT_DESCRIPTION)
)
async def choose_change_contact_description(message: Message, state: FSMContext):
    """
    Handling CHANGE_CONTACT_DESCRIPTION command
    """
    await message.reply(
        BotTextEnum.TYPE_NEW_VALUE,
        reply_markup=BACK_KEYBOARD
    )
    await state.set_state(UserState.CHANGE_CONTACT_DESCRIPTION)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_CHANGE_DESCRIPTION)


@router.message(
    UserState.CHANGE_FIRST_NAME,
)
async def choose_change_first_name_final(message: Message, state: FSMContext):
    """
    Handling CHANGE_FIRST_NAME state
    """
    logic.change_contact(
        line_to_change,
        message.chat.username,
        0,
        message.text
    )
    await message.answer(
        BotTextEnum.CHANGED_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_CHANGED_FIRST_NAME)


@router.message(
    UserState.CHANGE_LAST_NAME,
)
async def choose_change_last_name_final(message: Message, state: FSMContext):
    """
    Handling CHANGE_LAST_NAME state
    """
    logic.change_contact(
        line_to_change,
        message.chat.username,
        1,
        message.text
    )
    await message.answer(
        BotTextEnum.CHANGED_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_CHANGED_LAST_NAME)


@router.message(
    UserState.CHANGE_PHONE_NUMBER,
)
async def choose_change_phone_number_final(message: Message, state: FSMContext):
    """
    Handling CHANGE_PHONE_NUMBER state
    """
    logic.change_contact(
        line_to_change,
        message.chat.username,
        2,
        message.text
    )
    await message.answer(
        BotTextEnum.CHANGED_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_CHANGED_PHONE_NUMBER)


@router.message(
    UserState.CHANGE_CONTACT_DESCRIPTION,
)
async def choose_change_contact_description_final(message: Message, state: FSMContext):
    """
    Handling CHANGE_CONTACT_DESCRIPTION state
    """
    logic.change_contact(
        line_to_change,
        message.chat.username,
        3,
        message.text
    )
    await message.answer(
        BotTextEnum.CHANGED_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_CHANGED_DESCRIPTION)


@router.message(
    UserState.DELETE_CONTACT
)
async def delete_contact(message: Message, state: FSMContext):
    """
    Handling DELETE_CONTACT state
    """
    logic.delete_contact(message.text, message.chat.username)
    await message.answer(
        BotTextEnum.DELETED_SUCCESS,
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.HAS_DELETED_CONTACT)


@router.message(
    UserState.CHOOSE_OPERATION_TYPE,
    Text(text=UserTextEnum.DOWNLOAD_FILE)
)
async def get_file(message: Message, state: FSMContext):
    """
    Handling "Download file" command
    """
    assert os.path.exists(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    assert os.path.getsize(logic.get_path_txt(message.chat.username)), \
        "Телефонная книга пуста, запишите хотя бы один контакт"
    await message.answer_document(
        FSInputFile(logic.get_path_txt(message.chat.username)),
        reply_markup=CHOOSE_OPERATION_KEYBOARD
    )
    await state.set_state(UserState.CHOOSE_OPERATION_TYPE)
    logic.logger(message.chat.username, LoggerTextEnum.PUSHED_DOWNLOAD_FILE)

