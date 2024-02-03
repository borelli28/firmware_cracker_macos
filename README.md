# firmware_cracker_macos
This brute force script is specifically designed to bruteforce the firmware password of MacOS systems using the macos utility firmwarepasswd -setpasswd

### Usage

Clone repo
`git clone https://github.com/borelli28/firmware_cracker_macos.git`

Install dependencies
`pip install -r requirements.txt`

Create .env file in project root directory and put your sudo password and new firmware password here,
`SUDO_PASSWD='YourSudoPasswordHere'`

`NEW_FIRMAWARE_PASSWD='YourNewFirmwarePasswordHere'`

or replace the environment variables in brute.py with your passwords,
`child.sendline('YourSudoPasswordHere') # Replace with sudo password here`

`child.sendline('YourNewFirmwarePasswordHere')  # Replace with new firmware password here`

You need a password list and replace the path in brute.py
`with open('./rockyou.txt', 'r') as file:`

Run the program
`python brute.py`
