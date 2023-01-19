import os
import subprocess

# Root check
print('[+] Checking user id')
if os.geteuid() != 0:
    print('[-] Error: The script must be run as root')
    print('[-] Exiting')
    exit(2)

# Add new debian repostitories
# TO DO

# Update apt
#subprocess.run('apt update -y')

# Install packages
current_dir = os.path.dirname(os.path.abspath(__file__))
packages_file_path = os.path.join(current_dir, 'packages')

print('[+] Reading packages from {}'.format(packages_file_path))
with open(packages_file_path) as f:
    lines = [line.strip() for line in f]

for package in lines:
    cmd = 'apt install {} -y'.format(package)
    subprocess.run(cmd.split())

# Import linux config
subprocess.run('git clone -C ~/ https://github.com/0xblank/linux_config.git'.split())

# Install Oh my zsh
subprocess.run(os.path.join(current_dir, 'zsh.sh').split())

print('[+] Installation was successful')