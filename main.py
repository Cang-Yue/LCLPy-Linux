#Modules
import sys
sys.path.insert(1, 'modules')
import argparse
import launch
import config
import subprocess
import os

try:
	os.mkdir(os.getenv("HOME")+"/.lcl")
except:
	pass
os.chdir(os.getenv("HOME")+"/.lcl")

#Checks if Options.ini exists or not.
config.ConfigExist()

#CLI Arguments
parser=argparse.ArgumentParser(prog="Lunar Client Lite Python (LCLPy)",
							   description="A debloated, feature rich and CLI based launcher for Lunar Client. Made in Python.",
							   usage="lcl [-v | --version ] <version>\n\t[-s | --server ] <version> <server>\n\t[-d | --debug ]\n\t[-c | --config ]")
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-v','--version',
					 action="store",
					 nargs=1,
					 metavar=("<Version>"),
					 help="Version => 1.7/1.8/1.12/1.16/1.17/1.18.1/1.18.2")
command.add_argument('-d','--debug',
					 action="store",
					 nargs=1,
					 metavar=("<Version>"),
					 help="Displays the selected version, JRE path, launch directory, arguments and launch command.")

command.add_argument('-s','--server',
					 action="store",
					 nargs=2,
					 metavar=("<Version>", "<Server IP>"),
					 help="Version => 1.7/1.8/1.12/1.16/1.17/1.18.1/1.18.2\nServer IP => Server IP Address")
command.add_argument('-c', '--config',
					 action='store_true',
					 help="Edit LCLPy's Config File.") 
args = parser.parse_args()

#Arguments
if args.version != None:
	launch.Launch(str(args.version[0]), " ", False)
elif args.config == True:
	subprocess.run(["nano Options.ini"], shell=True)
elif args.server != None:
	launch.Launch(str(args.server[0]), "--server "+args.s[1], False)
elif args.debug != None:
	launch.Launch(str(args.debug[0]), " ", True)
	
