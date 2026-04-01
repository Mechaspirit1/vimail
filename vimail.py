#! /usr/bin/env python3

import smtplib
import mimetypes
import os
from email.message import EmailMessage
from getpass import getpass

#Esta função foi em grande parte escrita por IA e modificada afim de conformar com minhas necesidades, maiores testes precisam ser feitos ainda
def send_test_email(sender_email, sender_password, subject, recipient_email, message, service, attachment_path=None):
    msg = EmailMessage()
    msg["To"] = recipient_email
    msg["From"] = sender_email
    msg["Subject"] = subject

    msg.set_content(message)

    if attachment_path:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type = mime_type or "application/octet-stream"

        maintype, subtype = mime_type.split("/")

        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=maintype,
                subtype=subtype,
                filename=os.path.basename(attachment_path)
            )

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
    print("vimail 1.0.3")
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
            logic_subject = input("Type the standard message subject -> ")
            logic_message = input("Type the standard message template you wish to send -> ")

            #loop usado para enviar mais emails a partir do mesmo remetente e usando a mesma base
            while True:
                try:
                    logic_recipient = input("Type the address of the recipient -> ").lower()
                    if "@" not in logic_recipient:
                        print ("!!! Invalid address, please try again !!!")
                        continue

                    #Permite o envio de arquivos individuais. Checa se os arquivos existem andes de serem enviados
                    personal_attachment = input("Would you like to include a personal attachment with the message ? [y/n] -> ").lower()
                    logic_attachment = None
                    if personal_attachment == "y":
                        logic_attachment = input("Type the file path -> ")
                        if logic_attachment and not os.path.isfile(logic_attachment):
                            print("Attachment file not found.")
                            continue

                    unique_add = input("Type an addition to the message template -> ")
                    final_message = logic_message + "\n\n" + unique_add

                    send_test_email(logic_sender, logic_password, logic_subject, logic_recipient, final_message, logic_service, logic_attachment)
                    print("Transaction successful !")

                    action_repeat = input(("Would you like to send more emails ? [y/n] -> ")).lower()
                    if action_repeat == "y":
                        continue
                    elif action_repeat == "n":
                        print("Program terminated, exiting...")
                        return
                    else:
                        return
                    
                except smtplib.SMTPSenderRefused:
                    print("\nYour message exceeded your provider\'s file size limits. Please try again.")
                    continue

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
