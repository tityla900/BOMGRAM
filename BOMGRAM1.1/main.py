import smtplib
import random
from email.mime.text import MIMEText
import webbrowser

print(   )
print ("ʙᴏᴍɢʀᴀᴍ1.1")





def read_email_addresses(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def read_passwords(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def read_random_message(filename):
    with open(filename, 'r') as file:
        messages = [line.strip() for line in file]
        return random.choice(messages)

def send_email(email_address, password, recipient_email, subject, message_text):
    try:
        smtp_server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtp_server.starttls()
        smtp_server.login(email_address, password)

        msg = MIMEText(message_text)
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = recipient_email

        smtp_server.sendmail(email_address, [recipient_email], msg.as_string())
        print(f'Письмо успешно отправлено от {email_address} на адрес {recipient_email}!')

    except smtplib.SMTPAuthenticationError:
        print(f'Ошибка аутентификации для адреса {email_address}. Проверьте правильность введенных данных.')

    finally:
        smtp_server.quit()

def main():
    # Чтение адресов из файла
    email_addresses_hotmail = read_email_addresses('hot.txt')
    email_addresses_gmail = read_email_addresses('gmail.txt')
    passwords_hotmail = read_passwords('pass.txt')
    passwords_gmail = read_passwords('gpass.txt')

    # Запрашиваем количество адресов для отправки
    while True:
        try:
            num_addresses = int(input("Введите количество адресов, с которых отправиться письмо: "))
            if num_addresses > len(email_addresses_hotmail) + len(email_addresses_gmail):
                print(f"Ошибка: количество адресов превышает доступное количество ({len(email_addresses_hotmail) + len(email_addresses_gmail)}). Пожалуйста, введите число еще раз.")
            else:
                break
        except ValueError:
            print("Ошибка: введите корректное число.")

    # Отображаем количество подключенных адресов
    print(f"Подключено {len(email_addresses_hotmail)} Hotmail адресов и {len(email_addresses_gmail)} Gmail адресов.")

    # Отправляем письмо на каждый адрес
    for i, (email_address, password) in enumerate(zip(email_addresses_hotmail + email_addresses_gmail, passwords_hotmail + passwords_gmail)):
        if i >= num_addresses:
            break
        recipient_email = ("abuse@telegram.org, DMCA@telegram.org, support@telegram.org")
        subject = input("Введите тему сообщения (Жалоба, Report и так далее): ")
        message_text = read_random_message('text.txt')
        send_email(email_address, password, recipient_email, subject, message_text)
        print(f"Отправлено {i + 1} писем.")

if __name__ == "__main__":
    while True:
        
        print("1 - Отправить Жалобу")
        print("2 - Перейти в канал Разработчика")
        print("3 - Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            main()
        elif choice == "3":
            print("Программа завершена.")
            break
        elif choice == "2":
            print("Переход в канал Разработчика...")
            webbrowser.open("https://t.me/SADLY_Prog")  # Открываем ссылку в браузере
        else:
            print("Некорректный выбор. Пожалуйста, введите 01, 02 или 03.")
