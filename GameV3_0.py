import random
import os
import time
import sys

print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")

while True:
    num = random.randint(1, 100)
    n = 5
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("4. Russian Roulette (1 chance)")

    while True:
        try:
            ch = int(input("Enter choice:"))
            if ch <= 4 and ch > 0:
                break
            else:
                print("Please select a valid choice")
        except ValueError:
            print("Please enter a number")

    if ch == 1:
        n = 10
        print("Great! You have selected the Easy difficulty level.")
    elif ch == 3:
        n = 3
        print("Great! You have selected the Hard difficulty level.")
    elif ch == 2:
        n = 5
        print("Great! You have selected the Medium difficulty level.")
    elif ch == 4:
        n = 1
        print("Great job, Comrade! Let's play a round of Russian Roulette.")
        print("⚠ WARNING: Losing will delete SYSTEM32 ⚠")

    print("Let's start the game!")
    tries = 0
    won = False

    while n > 0:
        guess = int(input("Enter your guess:"))
        if guess > num:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < num:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {tries} attempts.")
            won = True
            break
        n -= 1
        tries += 1

    if won == False:
        print(f"Tough Luck! the number was {num}.")

        # Special prank for Russian Roulette
        if ch == 4:
             fake_files = [
    "C:\\Windows\\System32\\kernel32.dll",
    "C:\\Windows\\System32\\ntoskrnl.exe",
    "C:\\Windows\\System32\\bootmgr",
    "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "C:\\Windows\\System32\\winload.exe",
    "C:\\Windows\\System32\\hal.dll",
    "C:\\Windows\\System32\\config\\SYSTEM",
    "C:\\Windows\\System32\\config\\SOFTWARE",
    "C:\\Windows\\System32\\config\\SAM",
    "C:\\Windows\\System32\\config\\SECURITY",
    "C:\\Windows\\System32\\cmd.exe",
    "C:\\Windows\\System32\\user32.dll",
    "C:\\Windows\\System32\\gdi32.dll",
    "C:\\Windows\\System32\\advapi32.dll",
    "C:\\Windows\\System32\\msvcrt.dll",
    "C:\\Windows\\System32\\dnsapi.dll",
    "C:\\Windows\\System32\\wininet.dll",
    "C:\\Windows\\System32\\explorer.exe",
    "C:\\Windows\\System32\\taskmgr.exe",
    "C:\\Windows\\System32\\services.exe",
    "C:\\Windows\\System32\\lsass.exe",
    "C:\\Windows\\System32\\smss.exe",
    "C:\\Windows\\System32\\csrss.exe",
    "C:\\Windows\\System32\\drivers\\tcpip.sys",
    "C:\\Windows\\System32\\drivers\\ndis.sys",
    "C:\\Windows\\System32\\drivers\\volsnap.sys",
    "C:\\Windows\\System32\\drivers\\disk.sys",
    "C:\\Windows\\System32\\drivers\\kbdclass.sys",
    "C:\\Windows\\System32\\drivers\\mouclass.sys",
    "C:\\Windows\\System32\\drivers\\atapi.sys",
    "C:\\Windows\\System32\\drivers\\usbport.sys",
    "C:\\Windows\\System32\\drivers\\hidparse.sys",
    "C:\\Windows\\System32\\drivers\\acpi.sys",
    "C:\\Windows\\System32\\drivers\\pci.sys",
    "C:\\Windows\\System32\\drivers\\fltMgr.sys",
    "C:\\Windows\\System32\\drivers\\srv.sys",
    "C:\\Windows\\System32\\drivers\\afd.sys",
    "C:\\Windows\\System32\\drivers\\tcpip6.sys",
    "C:\\Windows\\System32\\drivers\\monitor.sys",
    "C:\\Windows\\System32\\drivers\\partmgr.sys",
    "C:\\Windows\\System32\\drivers\\cdrom.sys",
    "C:\\Windows\\System32\\drivers\\null.sys",
    "C:\\Windows\\System32\\drivers\\beep.sys",
    "C:\\Windows\\System32\\drivers\\i8042prt.sys",
    "C:\\Windows\\System32\\drivers\\ndproxy.sys",
    "C:\\Windows\\System32\\drivers\\netbt.sys",
    "C:\\Windows\\System32\\drivers\\rdbss.sys",
    "C:\\Windows\\System32\\drivers\\srv2.sys",
    "C:\\Windows\\System32\\drivers\\termdd.sys",
    "C:\\Windows\\System32\\drivers\\vga.sys",
    "C:\\Windows\\System32\\drivers\\watchdog.sys",
    "C:\\Windows\\System32\\drivers\\dxgkrnl.sys",
    "C:\\Windows\\System32\\drivers\\dxgmms1.sys",
    "C:\\Windows\\System32\\drivers\\win32k.sys",
    "C:\\Windows\\System32\\drivers\\framebuf.dll",
    "C:\\Windows\\System32\\drivers\\ntfs.sys",
    "C:\\Windows\\System32\\drivers\\fastfat.sys",
    "C:\\Windows\\System32\\drivers\\netio.sys",
    "C:\\Windows\\System32\\drivers\\http.sys"]
        for f in range(0,len(fake_files)):
            print(f"Deleting {fake_files[f]} ...")
            if f < 10:
                time.sleep(0.3)
            else:
                time.sleep(0.1)        
        print("Fatal Error: Windows cannot continue. Restart required.")
        print("💀 Your PC has been terminated by Russian Roulette 💀")
        os.system("shutdown /s /t 1")
        sys.exit()

    again = input("Want to play again(y/n):")
    if again == 'n':
        print("Thanks for playing, hope to see you again!")
        break
    elif again == 'y':
        print("Here We Go Again!")
    else:
        print("Oh look you accidentally pressed yes")



    
