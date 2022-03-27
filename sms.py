import email
import smtplib
import ssl
from providers import PROVIDERS


def send_sms_via_email(
		number: str, 
		message: str, 
		provider: str, 
		sender_credentials: tuple, 
		subject: str = "sent using python", 
		smtp_server: str = "smtp.gmail.com",
		smtp_port: int = 465,
):
		sender_email, email_password = sender_credentials
		receive_email = f"{number}@{PROVIDERS.get(provider).get("sms")}"
		
		email_message = f"subject:{subject}\nTo:{receive_email}\n{message}"
		
		with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
				email.login(sender_email, email_password)
				email.send(sender_email, receive_email, email_message)sendmail()

def get_config():
		
		config = {}
		
		with open("config.json") as config:
				config = json.load()
				
		return config		

def main():
		number =
		message =
		provider = "Verizon"
						
		config =get_config()
		sender_credentials = (config.get("email"), config.get("password"))
						
		send_sms_via_email(number, message, provider, sender_credentials)
						
						
if__name__ == "__main__":
		main()				
		
		
