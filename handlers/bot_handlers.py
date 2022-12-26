from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from keyboards.user_choice import get_log_in_out, get_log_out
from aiogram.filters.command import Command
from logic import log_in, log_out, delete_contact
from bot_replies import constants

router = Router()


class FSMKbLevels(StatesGroup):
    choose_operation_type = State()
    delete_contact = State()
    get_file = State()
    log_in_operation = State()
    log_out_operation = State()
    log_out_one_line = State()
    log_out_lines = State()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        constants.Messages.INITIAL_MESSAGE,
        reply_markup=get_log_in_out()
    )
    await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(Command('back'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Возвращаемся в главное меню",
        reply_markup=get_log_in_out()
    )
    await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(FSMKbLevels.choose_operation_type)
async def choose_operation(message: Message, state: FSMContext):
    if message.text == "Записать контакт":
        await message.reply(
            constants.Messages.LOG_IN_CONTACT,
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.log_in_operation)
    elif message.text == "Посмотреть контакт":
        await message.answer(
            constants.Messages.LOG_OUT_FORMAT,
            reply_markup=get_log_out()
        )
        await state.set_state(FSMKbLevels.log_out_operation)
    elif message.text == "Удалить контакт":
        await message.answer(
            constants.Messages.DELETE_CONTACT,
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.delete_contact)
    elif message.text == "Показать файл":
        await message.reply_document(FSInputFile('phone_book.txt'))


@router.message(FSMKbLevels.log_in_operation)
async def log_in_operation(message: Message, state: FSMContext):
    line = message.text
    if log_in.log_in(line):
        await message.answer(
            constants.Messages.LOGGED_IN_SUCCESS,
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)
    else:
        await message.answer(
            constants.Messages.LOGGED_IN_ERROR
        )


@router.message(FSMKbLevels.log_out_operation)
async def log_out_operation(message: Message, state: FSMContext):
    if message.text == "Показать контакт одной строкой":
        await message.answer(
            constants.Messages.LOG_OUT_CONTACT,
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.log_out_one_line)
    elif message.text == "Показать контакт в несколько строк":
        await message.answer(
            constants.Messages.LOG_OUT_CONTACT,
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.log_out_lines)
    elif message.text == "Назад":
        await message.answer(
            "Идем назад",
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(FSMKbLevels.log_out_one_line)
async def logging_out_one_line(message: Message, state: FSMContext):
    msg = message.text
    lst = log_out.log_out_one_line(msg)
    if lst is not False:
        for line in lst:
            await message.reply(
                line,
                reply_markup=get_log_in_out()
            )
        await state.set_state(FSMKbLevels.choose_operation_type)
    else:
        await message.answer(
            constants.Messages.CONTACT_NOT_FOUND,
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(FSMKbLevels.log_out_lines)
async def logging_out_lines(message: Message, state: FSMContext):
    msg = message.text
    lst = log_out.log_out_lines(msg)
    if lst is not False:
        for lines in lst:
            await message.answer(
                lines,
                reply_markup=get_log_in_out()
            )
        await state.set_state(FSMKbLevels.choose_operation_type)
    else:
        await message.answer(
            constants.Messages.CONTACT_NOT_FOUND,
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(FSMKbLevels.delete_contact)
async def delete(message: Message, state: FSMContext):
    msg = message.text
    if delete_contact.delete_contact(msg):
        await message.reply(
            "Контакт успешно удален",
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)
    else:
        await message.answer(
            constants.Messages.CONTACT_NOT_FOUND,
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)
