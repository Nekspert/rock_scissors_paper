from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_keyboard: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard = True
)

button_1 = KeyboardButton(text=LEXICON_RU["rock"])
button_2 = KeyboardButton(text=LEXICON_RU["scissors"])
button_3 = KeyboardButton(text=LEXICON_RU["paper"])

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1],
        [button_2],
        [button_3]
    ],
    resize_keyboard=True
)

