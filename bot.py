import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import _random
from vk_api.utils import get_random_id


def main() -> None:
    vk_session = vk_api.VkApi(token='2e7f100c8864d944b2b7535df8a7a36cb5958ee3ce0e7a31605a20a3a122e4a8ffd6b6fb5162ccda4c3ce')
    long_poll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' +str(datetime.strftime(datetime.now(),"%H:%M:%S")))
            print('Текст сообщения : ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if(event.from_user and not (event.from_me)):
                if(response == "1"):
                    vk_session.method('messages.send', {'user_id':event.user_id, 'message': 'Приветствую вас. Я бот группы ММП-19. Меня написал ваш соратник Максим для автоматизации рутинных(или не очень) дел. Пока я умею мало, но со временем мой функционал будет расти. ', 'random_id': 0})
if __name__ == '__main__':
    main()