import sys
import os
from colorama import Fore, Back, Style
#
# print("\n\t" + Fore.RED + "create\t\t" + Style.RESET_ALL + sys.argv[2])
# print("\n\t" + Fore.RED + "MAKE\t\t" + Style.RESET_ALL + sys.argv[2])

#START -> creating model
PATH = os.getcwd()

if not os.path.isdir(PATH + "/models"):
    try:
        os.mkdir(PATH + "/models")
    except OSError:
        print("\n\t" + Fore.RED + "FAIL\t\t" + Style.RESET_ALL + "Creation of the folder models failed.")
    else:
        print("\n\t" + Fore.YELLOW + "CREATE\t\t" + Style.RESET_ALL + "Successfully created models.")
else:
    print("\n\t" + Fore.YELLOW + "INVOKE\t\t" + Style.RESET_ALL + "Models folder.")

try:
    ff = open(PATH + "/models/"+ sys.argv[1] + ".py", "r")
    print("\t" + Fore.YELLOW + "INVOKE\t\t" + Style.RESET_ALL + "Invoked " + sys.argv[1] + " model."  )
except FileNotFoundError:
    try:
        f = open(PATH + "/models/" + sys.argv[1] + ".py","w+")
        print("\t" + Fore.YELLOW + "CREATE\t\t" + Style.RESET_ALL + "Successfully created " + sys.argv[1] + " model."  )
    except FileNotFoundError:
        print("\t" + Fore.RED + "FAIL\t\t" + Style.RESET_ALL + "Creation of the" + sys.argv[1] +" model failed.")


f = open(PATH + "/models/" + sys.argv[1] + ".py","w+")
modelname = sys.argv[1].capitalize()
tablename = sys.argv[1] + 's'

model = """
from db import db

class {modelname}Model(db.Model):
    __tablename__ = '{tablename}'

""".format(modelname=modelname,tablename=tablename)
f.write(model)

f.close()

print("\n")
