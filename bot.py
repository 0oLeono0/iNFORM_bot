from vkbottle import Keyboard, Text, BaseStateGroup, EMPTY_KEYBOARD
from vkbottle.bot import Bot, Message
import os

bot = Bot(os.environ.get('TOKEN'))

class States(BaseStateGroup):
    CHOOSE_STATE = 0
    ANYTHINGELSE_STAGE = 1
    STOP_STATE = 2

@bot.on.message(text="Начать")
async def start(message: Message):
    await message.answer("Привет! Это бот iNFORM. Я помогу" + 
                        " тебе не запутаться в отделах проекта" + 
                        " и заполнить форму регистрации. Для начала" +
                        " выбери отдел, в который хочешь отправить заявку.", keyboard=EMPTY_KEYBOARD)
    await bot.state_dispenser.set(message.peer_id, States.CHOOSE_STATE)
    await choosewishely(message.peer_id)

async def choosewishely(peer_id):
    await bot.state_dispenser.set(peer_id, States.CHOOSE_STATE)
    keyboard = Keyboard(one_time = True, inline=False)
    keyboard.add(Text("Сёрферы"))
    keyboard.add(Text("Медиа"))
    keyboard.row()
    keyboard.add(Text("Дизайн"))
    keyboard.add(Text("Пиар"))
    keyboard.row()
    keyboard.add(Text("Модерация"))
    keyboard.add(Text("Консультация"))
    keyboard.row()
    keyboard.add(Text("Собеседники"))
    keyboard.add(Text("Ивент"))
    await bot.api.messages.send(peer_id=peer_id,message="В какой отдел ты хочешь?", keyboard=keyboard.get_json(), random_id=0)

@bot.on.message(state=States.CHOOSE_STATE, text="Модерация")
async def moder(message: Message):
    await message.answer("Отдел Модерации работает с организаторами проекта iNFORM. Модераторы выстраивают позиционирование нашей команды: следят за соблюдением правил и регламента, а также модерируют контент в социальных сетях проекта. Перед началом активной фазы сотрудники отдела проводят доскональную проверку всех социальных сетей каждого организатора проекта.\n\nПодать заявку в отдел можно тут:\nhttps://forms.gle/mxrAfhdd2pHByFhJA")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Собеседники")
async def sobes(message: Message):
    await message.answer("Люди, которые отвечают за беседы факультетов и беседы по интересам. Они знают все об университете и котиках. В обязанности собеседников входит общение с первокурсниками в беседах, модерирование чатов и готовность ответить на любой вопрос, касающийся обучения и не только.\n\nПодать заявку в отдел можно тут:\nhttps://docs.google.com/forms/d/e/1FAIpQLSczfwjSNSeRCkyx97gYXpO-EsmAe38qpTyjfZ-pJPOXcJ-QTg/viewform")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Дизайн")
async def dezign(message: Message):
    await message.answer("Разрабатывают фирменный стиль и айдентику, а также мерч для мероприятий и организаторов проекта. Во время работы у дизайнеров есть возможность не только отточить свои навыки, создавая шаблонные посты, но и проявить креативность, генерируя развлекательный контент.\n\nПодать заявку в отдел можно тут:\nhttps://docs.google.com/forms/d/1E9CphfXuy40e3cRcdPH2ElaYBzNiM11hBX3nXxfu6jc/edit")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Пиар")
async def omir(message: Message):
    await message.answer("Отдел ведет интернет-ресурсы и занимается продвижением проекта в социальных сетях. Одной из главных задач является повышение узнаваемости проекта не только в стенах университета, но и за его пределами. Где ты мог(ла) познакомиться с ними? В группах iNFORM, Абитуриенты СПбГУТ, НеНочная во ВКонтакте, а также на платформе Яндекс.Дзен.\n\nПодать заявку в отдел можно тут:\nhttps://forms.gle/Vutfi6uSPJD2jGMQA")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Консультация")
async def cons(message: Message):
    await message.answer("Кто встречает тебя в приемной комиссии и отвечает тебе в социальных сетях? Конечно же, консультанты. Их задача – помочь абитуриентам с выбором факультета или направления обучения и объяснить все страшное простыми словами. Консультанты знают ответы на все: от стоимости проезда в метро до всех нюансов подачи документов.\n\nПодать заявку в отдел можно тут:\nhttps://forms.gle/5WFJubvZobRtdyVu9")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Сёрферы")
async def surf(message: Message):
    await message.answer("Первые из студентов, с кем ты общаешься, когда поступаешь в наш университет. Серферы занимаются мониторингом приказов о поступлении и поиском новоиспеченных первокурсников в социальных сетях. Порой это бывает непросто, ведь никогда не знаешь, кто скрывается за аватаркой с котиком. После нахождения нужного человека серфер направляет его в беседу факультета.\n\nПодать заявку в отдел можно тут:\nhttps://forms.gle/ArGa93x2pCTPU42AA")
    await anythingElse(message.peer_id)
    
@bot.on.message(state=States.CHOOSE_STATE, text="Медиа")
async def media(message: Message):
    await message.answer("Снимают фото и видео, придумывают идеи и пишут раскадровки, обрабатывают и анимируют, все это делает медиа-отдел для социальных сетей проекта и его внешнего представления на других площадках. Увидеть работы можно в группах iNFORM, Абитуриенты и НеНочная.\n\nПодать заявку в отдел можно тут:\nhttps://docs.google.com/forms/d/e/1FAIpQLSe8nerUPgnN3yvFIAIioaUvmPzjTyezU3lxxAQvKYDPjRChFw/viewform?usp=sf_link")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Ивент")
async def event(message: Message):
    await message.answer("Ha Ивент-отделе лежит ответственность представить первокурсникам другую сторону студенческой жизни. Они проводят первое мероприятие для поступивших ребят,где знакомят их друг с другом и с университетом. Но не стоит думать, что на этом их работа заканчивается Во время пассивной фазы Ивент-отдел организует мероприятия, направленные на командообразование, развитие проекта и организаторов.\n\nПодать заявку в отдел можно тут:\nhttps://forms.gle/YoaUsoB8LMekL5N96")
    await anythingElse(message.peer_id)

async def anythingElse(peer_id):
    await bot.state_dispenser.set(peer_id, States.ANYTHINGELSE_STAGE)
    keyboard = Keyboard(one_time=True, inline=False)
    keyboard.add(Text("Да"))
    keyboard.add(Text("Нет"))
    await bot.api.messages.send(peer_id=peer_id,message="Желаешь вступить куда-нибудь еще?", keyboard=keyboard.get_json(), random_id=0)

@bot.on.message(state=States.ANYTHINGELSE_STAGE, text="Да")
async def yos(message: Message):
    await choosewishely(message.peer_id)

@bot.on.message(state=States.ANYTHINGELSE_STAGE, text="Нет")
async def no(message: Message):
    await message.answer("Спасибо за заявку! Ждём тебя на следующих этапах отбора 🤍\n\n P.s.: чтобы запустить меня заново,напиши «Начать»")
    # await bot.state_dispenser.set(message.peer_id, state=None)
    return
    

if __name__ == '__main__':
    bot.run_forever()
