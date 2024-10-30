import os
import subprocess

# Define ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Colorful banner
banner = f"""{GREEN}
blob:https://web.telegram.org/0d9eb546-8f2c-448f-96fe-146ed60e9312═╝ ╚═════╝╚═╝  ╚═╝ 
{RESET}"""

# Colorful info
info = f"""{YELLOW}
--------------------------------------------------------
Author : {CYAN}Shayan Bhat{YELLOW}
Telegram : {CYAN}@Shayanbhat{YELLOW}
TOOLS : {CYAN}MEMEFI COIN UP{YELLOW}
--------------------------------------------------------{RESET}
"""

os.system("clear")
print(banner)
print(info)

auth_token = input(f"{MAGENTA}Enter your auth token: {RESET}")

# Step 2: Delete the old query_id.txt file if it exists
file_path = 'query_id.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{GREEN}----------------------------------------------------------{RESET}")
else:
    print(f"{YELLOW}does not exist, creating a new one.{RESET}")

# Step 3: Save the new auth token into query_id.txt
with open(file_path, 'w') as file:
    file.write(auth_token)
    print(f"{GREEN}----------------------------------------------------------{RESET}")

# Step 4: Run memefi.py
try:
    subprocess.run(['python', 'memefi.py'])
except Exception as e:
    print(f"{RED}Failed to run memefi.py: {e}{RESET}")
