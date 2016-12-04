import time
import subprocess
import random

sim_time = int(raw_input('How long should we simulate users for? (seconds) '))
cur_time = time.time()
target_time = sim_time + cur_time

# <== Fill password list with passwords file ==>

passwords = []
pwfile_choice = raw_input('Please specify a password list file or leave black to use the default: ')
if pwfile_choice == '':
    pwfile_choice = '500-worst-passwords.txt'

with open(pwfile_choice) as pwfile:
    for line in pwfile:
        passwords.append(line.strip())
# uncomment to test
# print passwords

# <== Fill user list with user file or preconfigured users ==>

users = []
usrfile_choice = raw_input('Please specify a user list file or leave black to use the default list: ')
if usrfile_choice == '':
    users = ['root','mysql','admin','administrator','user','postrges','oracle','guest','test']
else:
    with open(usrfile_choice) as usrfile:
        for line in usrfile:
            users.append(line.strip())

protocol = raw_input('Which protocol do you wish to test? ')
ip_addr = raw_input('What is the host IP you wich to test against?')

print 'Simulating user logins with Hydra...'
while cur_time < target_time:
    subprocess.call(['hydra','-l',random.choice(users),'-p',random.choice(passwords),ip_addr,protocol])
#    print random.choice(users) 
    cur_time = time.time()
    
