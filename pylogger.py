#this is a PRogram That Log ever Single event with its details date time and locks into a simple directory 
#using a bat file
#github.com/ibrahimhaleemkhan
#OpenSOURCE FOR ALL
import os,datetime,time

def logoption(Event):
	os.system("lock.bat")
	f=open("Groove/log.txt" , "a")
	now = datetime.datetime.now()
	f.write("\nEvent Details \n ")
	f.write(Event)
	f.write("\n Event Logged at : \n")
	f.write(str(now))
	f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
	f.close()
	os.system("lock.bat")

def logclear():
 	#this Provides a way for clearing up the log and the default password is ihk

	CL=raw_input("Do you wanna clear the log (y/n) \n:")
	if CL== ("y" or "Y" or "Yes"):
		PD=raw_input("If you wanna clear the log, Enter the password \n :  ")
		if PD==("ihk" or "IHK" or "Mr.robot" or "YOLO" or "Ihk"):
		    print "Clearing the Log "
		    os.system("lock.bat")
		    f=open("Groove/log.txt", "w")
		    f.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		    f.write("LOG CLEARED !! AT -")
		    now = datetime.datetime.now()
		    f.write(str(now))
		    f.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		    f.close()
		    os.system("lock.bat")
		    print "LOG CLEARED"
		                  
		        
		else:
		    print "PASSWORD INCORRECT "
		    print "This Event has also being logged"
		    os.system("lock.bat")
		    f=open("log.txt", "w")
		    f.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		    f.write("UNAUTHORISED ENTRY - Invalid password !! AT -")
		    now = datetime.datetime.now()
		    f.write(str(now))
		    f.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		    f.close()
		    os.system("lock.bat")
		        
	else:
		print "\n The Log Has Been Maintained.\n "


def main():
	os.system("lock.bat")
	f=open("Groove/log.txt" , "a")
	now = datetime.datetime.now()
	f.write("\nEvent Details \n ")
	f.write("Program Executed or last used at")
	f.write("\n -------------------------------------------\n")
	f.write(str(now))
	f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
	f.close()
	os.system("lock.bat")

	print "\t \t Welcome To The ---- | PyLogger |-----\n "
	print "\t \t #github.com/ibrahimhaleemkhan"
	print "Support For Windows Only"
	print "\t Program That logs the event details, provided to the function\n  "
	print "------------------------------------------------------------------------ \n \n"
	logclear()
	Event = raw_input("\tEnter The event Details or \t \n use the Function for your own values(being parsed) \n :")
	#pass your event details from the function below
	#
	logoption(Event)

 	

    
while True:

	main()
	print "--------------- | YOUR EVENT WAS SUCCESFULLY LOGGED |--------------"
	print "Do you want to see the log"
	logpass = raw_input("Enter the password")
	if logpass== ("view" or "View" or "VIEW"):
		print "Showing in Console Log"
		time.sleep(2)
		os.system("lock.bat")
		f=open("Groove/log.txt" , "ab+")
		showlog =f.read()
		f.close()
		os.system("lock.bat")
		print "LOG STARTS---------------------------------------------- \n "
		
		print showlog
		print "LOG ENDS---------------------------------------------- \n "
		print "Saw the Log ? press any key to continue \n :"
		
		time.sleep(2)
		rr =raw_input(" \t :::: Waiting .......... ")
	else:
		print "Wrong Password, NO Peaking"
	
	

	
	