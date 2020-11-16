import amino
import time
import os
green=""
red=""
white=""
blue=""
db_1 = ("1")
db_2 = ("2")
db_3 = ("3")
db_4 = ("4")
db_0 = ("0")
db_clear = ("clear")
print ("Amino Tools Script")
time.sleep(1)
print ("By Bovonos")
time.sleep(1)
print ("github: https://github.com/Bovonos0")
time.sleep(1)
print ("amino: http://aminoapps.com/u/Anonymous-alMakyron-Loard")
print (" ")
time.sleep(1)
email=input("Type Your Email: ")
password=input("Type Your Password: ")
client=amino.Client()
client.login(email=email ,password=password)
comid=input("Type Forum ID: ")
time.sleep(1)
chatid=input("Chat Link: ")
chatid=client.get_from_code(chatid).objectId
print (" ")
print ("[1] Normal Message")
print ("[2] Transparent Message")
print ("[3] Delete Chat")
print ("[0] Exit")
user=input("choose: ")
if user== db_1:
	print ("[1] Send Normally")
	print ("[2] Send Spam")
	print ("[3] More")
	print ("[0] Exit")
	nos=input("choose: ")
	if nos== db_1:
		subclient = amino.SubClient(comId=comid , profile=client.profile)
		while True:
			massage=input("Type a Message: ")
			subclient.send_message(message=massage, chatId=chatid , messageType=0)
			if massage== db_clear:
				os.system("clear")
			
	if nos== db_2:
		subclient=amino.SubClient(comId=comid  ,profile=client.profile)
		mass = input("Type a Message: ")
		while True:
			try:
				subclient.send_message(message=mass ,chatId=chatid ,messageType=0)
			except:
				pass
	
	if nos== db_3:
		print ("[1] Send Normal Message but with a hit")
		print ("[2] Send Normal Message but can't Delete")
		print ("[0] Exit")
		hde = input("choose:")
		if hde== db_1:
			print ("[1] Send Normally")
			print ("[2] Send Spam")
			print ("[0] Exit")
			nsl =input("choose: ")
			if nsl== db_1:
				subclient=amino.SubClient(comId=comid ,profile=client.profile)
				while True:
					massage=input("Type Message: ")
					subclient.send_message(message=massage , chatId=chatid , messageType=1)
					if massage== db_clear:
						os.system("clear")
					
			if nsl== db_2:
				subclient=amino.SubClient(comId=comid ,profile=client.profile)
				mas=input("Type a Message: ")
				while True:
					try:
						subclient.send_message(message=mas ,chatId=chatid ,messageType=1)
					except:
						pass
					
			if nsl== db_0:
				os.system("exit")
				exit()
			
		
		if hde== db_2:
			print ("[1] Send Normally")
			print ("[2] Send Spam")
			nsa=input("choose: ")
			if nsa==db_1:
				subclient=amino.SubClient(comId=comid ,profile=client.profile)
				while True:
					massage=input("Type a Message: ")
					try:
						subclient.send_message(message=massage ,chatId=chatid ,messageType=55)
						if massage== db_clear:
							os.system("clear")
					except:
						pass
			
			if nsa==db_2:
				subclient=amino.SubClient(comId=comid ,profile=client.profile)
				massage=input("Type a Message: ")
				while True:
					try:
						subclient.send_message(message=massage ,chatId=chatid , messageType=55)
					except:
						pass
			if nsa== db_0:
				os.system("exit")
				exit()
			
		if hde== db_0:
			os.system("exit")
			exit()
		
		
		
		
	if nos== db_0:
		os.system("exit")
		exit()
if user== db_2:
	print ("[1] Send Normally")
	print ("[2] Send Spam")
	print ("[0] Exit")
	tnos =input("choose: ")
	if tnos== db_1:
		subclient=amino.SubClient(comId=comid ,profile=client.profile)
		while True:
			try:
				massage=input("Type Message: ")
				subclient.send_message(message=massage ,chatId=chatid , messageType=110)
				if massage== db_clear:
					os.system("clear")
			except:
				pass
	if tnos== db_2:
		subclient=amino.SubClient(comId=comid ,profile=client.profile)
		massage=input("Type a Message: ")
		while True:
			try:
				subclient.send_message(message=massage ,chatId=chatid , messageType=110)
			except:
				pass
	if tons== db_0:
		os.system("exit")
		exit()

if  user== db_3:
	userid=input("Type Host Link: ")
	userid=client.get_from_code(userid).objectId
	subclient=amino.SubClient(comId=comid ,profile=client.profile)
	subclient.kick(userId=userid ,chatId=chatid, allowRejoin=True)