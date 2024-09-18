def send_email(message, recipient, sender="university.help@gmail.com"):

    var_ = ('.com', '.ru', '.net')

    if recipient.find('@') == -1 or not recipient.endswith(var_) or \
       sender.find('@') == -1 or not sender.endswith(var_):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

# 1-ое условие
print('1-е условие')
send_email('Привет', "univer.help@gmail.ru", "adallar@gmail")
send_email('Привет', "univer.helpgmail.ru", "adallar@gmail.com")
send_email('Привет', "univer.help@gmail", "adallar@gmail.com")
send_email('Привет', "univer.help@gmail.ru", "adallargmail.com")
send_email('Привет', "univer.helpgmail", "adallar@gmail.com")
# 2-ое условие
print()
print('2-ое условие')
send_email('Как дела?', "Villy@gmail.net", "Villy@gmail.net")
# 3-е условие
print()
print('3-е условие')
send_email('Как дела?', "Villy@gmail.net")
# 4-ое условие
print()
print('4-ое условие')
send_email('Как дела?', "Villy@gmail.net", "crazy@yandex.ru")







