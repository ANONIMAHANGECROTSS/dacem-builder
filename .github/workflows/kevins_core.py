import os
import sys
import random
import string

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def obfuscate_smali(target_dir):
    print("[+] KEVINS CORE: Obfuscating Smali Code...")
    for root, dirs, files in os.walk(target_dir):
        if "smali" in root:
            for file in files:
                if file.endswith(".smali"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            lines = f.readlines()
                        
                        new_lines = []
                        for line in lines:
                            new_lines.append(line)
                            # Suntik Junk Code ke setiap method
                            if line.strip().startswith(".method"):
                                junk_name = get_random_string(15)
                                new_lines.append(f"    # KevinsEnc: {junk_name}\n")
                                new_lines.append(f"    const-string v0, \"{get_random_string(30)}\"\n")
                        
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.writelines(new_lines)
                    except:
                        pass

def encrypt_assets(target_dir):
    print("[+] KEVINS CORE: Encrypting Assets Folder...")
    assets_dir = os.path.join(target_dir, "assets")
    if not os.path.exists(assets_dir):
        return

    key = 170 # XOR Key

    for root, dirs, files in os.walk(assets_dir):
        for file in files:
            # Lewati gambar & font agar UI app target tidak blank total
            if file.endswith(".png") or file.endswith(".ttf") or file.endswith(".jpg"):
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, "rb") as f:
                    data = bytearray(f.read())
                
                for i in range(len(data)):
                    data[i] ^= key
                
                new_filename = get_random_string(10) + ".kenc"
                new_filepath = os.path.join(root, new_filename)
                
                with open(new_filepath, "wb") as f:
                    f.write(data)
                
                os.remove(filepath)
            except:
                pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Argumen kurang")
        sys.exit(1)
    
    workspace = sys.argv[1]
    level = sys.argv[2]

    print(f"============================================")
    print(f"   KEVINS ENCRYPTOR ENGINE | LEVEL: {level}   ")
    print(f"============================================")
    
    if level == "HARD":
        obfuscate_smali(workspace)
        encrypt_assets(workspace)
    elif level == "MEDIUM":
        obfuscate_smali(workspace)
    else:
        print("[+] LOW Level: Skip enkripsi berat, hanya resign APK.")
        
    print("[+] KEVINS CORE: Proses Selesai.")
