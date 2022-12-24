import re

from aiogram import Router
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from keyboards.user_choice import get_log_in_out, get_log_out
from aiogram.filters.command import Command

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
        "Привет, это бот-телефонная книга\n"
        + "Я могу хранить и показывать контакты.\n"
        + "Пожалуйста, выберите, что вы хотите сделать:",
        reply_markup=get_log_in_out()
    )
    await state.set_state(FSMKbLevels.choose_operation_type)


@router.message(FSMKbLevels.choose_operation_type)
async def choose_operation(message: Message, state: FSMContext):
    if message.text == "Записать контакт":
        await message.reply(
            "Отлично!\n"
            + 'Введите фамилию, имя, телефон и описание в одну строчку через запятую\n'
            + 'Например, Василий, Пупкин, +79999999999, домашний',
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.log_in_operation)
    elif message.text == "Посмотреть контакт":
        await message.answer(
            "Отлично!\n"
            + "Пожалуйста, выберете нужный формат вывода",
            reply_markup=get_log_out()
        )
        await state.set_state(FSMKbLevels.log_out_operation)
    elif message.text == "Удалить контакт":
        await message.answer(
            "Отлично\n"
            + "Пожалуйста, введите номер телефона контакта, который хотите удалить",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.delete_contact)
    elif message.text == "Показать файл":
        await message.reply_document(FSInputFile('phone_book.txt'))


@router.message(FSMKbLevels.log_in_operation)
async def log_in_operation(message: Message, state: FSMContext):
    line = message.text
    try:
        line = message.text.split(', ')
        with open('phone_book.txt', 'a', encoding='utf-8') as file:
            file.write(f'{line[0]}; {line[1]}; {line[2]}; {line[3]}\n')
        await message.answer(
            "Контакт успешно записан",
            reply_markup=get_log_in_out()
        )
        await state.set_state(FSMKbLevels.choose_operation_type)
        print("Succes")
    except Exception:
        await message.answer(
            "Ошибка ввода, попробуйте еще раз"
        )


@router.message(FSMKbLevels.log_out_operation)
async def log_out_operation(message: Message, state: FSMContext):
    if message.text == "Показать контакт одной строкой":
        await message.answer(
            "Пожалуйста, введите фамилию и имя контакта\n"
            + "Например: Пупкин, Василий",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(FSMKbLevels.log_out_one_line)
    elif message.text == "Показать контакт в несколько строк":
        await message.answer(
            "Пожалуйста, введите имя и фамилию контакта\n"
            + "Например: Василий, Пупкин",
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
    try:
        msg = message.text.split(', ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.__contains__(msg[0]) and line.__contains__(msg[1]):
                    await message.reply(
                        line.replace('; ', ' '),
                        reply_markup=get_log_in_out()
                    )
            await state.set_state(FSMKbLevels.choose_operation_type)
    except Exception:
        await message.answer(
            "Ошибка ввода, попробуйте еще раз"
        )


@router.message(FSMKbLevels.log_out_lines)
async def logging_out_lines(message: Message, state: FSMContext):
    msg = message.text
    lst = []
    try:
        msg = message.text.split(', ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.__contains__(msg[0]) and line.__contains__(msg[1]):
                    line = line.split('; ')
                    for i in line:
                        lst.append(i)
            for lines in lst:
                await message.reply(
                    lines,
                    reply_markup=get_log_in_out()
                )
            await state.set_state(FSMKbLevels.choose_operation_type)
    except Exception:
        await message.answer(
            "Ошибка ввода, попробуйте еще раз"
        )


@router.message(FSMKbLevels.delete_contact)
async def delete_contact(message: Message, state: FSMContext):
    msg = message.text
    lst = []
    try:
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                lst.append(line.replace('\n', ''))
            print(lst)
            for i in lst:
                if i.__contains__(msg):
                    lst.remove(i)
            with open('phone_book.txt', 'w', encoding='utf-8') as F:
                if lst:
                    for i in lst:
                        if i is not None:
                            F.write(f"{i}\n")
                else:
                    F.write('')
            await message.reply(
                "Контакт успешно удален",
                reply_markup=get_log_in_out()
            )
            await state.set_state(FSMKbLevels.choose_operation_type)
    except Exception:
        await message.answer(
            "Ошибка ввода, попробуйте еще раз"
        )
