import subprocess

comando_1 = ["sudo", "apt-get", "install", "gcc", "python3-dev"]

subprocess.run(comando_1)

comando_2 = ["sudo", "apt", "install", "python3-pip"]

subprocess.run(comando_2)

comando_3 = ["pip", "install", "psutil"]

subprocess.run(comando_3)
