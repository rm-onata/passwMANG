import os, sys
import platform




#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m"
BBlue = "\033[1;34m"
BYellow = "\033[1;33m"


system = platform.uname()[0]
if system == "Linux":
	os.system("if [ ! -f `which ccrypt` ]; then sudo apt-get install ccrypt || sudo yum install ccrypt; fi")
	os.system("clear")
else:
	print("Windows does not support")
	sys.exit()


print(BBlue+"""
                                            _                                               
                                           | |                                              
  _ __   __ _ ___ _____      _____  _ __ __| |  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ 
 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| | | | | | | | (_| | | | | (_| | (_| |  __/ |   
 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   
 | |                                                                         __/ |          
 |_|                                                                        |___/           

""")





first = input("For Decrypt[y] or Encrypt[n]: ")
if first == "y":
	os.system("ccdecrypt passwd")
	print(Green+"file is decrypted")
elif first == "n":
	os.system("ccencrypt passwd")
	print(Green+"\nfile is encrypted")
	print(BYellow+"thanks for using my-tools :)")
	sys.exit()
else:
	pass
	

print() 
ext = input("if you exit enter[y] : ")
if ext == "y":
	print(BYellow+"thanks for using my-tools :)")
	sys.exit()
print()



print(White+"<= If You Get Next Step Press Enter =>")
input("\n")


def passwords_manage():
	name = input("enter site name : ")
	username = input("enter username : ")
	password = input("enter password : ")

	with open("passwd", "a+") as f:
		f.write("site_name : "+name+"\n")
		f.write("username : "+username+"\n")
		f.write("password : "+password+"\n")
		f.write("\n-------------------------------------------\n")

	return Green+"added"



if __name__ == "__main__":
	passwords_manage()
	
	sal = input("Do You Encrypt 'passwd' file [y,n]? ")
	if sal=="y":
		os.system("ccencrypt passwd")
		print(Green+"file is encrypted")
	else:
	    print(BYellow+"good luck")