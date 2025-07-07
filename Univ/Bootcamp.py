import os
import subprocess
import platform

def make_usb():
    print("Make sure that your USB is on GPT and exFat or NTFS format")
    usb_drive = input("Enter the path to your USB drive (e.g., /Volumes/USB): ")
    iso_path = input("Enter the path to your Windows ISO file: ")
    
    if not os.path.exists(usb_drive):
        print(f"USB drive {usb_drive} does not exist.")
        return
    
    if not os.path.exists(iso_path):
        print(f"ISO file {iso_path} does not exist.")
        return
    
    # Unmount the USB drive
    subprocess.run(["diskutil", "unmountDisk", usb_drive])
    
    # Use dd to create a bootable USB
    subprocess.run(["sudo", "dd", f"if={iso_path}", f"of={usb_drive}", "bs=1m", "conv=sync"])
    
    print("Bootable USB created successfully.")

if __name__ == "__main__":
    if platform.architecture()[0] == "64bit":
        print("This script helps you to create a bootable USB for Windows installation on Intel Macs")
        make_usb()
        exit(0)
    else:
        print("You can't install Bootcamp on Apple Silicon Macs")