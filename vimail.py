#! /usr/bin/env python3

import smtplib
from email.message import EmailMessage
from getpass import getpass

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
    
    banner = r"""

              ███                             ███  ████ 
             ░░░                             ░░░  ░░███ 
 █████ █████ ████  █████████████    ██████   ████  ░███ 
░░███ ░░███ ░░███ ░░███░░███░░███  ░░░░░███ ░░███  ░███ 
 ░███  ░███  ░███  ░███ ░███ ░███   ███████  ░███  ░███ 
 ░░███ ███   ░███  ░███ ░███ ░███  ███░░███  ░███  ░███ 
  ░░█████    █████ █████░███ █████░░████████ █████ █████
   ░░░░░    ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░░ 
"""                                                        

    print(banner)
    print("vimail")
    print("\033]8;;https://github.com/Mechaspirit1\033\\A tool by Pablo Loschi (Mechaspirit1)\033]8;;\033\\")
    
    try:
        logic_sender = input("Type the address of the sender -> ").lower()
        logic_password = getpass("Type the app password of the sender -> ").lower()
        email_quantity = int(input("Type the ammount of emails to be sent -> "))
        logic_message = input("Type the standard message template you wish to send -> ")
        logic_subject = input("Type the standard message subject - > ")

        for i in range(email_quantity):
            logic_recipient = input("Type the address of the recipient -> ").lower()
            unique_add = input ("Type an addition to the message template -> ")

            final_message = logic_message + "\n" + unique_add

            send_test_email(logic_sender, logic_password, logic_subject, logic_recipient, final_message)
            print("Transaction successful !")


    except ValueError:
        print("\nWrong value")
        return
    except KeyboardInterrupt:
        print("\nProgram terminated. Exiting...")
        return
    except EOFError:
        print("\nForceful termination. Exiting...")
        return

if __name__ == "__main__":
    main()
