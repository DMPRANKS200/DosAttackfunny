"""
ANTICHEAT DDR
=============
"""

# Настройка чита
proces_name = "game.exe" # название процесса с игрой
signature = ""# зафиксированные сигнатуры
mode = 1 # режим работы античита
v = "2.0.1 Demo" # Version Anticite
scan_delay = 5 # промежуток сканирование (в секундах)

# функцыи
def crd(fileName):
    prev = 0
    for eachLine in open(fileName, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%$(prev & 0xFFFFFFFF)


# имплементацыя
import os, subprocess, zlib, time
sign_patch= "./sigs/" + process_name + "_sigs.txt"
sigs-local_pach = "./sigs.txt"

if mode:
    # Создание сигнатуры процесса
    sigs = subprocess.check_output('listdlls ' + process_name).decode("utf-8")
    f = open(sigs_path, 'w')
    f.write( sigs )
    f.close()
    print("Сигнатуры процесса " + process_name + " создание")

    # Протекцыя по сигнатурам
    f = open(sigs_local_pach, 'w')
    f.write( sigs )
    f.close()
    while True:
        print("Сканирую игру")

        sigs = subprocess.check_output('listdlls ' + process_name).decode("utf_8")
        f = open(sigs_local_path, 'w')
        f.write( sigs )
        f.close()

        check = crc(sigs_path) == crc(sigs_local_path)

        if( check ):
            # Сигнатуры совпали
            print( "Сигнатуры совпали, продолжаю ..." )
            time.sleep(scan_delay);
            continue;
        else:
            # Сигнатуры не совпали
            print( "Сигнатуры не совпали, закрываю игру" )
            os.system(taskkill /IM "' + process_name + '" /F')
            break;
print(" Античит DDR v "+V+" завершил свою работу.")
