import pexpect
import time
from dotenv import load_dotenv
import os

# Load secret passwords from .env
load_dotenv()
SUDO_PASSWD = os.getenv("SUDO_PASSWD")
NEW_FIRMWARE_PASSWD = os.getenv("NEW_FIRMWARE_PASSWD")

with open('./passwd-lists/100K-passwords.txt', 'r') as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()  # Remove any leading/trailing whitespaces

    child = pexpect.spawn('sudo firmwarepasswd -setpasswd')

    # Wait for the sudo password prompt and enter the password
    child.expect('Password:')
    child.sendline(SUDO_PASSWD) # Replace with sudo password here

    # Enter the current firmware password
    child.expect('Enter password:')
    child.sendline(password)

    # Enter new password
    child.expect('Enter new password:')
    child.sendline(NEW_FIRMWARE_PASSWD)  # Replace with new firmware password here
    child.expect('Re-enter new password:')
    child.sendline(NEW_FIRMWARE_PASSWD)  # Replace with new firmware password here

    # Wait for the password to finish and capture the output
    child.expect(pexpect.EOF)
    output = child.before.decode()
    print(f"Output for password '{password}':\n{output}")

    child.close()
    time.sleep(1)