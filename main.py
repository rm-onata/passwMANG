from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from getpass import getpass
import os, sys, time, base64




#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m"
BBlue = "\033[1;34m"
BYellow = "\033[1;33m"



DB_PATH = os.path.join("src", "db_main")
DB_PATH_ENC = os.path.join("src", "db_main.enc")


if not os.path.exists("src"):
	os.mkdir("src")


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))



def encrypt():
	passwd0 = getpass(prompt="Input your password: ")
	passwd1 = getpass(prompt="Input your password(Repeat): ")

	if passwd0 != passwd1:
		print(Red+"Incorrect password!")
		sys.exit()
		

	salt = b"\xb6\x1d\xe8x_\xfd\x1c.O\x1d\xde\xd8K^\xd8\x07"
	key = derive_key(passwd1, salt)
	fernet = Fernet(key)

	try:
		os.remove(DB_PATH_ENC)
	except:
		pass

	with open(DB_PATH, "rb") as file:
		original = file.read()
	
	try:
		encrypted = fernet.encrypt(original)
	except:
		print(Red+"Signature did not match digest.")
		sys.exit()
	
	with open(DB_PATH_ENC, "wb") as encrypted_file:
		encrypted_file.write(encrypted)



def decrypt():
	passwd0 = getpass(prompt="Input your password: ")
	passwd1 = getpass(prompt="Input your password(Repeat): ")

	if passwd0 != passwd1:
		print(Red+"Incorrect password!")
		time.sleep(2)
		banner()
		

	salt = b"\xb6\x1d\xe8x_\xfd\x1c.O\x1d\xde\xd8K^\xd8\x07"
	key = derive_key(passwd1, salt)
	fernet = Fernet(key)

	with open(DB_PATH_ENC, "rb") as enc_file:
		encrypted = enc_file.read()
	
	try:
		decrypted = fernet.decrypt(encrypted)
	except:
		print(Red+"Signature did not match digest.")
		banner()
	
	with open(DB_PATH, "wb") as dec_file:
		dec_file.write(decrypted)
	
	os.remove(DB_PATH_ENC)







def banner():
	print(BBlue+"""
                                            _                                               
                                           | |                                              
  _ __   __ _ ___ _____      _____  _ __ __| |  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ |   
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
 | |                                                                         __/ |          
 |_|                                                                        |___/           
			     https://github.com/rm-onata/passwMANG



{g}[+]{w} 1-  Add new
{g}[+]{w} 2-  Search domain in Database
{g}[+]{w} 3-  Show your all Data
{g}[+]{w} 0-  Save & Exit
	""".format(g=Green,w=White))

	banr = input(BYellow+"_> "+White)
	if banr == "1":
		add_new()

	elif banr == "2":
		banner()		#coming soon

	elif banr == "3":
		show_db()

	elif banr == "0":
		if not os.path.exists(DB_PATH_ENC):
			encrypt()
			os.remove(DB_PATH)

		print(BYellow+"Good Luck :)")
		sys.exit()

	else:
		print(Red+"Invalid number.\n")
		time.sleep(2)
		banner()





def show_db():
	if os.path.exists(DB_PATH_ENC):
		decrypt()

	os.system("clear")
	with open(DB_PATH, "r") as f:
		rdr = f.readlines()
	
	for i in rdr:
		i = i.rstrip()
		print(i)

	input(BYellow+"\n\nPress Enter to Exit")
	banner()





def add_new():
	if os.path.exists(DB_PATH_ENC):
		decrypt()

	domain = input("[-] Domain => ")
	username = input("[-] username => ")
	password = input("[-] password => ")

	with open(DB_PATH, "a+") as f:
		f.write("site_name : "+domain+"\n")
		f.write("username : "+username+"\n")
		f.write("password : "+password+"\n")
		f.write("\n-------------------------------------------\n")

	print(Green+"added\n"+White)
	time.sleep(1)
	banner()



if __name__ == "__main__":
	banner()
