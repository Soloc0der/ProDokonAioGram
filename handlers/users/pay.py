from aiogram import types
from loader import dp, db
from aiogram.dispatcher.storage import FSMContext
from keyboards.default.menu import *
from states.main import ShopState



@dp.message_handler(text="Buyurtmalarim π", state="*")
async def bot_echo(message: types.Message, state: FSMContext):
    await ShopState.tolov.set()
    chizziq = "-"
    user_id = message.from_user.id
    zakaz_nomer = 0

    zakazlar = db.cheak_zakaz(user_id=user_id)
    if len(zakazlar) == 0:
        await message.answer("SIZDA HALI BUYURTMALAR MAVJUD EMAS π")
    else:
        for zakaz in zakazlar:
            zakaz_nomer += 1
            msg = ""
            address = (zakaz[5])[2:-21]

            if zakaz[9] == False:
                tolandi = "To'lanmaganβ"
            else:
                tolandi = "To'langan β"

        
            msg += f"<b>π¨{zakaz_nomer} - Buyurtma </b>π\n\nBuyurtma qilingan sana : {zakaz[8]} β³\n<i>Buyurtmalar ro'yxati</i> : π½<code>\n\n{zakaz[7]}</code>\n{chizziq * 15}\n"
            msg += f"Manzil: {address} π\n{chizziq * 17}\nTelefon raqam : {zakaz[6]} βοΈ\nUMUMIY HISOB - {zakaz[2]} πΈ\n\n Holati : {tolandi}"
            
            await message.answer(msg)
            await ShopState.category.set()

    