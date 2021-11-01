import sys 
import subprocess 
import os
# importing urllib.requests for internet cheking funtions 
import urllib.request 
  
# To check if the system is connected to the internet
def connect(host='https://google.com/'):
    # trying to open gfg 
    try: 
        urllib.request.urlopen(host) 
        return True
  
    # trying to catch exception when internet is not ON.
    except: 
        return False

# Reading package names
with open("requirements.txt",'r') as file:
    package_q = file.readlines()

    for package in package_q:
        # removing '\n'
        package = package[:-2]

def setup(module_name): 
  
    # updating pip to latest version 
    subprocess.run('python -m pip install --upgrade pip') 
  
    # commanding terminal to pip install required modules
    p = subprocess.run('pip3 install '+module_name) 
    
    # internet off 
    if(p.returncode == 1 and connect() == False): 
        print("error!! occured check\nInternet conection") 
  
    # Every thing worked fine 
    elif(p.returncode == 0): 
        print("It worked", module_name, " is installed") 
  
    # Name of module wrong 
    elif(p.returncode == 1 and connect() == True): 
        print("error!! occured check\nName of module")

print('Installing')
print('Please wait....')
print('Do not close this program')
for package in package_q: #sending module names to the setup_a funtion
    setup(package)
print('Installation finished')
subprocess.run('python main.py') #to run the main.py file