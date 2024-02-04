# firmware_cracker_macos
This script is specifically designed to bruteforce the firmware password of MacOS systems using the terminal utility firmwarepasswd -delete, to try to delete the firmware password.

### Usage
- Clone repo  
`git clone https://github.com/borelli28/firmware_cracker_macos.git`  

- - Install dependencies  
`pip install -r requirements.txt`  

- Create .env file in project root directory and put your sudo password  
`SUDO_PASSWD=YourSudoPasswordHere`  

    or replace the environment variables in brute.py with your password  
    `child.sendline('YourSudoPasswordHere')`  

- You need a password list and replace the path in brute.py  
`with open('./rockyou.txt', 'r') as file:`  

- Run the program  
`python brute.py`  
