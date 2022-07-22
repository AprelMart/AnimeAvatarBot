import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5581740196:AAH4NnuT8htWLgiWOKmWHDRHZFEediRAM4Q'
d = "https://kartinkin.net/uploads/posts/2021-07/1625524563_1-kartinkin-com-p-anime-dazai-anime-krasivo-1.jpg"
d1 = "https://i.pinimg.com/originals/2a/60/37/2a603771a699d8013087f7c5131fee6b.jpg"
ch = "https://i.pinimg.com/736x/12/11/88/12118836f214a9858793e5f1433e8e06.jpg"
ch1 = "https://i.pinimg.com/originals/43/bc/71/43bc71f39baad14e16735c113e883e0f.jpg"
f = "https://kartinkin.net/uploads/posts/2021-07/1625507551_19-kartinkin-com-p-fyodor-dostoevskii-anime-anime-krasivo-19.jpg"
f1 = "https://kartinkin.net/uploads/posts/2021-07/1625507551_19-kartinkin-com-p-fyodor-dostoevskii-anime-anime-krasivo-19.jpg"
s = "https://wallpaperscave.com/images/original/18/03-23/anime-one-punch-man-32624.jpg"
s2 = "https://phonoteka.org/uploads/posts/2021-06/1624351681_50-phonoteka_org-p-saitama-oboi-krasivo-54.png"
so = "http://pm1.narvii.com/6917/33359de7536c48b55db78851b306999236bd8919r1-600-649v2_uhq.jpg"
so1 = "https://i.pinimg.com/736x/a9/48/89/a94889479517de93daaea4768b67db65--hot-anime-anime-guys.jpg"
m = "https://printstorm.ru/wp-content/uploads/2021/03/11-04-19020328-9121-100086357-1.jpg"
m1 = "https://cdn.ananasposter.ru/image/cache/catalog/poster/anime/81/17266-1000x830.jpg"
la = "https://cdn.ananasposter.ru/image/cache/catalog/poster/anime/81/16806-1000x830.jpg"
la1 = "https://slovnet.ru/wp-content/uploads/2018/12/22-26.jpg"
l = "https://i.artfile.me/wallpaper/04-01-2013/1920x1080/anime-death-note-340953.jpg"
l2 = "https://static.zerochan.net/L.Lawliet.full.1631565.jpg"
m3 = "https://pbs.twimg.com/media/EZuf-F9U4AAukcl.jpg"
m2 = 'https://i.pinimg.com/originals/a8/4f/aa/a84faafe9192227ee94f87cc12a37a20.png'
mi = "https://images3.alphacoders.com/999/999424.png"
mi2 = "https://kartinkin.net/uploads/posts/2021-07/1625786197_52-kartinkin-com-p-midoriya-izuku-anime-anime-krasivo-55.jpg"
bak = "https://phonoteka.org/uploads/posts/2021-05/1622199408_25-phonoteka_org-p-moya-geroiskaya-akademiya-bakugo-art-krasi-25.jpg"
bak1 = "https://i.pinimg.com/736x/ec/4b/ce/ec4bceceddd1d752b0e50eeabf39d67f.jpg"
ai = "https://pm1.narvii.com/6827/86a787148d360e6d074accf1e7e2382187280df5v2_hq.jpg"
ai2 = "https://i.pinimg.com/originals/e9/a2/2c/e9a22c7b320750d98ff22dfbdd38651e.jpg"
marin = "https://i.ytimg.com/vi/OZNznVviEAQ/maxresdefault.jpg"
marin1 = "https://sun9-87.userapi.com/sun9-4/impg/w0Arie6GYeW84ShmoGH1sldtxIuj5IGDnPdj0w/nb0EzoiN1eA.jpg?size=453x604&quality=96&sign=67e5112018c5f300de40eca9f669827f&type=album"
mar = "https://pbs.twimg.com/media/FORvilQVEAIIe60.jpg"
mar3 = "https://www.free-wallpapers.su/data/media/3/big/anm8548.jpg"
mari = "https://i.pinimg.com/736x/35/9e/c4/359ec496b8674554e2d326e3228bf5ed.jpg"
marin3 = "https://i.pinimg.com/736x/a5/f0/53/a5f05323ff38e3fb2b58727a5f8b6bcd.jpg"
marin4 = "https://pbs.twimg.com/media/FNGxBNnXoAYGETu.jpg"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Здравствуйте!\nМы рады приветствовать вас в нашем Телеграмм боте\n.Этот бот поможет вам выбрать аватарку из вашего любимого аниме.")
    await message.answer(
        "СПИСОК АНИМЕ:\n- Великий из бродячих псов(/dog)\n- Ванпачмен(/onepunchman)\n- Тетрадь смерти(/deathnote)\n- Моя геройская академия(/heroacademy)\n- Эта фарфоровая кукла влюбилась(/porcelaindoll)\nНажмите на команду в скобчках")


@dp.message_handler(commands=['dog'])
async def bungou_stray_dogs(message: types.Message):
        await message.answer("ПЕРСОНАЖИ:\n- Дазай Осаму\n- Накахара Чуяа\n- Федор Достаевский")
        await bot.send_photo(message.chat.id, photo=d)
        await bot.send_photo(message.chat.id, photo=d1)
        await bot.send_photo(message.chat.id, photo=ch)
        await bot.send_photo(message.chat.id, photo=ch1)
        await bot.send_photo(message.chat.id, photo=f)


@dp.message_handler(commands=['onepunchman'])
async def one_punch_man(message: types.Message):
    await message.answer("ПЕРСОНАЖИ:\n- Сайтама\n- Соник\n- Мисс Буран")
    await bot.send_photo(message.chat.id, photo=s)
    await bot.send_photo(message.chat.id, photo=s2)
    await bot.send_photo(message.chat.id, photo=so)
    await bot.send_photo(message.chat.id, photo=so1)
    await bot.send_photo(message.chat.id, photo=m)
    await bot.send_photo(message.chat.id, photo=m1)


@dp.message_handler(commands=['deathnote'])
async def death_note(message: types.Message):
    await message.answer("ПЕРСОНАЖИ:\n- Лайт \n- L \n- Миса Миса")
    await bot.send_photo(message.chat.id, photo=la)
    await bot.send_photo(message.chat.id, photo=la1)
    await bot.send_photo(message.chat.id, photo=l)
    await bot.send_photo(message.chat.id, photo=l2)
    await bot.send_photo(message.chat.id, photo=m3)
    await bot.send_photo(message.chat.id, photo=m2)


@dp.message_handler(commands=['heroacademy'])
async def hero_academy(message: types.Message):
    await message.answer("ПЕРСОНАЖИ:\n- Мидория \n- Бакуго\n- Айзава")
    await bot.send_photo(message.chat.id, photo=mi)
    await bot.send_photo(message.chat.id, photo=mi2)
    await bot.send_photo(message.chat.id, photo=bak)
    await bot.send_photo(message.chat.id, photo=bak1)
    await bot.send_photo(message.chat.id, photo=ai)
    await bot.send_photo(message.chat.id, photo=ai2)


@dp.message_handler(commands=['porcelaindoll'])
async def porcelain_doll(message: types.Message):
    await message.answer("ПЕРСОНАЖИ:\n- Китагава Марин")
    await bot.send_photo(message.chat.id, photo=marin)
    await bot.send_photo(message.chat.id, photo=marin1)
    await bot.send_photo(message.chat.id, photo=marin3)
    await bot.send_photo(message.chat.id, photo=marin4)
    await bot.send_photo(message.chat.id, photo=mar)
    await bot.send_photo(message.chat.id, photo=mar3)
    await bot.send_photo(message.chat.id, photo=mari)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
