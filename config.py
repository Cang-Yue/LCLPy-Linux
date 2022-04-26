# Modules
import os
import configparser

#Variables
HOME=os.getenv("HOME")

# Check if "Options.ini" exists or not.
def ConfigExist():
	if os.path.isfile(os.getenv("HOME")+"/.lcl/Options.ini") is False:
		ConfigCreate()
		
# Create a "Options.ini" file.	
def ConfigCreate():
	config = configparser.ConfigParser()
	config['Minecraft'] = {'1.7 Directory': HOME+"/.minecraft",
						   '1.8 Directory': HOME+"/.minecraft",
						   '1.12 Directory': HOME+"/.minecraft",
						   '1.16 Directory': HOME+"/.minecraft",
						   '1.17 Directory': HOME+"/.minecraft",
						   '1.18.1 Directory': HOME+"/.minecraft",
						   '1.18.2 Directory': HOME+"/.minecraft"
						   }
	config['Java'] = {'Arguments': "-Xms3G -Xmx3G -Xmn1G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M",
					  '1.7 Java': HOME+"/.lunarclient/jre/1.7/zulu16.30.15-ca-fx-jdk16.0.1-linux_x64/bin/java",
					  '1.8 Java': HOME+"/.lunarclient/jre/1.8/zulu16.30.15-ca-fx-jdk16.0.1-linux_x64/bin/java",
					  '1.12 Java': HOME+"/.lunarclient/jre/1.12/zulu16.30.15-ca-fx-jdk16.0.1-linux_x64/bin/java",
					  '1.16 Java': HOME+"/.lunarclient/jre/1.16/zulu16.30.15-ca-fx-jdk16.0.1-linux_x64/bin/java",
					  '1.17 Java': HOME+"/.lunarclient/jre/1.17/zulu17.30.15-ca-fx-jre17.0.1-linux_x64/bin/java",
					  '1.18.1 Java': HOME+"/.lunarclient/jre/1.18.1/zulu17.30.15-ca-fx-jre17.0.1-linux_x64/bin/java",
					  '1.18.2 Java': HOME+"/.lunarclient/jre/1.18.2/zulu17.30.15-ca-fx-jre17.0.1-linux_x64/bin/java"
					  }
	config['Optifine'] = {'1.7 Optifine': HOME+"/.lunarclient/offline/1.7/OptiFine_1.7.10_HD_U_E7",
						  '1.8 Optifine': HOME+"/.lunarclient/offline/1.8/preview_OptiFine_1.8.9_HD_U_M6_pre2",
						  '1.12 Optifine': HOME+"/.lunarclient/offline/1.12/preview_OptiFine_1.12.2_HD_U_G6_pre1",
						  '1.16 Optifine': HOME+"/.lunarclient/offline/1.16/OptiFine_1.16.5_HD_U_G8",
						  '1.17 Optifine': HOME+"/.lunarclient/offline/1.17/preview_OptiFine_1.17.1_HD_U_H1_pre2",
						  '1.18.1 Optifine': HOME+"/.lunarclient/offline/1.18.1/preview_OptiFine_1.18.1_HD_U_H5_pre4",
						  '1.18.2 Optifine': HOME+"/.lunarclient/offline/1.18.2/OptiFine_1.18.2_HD_U_H6"
						  }
	config['Optimizations'] = {'LC Cosmetics' : "On"}
	with open(os.getenv("HOME")+"/.lcl/Options.ini", 'w') as configfile:
		config.write(configfile)
		
# Read Values from "Options.ini".	   
def ConfigRead(Version):
	
	ConfigExist()
	config = configparser.ConfigParser()
	config.read(os.getenv("HOME")+"/.lcl/Options.ini")
	Arguments_String=config['Java']["Arguments"]
	Arguments_List=Arguments_String.split()
	
	# 1.7
	if Version=="1.7":
		Java_Path=config['Java']["1.7 Java"]
		Directory=config['Minecraft']["1.7 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.7 Optifine"]
		
	# 1.8	
	elif Version=="1.8":
		Java_Path=config['Java']["1.8 Java"]
		Directory=config['Minecraft']["1.8 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.8 Optifine"]
		
	# 1.12	
	elif Version=="1.12":
		Java_Path=config['Java']["1.12 Java"]
		Directory=config['Minecraft']["1.12 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.12 Optifine"]
		
	# 1.16	
	elif Version=="1.16":
		Java_Path=config['Java']["1.16 Java"]
		Directory=config['Minecraft']["1.16 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.16 Optifine"]
		
	# 1.17	
	elif Version=="1.17":
		Java_Path=config['Java']["1.17 Java"]
		Directory=config['Minecraft']["1.17 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.17 Optifine"]
		
	# 1.18.1	
	elif Version=="1.18.1":
		Java_Path=config['Java']["1.18.1 Java"]
		Directory=config['Minecraft']["1.18.1 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.18.1 Optifine"]

	# 1.18.2
	elif Version=="1.18.2":
		Java_Path=config['Java']["1.18.2 Java"]
		Directory=config['Minecraft']["1.18.2 Directory"]
		Cosmetics=config['Optimizations']['LC Cosmetics']
		Optifine_Path=config['Optifine']["1.18.2 Optifine"]

	# Return Values
	return [Cosmetics, Java_Path, Directory, Arguments_List, Optifine_Path]
