import time
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from manager.config import CHANNEL_ID, COOLDOWN
from manager.bot_instance import bot, dp

user_states = {}
user_last_application_time = {}
user_last_start_time = {}

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in user_last_start_time and (current_time - user_last_start_time[user_id]) < COOLDOWN:
        remaining_time = int(COOLDOWN - (current_time - user_last_start_time[user_id]))
        await message.reply(f"⏳ Подождите {remaining_time} секунд перед повторным использованием /start.")
        return

    user_last_start_time[user_id] = current_time
    user_states[user_id] = "waiting_for_application"
    await message.reply(
        "Отправьте вашу заявку в формате:\n\n1. Ссылка на китайца (Профиль Steam)\n2. На сколько китаец по $? \n3. Ваш дискорд\n4. С какой вы тимы?"
    )

@dp.message()
async def application_handler(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in user_last_application_time and (current_time - user_last_application_time[user_id]) < COOLDOWN:
        remaining_time = int(COOLDOWN - (current_time - user_last_application_time[user_id]))
        await message.reply(f"⏳ Подождите {remaining_time} секунд перед отправкой новой заявки.")
        return

    if user_id not in user_states or user_states[user_id] != "waiting_for_application":
        await message.reply("🔄 Начните с команды /start")
        return

    user_states[user_id] = "application_sent"
    user_last_application_time[user_id] = current_time
    user_profile = f"tg://user?id={user_id}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Написать пользователю", url=user_profile)]
    ])

    lines = message.text.splitlines()
    if len(lines) < 4:
        await message.reply("⚠️ Неверный формат заявки. Попробуйте снова.")
        return

    text = (f"📩 Новая заявка\n\n"
            f"🔗 Ссылка на китайца: {lines[0]}\n"
            f"💰 На сколько китаец по $?: {lines[1]}\n"
            f"🎧 Ваш дискорд: {lines[2]}\n"
            f"👥 С какой вы тимы?: {lines[3]}\n\n"
            f"👤 Отправитель: {message.from_user.full_name}")

    await bot.send_message(CHANNEL_ID, text, reply_markup=keyboard)
    await message.reply("✅ Ваша заявка отправлена! Чтобы отправить новую, введите /start")
