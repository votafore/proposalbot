from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import utils
from arch.SomeFile import users_manager

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove

router = Router()

invitation_msg: Message = None


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = users_manager.find_user_by_chat_id(message.chat.id)
    if user is None:
        kb = ReplyKeyboardBuilder()
        kb.button(text="Поделиться номером", request_contact=True)
        kb.button(text="Выход")
        kb.adjust(2)

        global invitation_msg
        invitation_msg = await message.answer(
            "Что бы вы получали уведомления нам необходим ваш номер телефона. "
            "Пожалуйста, поделитесь вашим контактом",
            reply_markup=kb.as_markup(resize_keyboard=True)
        )

    else:
        await message.answer(
            "уже зарегистрированы, тут список уведомлений"
        )

    await message.delete()


@router.message(F.text.lower() == "поделиться номером")
async def start_message_answer_share_phone(message: Message):
    await message.answer(
        "Супер!!! Вы зарегистрированы",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.delete()
    await invitation_msg.delete()


@router.message(F.text.lower() == "выход")
async def start_message_answer_exit(message: Message):
    await message.answer(
        "Пока - пока",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.delete()
    await invitation_msg.delete()


@router.message(Command("list"))
async def cmd_list(message: Message):
    # todo: обновить (вывести заново) список сообщений с заявками
    await message.answer(
        "тут типа список заявок"
    )

    await message.delete()


@router.message(Command("imadmin"))
async def cmd_show_admin_menu(message: Message):
    # todo: показать меню администратора
    await message.answer(
        "тут типа открывается меню админа"
    )

    await message.delete()


@router.message(Command("getlogs"))
async def cmd_get_logs(message: Message):
    # todo: сформировать файл с логами и выслать пользователю
    await message.answer(
        "тут типа файл с логом"
    )

    await message.delete()


@router.message()
async def handle_contact(message: Message):

    if message.contact is None:
        return

    saved = users_manager.save_user(
        message.chat.id,
        message.from_user.id,
        message.from_user.full_name,
        utils.get_phone_number(message.contact.phone_number)
    )

    if saved:
        await message.answer(
            f"{message.from_user.full_name}, приветствуем в нашем боте"
        )
        await message.delete()
        await invitation_msg.delete()

