from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os, sys, time, base64




#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m"
BBlue = "\033[1;34m"
BYellow = "\033[1;33m"




def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

password = "PASSWORD"

salt = b"\xb6\x1d\xe8x_\xfd\x1c.O\x1d\xde\xd8K^\xd8\x07"
key = derive_key(password, salt)

fernet = Fernet(key)


def encrypt():
	try:
		os.remove("./src/db_main.enc")
	except:
		pass

	with open("./src/db_main", "rb") as file:
		original = file.read()
		
	encrypted = fernet.encrypt(original)
	
	with open("./src/db_main.enc", "wb") as encrypted_file:
		encrypted_file.write(encrypted)



def decrypt():
	with open("./src/db_main.enc", "rb") as enc_file:
		encrypted = enc_file.read()
	
	decrypted = fernet.decrypt(encrypted)
	
	with open("./src/db_main", "wb") as dec_file:
		dec_file.write(decrypted)
	
	os.remove("./src/db_main.enc")







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
		if not os.path.exists("./src/db_main.enc"):
			encrypt()
			os.remove("./src/db_main")

		print(BYellow+"Good Luck :)")
		sys.exit()

	else:
		print(Red+"Invalid number.\n")
		time.sleep(2)
		banner()





def show_db():
	if os.path.exists("./src/db_main.enc"):
		decrypt()

	os.system("clear")
	with open("./src/db_main", "r") as f:
		rdr = f.readlines()
	
	for i in rdr:
		i = i.rstrip()
		print(i)

	input(BYellow+"\n\nPress Enter to Exit")
	banner()





def add_new():
	if os.path.exists("./src/db_main.enc"):
		decrypt()

	domain = input("[-] Domain => ")
	username = input("[-] username => ")
	password = input("[-] password => ")

	with open("./src/db_main", "a+") as f:
		f.write("site_name : "+domain+"\n")
		f.write("username : "+username+"\n")
		f.write("password : "+password+"\n")
		f.write("\n-------------------------------------------\n")

	print(Green+"added\n"+White)
	time.sleep(1)
	banner()



if __name__ == "__main__":
	banner()
