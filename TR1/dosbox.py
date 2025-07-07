import subprocess
from pathlib import Path
import shutil
import os

# Game folder and config file
game_folder = Path.home() / "Games" / "Tomb1_DOS"
dosbox_conf = game_folder / "tomb1.conf"

# DOSBox paths (macOS only)
DOSBOX_PATHS = [
    "/opt/homebrew/bin/dosbox-staging",
    "/usr/local/bin/dosbox-staging",
    "/Applications/DOSBox.app/Contents/MacOS/DOSBox"
]

def find_dosbox():
    for path in DOSBOX_PATHS:
        if Path(path).exists():
            return path
    return None

def write_conf(executable):
    with open(dosbox_conf, "w") as f:
        f.write(f"""[autoexec]
@echo off
mount c "{game_folder}"
c:
cls
{executable}
exit
""")

def launch_dosbox():
    dosbox = find_dosbox()
    if not dosbox:
        print("❌ DOSBox not found.")
        print("👉 Install it with Homebrew: brew install dosbox-staging")
        return
    print(f"🚀 Launching DOSBox from: {dosbox}")
    subprocess.run([dosbox, "-conf", str(dosbox_conf)])

def install_tr1():
    cd_path = input("📥 Enter the full path to your mounted TR1 CD (e.g., /Volumes/TR1CD): ").strip()
    if not os.path.exists(cd_path):
        print(f"❌ Path {cd_path} does not exist!")
        return

    with open(dosbox_conf, "w") as f:
        f.write(f"""[autoexec]
@echo off
mount c "{Path.home() / 'Games'}"
mount d "{cd_path}"
d:
install.exe
exit
""")

    launch_dosbox()


def play_tr1():
    tomb_path = Path.home() / "Games" / "TOMBRAID" / "tomb.exe"
    if not tomb_path.exists():
        print("❌ 'tomb.exe' not found in ~/Games/TOMBRAID. Did you run the installer?")
        return

    # Write config to run the installed game
    with open(dosbox_conf, "w") as f:
        f.write(f"""[autoexec]
@echo off
mount c "{Path.home() / 'Games'}"
c:
cd TOMBRAID
tomb.exe
exit
""")

    launch_dosbox()


def main():
    print("=== Tomb Raider 1 DOSBox Launcher ===")
    print("This is an incomplete version, pull requests are welcome!")
    print("1. Install TR1")
    print("2. Play TR1")
    print("0. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        install_tr1()
    elif choice == "2":
        play_tr1()
    elif choice == "0":
        print("👋 Bye!")
    else:
        print("❓ Invalid option.")

if __name__ == "__main__":
    main()
