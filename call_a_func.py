import re

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    if sender == 'university.help@gmail.com':
        print()
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif re.search(r'[^com|^net|^ru]$',sender):
        print()
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print()
        print("Нельзя отправить письмо самому себе!")
    elif re.search(r'urban', recipient):
        print()
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
