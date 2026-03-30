import smtplib
from email.message import EmailMessage

def send_test_email(sender_email, sender_password, subject, recipient_email, message):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    msg.set_content(message)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


def main():
    try:
        logic_sender = input("Type the address of the sender -> ").lower()
        logic_password = input("Type the app password of the sender -> ").lower()
        email_quantity = int(input("Type the ammount of emails to be sent -> "))
        logic_message = input("Type the standard message template you wish to send -> ")

        for i in range(email_quantity):
            logic_recipient = input("Type the address of the recipient -> ").lower()
            send_test_email(logic_sender, logic_password, "Email Automático", logic_recipient, logic_message)

    except ValueError:
        print("Wrong value")
        return

if __name__ == "__main__":
    main()
