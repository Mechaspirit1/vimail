#! /usr/bin/env python3

import smtplib
from email.message import EmailMessage
from getpass import getpass

def send_test_email(sender_email, sender_password, subject, recipient_email, message, service):

    msg = EmailMessage()
    msg["To"] = recipient_email
    msg["From"] = sender_email
    msg["Subject"] = subject

    msg.set_content(message)

    with smtplib.SMTP(f"smtp.{service}.com", 587) as smtp:
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
    
    while True:
        try:
            logic_sender = input("Type the address of the sender -> ").lower()
            if "@" not in logic_sender:
                print("!!! Invalid address, please try again !!!")
                continue
            
            logic_service = logic_sender.split("@")[1].split(".")[0] #usado para identificar o provedor de email do remetente automaticamente

            if logic_service == "outlook" or logic_service == "hotmail":
                logic_service = "office365"

            #print(logic_service)
            
            logic_password = getpass("Type the app password of the sender -> ")
            logic_subject = input("Type the standard message subject - > ")
            logic_message = input("Type the standard message template you wish to send -> ")

            #loop usado para enviar mais emails a partir do mesmo remetente e usando a mesma base
            while True:
                logic_recipient = input("Type the address of the recipient -> ").lower()

                if "@" not in logic_recipient:
                    print ("!!! Invalid address, please try again !!!")
                    continue

                unique_add = input("Type an addition to the message template -> ")
                final_message = logic_message + "\n\n" + unique_add

                send_test_email(logic_sender, logic_password, logic_subject, logic_recipient, final_message, logic_service)
                print("Transaction successful !")

                action_repeat = input(("Would you like to send more emails ? [y/n] -> ")).lower()
                if action_repeat == "y":
                    continue
                elif action_repeat == "n":
                    print("Program terminated, exiting...")
                    return
                else:
                    return

        except ValueError:
            print("\nWrong value")
            continue
        except KeyboardInterrupt:
            print("\nProgram terminated. Exiting...")
            return
        except EOFError:
            print("\nForceful termination. Exiting...")
            return
        except IndexError:
            print("\nInvalid sender address, try again.")
            continue

if __name__ == "__main__":
    main()
