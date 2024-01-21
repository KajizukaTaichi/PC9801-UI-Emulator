from time import sleep
from subprocess import run, CompletedProcess
import os
import vlc

def play_pipo_sound():
    player = vlc.MediaPlayer("seek.mp3")
    player.play()
    
    player = vlc.MediaPlayer("https://upload.wikimedia.org/wikipedia/commons/f/fb/NEC_PC-9801VX_ITF_beep_sound.ogg")
    player.play()

    sleep(2)

def display_text(text):
    for line in text.splitlines():
        print(line)
        sleep(0.04)

def animated_memory_check():
    def format_memory(i):
        return f'MEMORY {i}KB' if i < 640 else f'MEMORY 640KB + {i - 640}KB'

    memory = list(range(0, 3072 + 641, 8))
    for i in memory:
        frame = f"\r{format_memory(i)}"
        print(frame, end="")
        sleep(0.008) if i >= 640 else sleep(0.005)
    print(" OK", end="\r")
    sleep(4)

def display_title():
    titles = [
        "NEC PC-9800シリーズ パーソナルコンピュータ\n\n"
        "マイクロソフト MS—DOS バージョン 6.22\n"
        "Copyright (C) 1981, 1994 Microsoft Corp. / NEC Corporation",

        "HIMEM is testing extended memory... done.\n"
        "\n"
        "    プリンタが使用可能です\n"
        "    ＲＳ-２３２Ｃインターフェイスが使用可能です\n"
        "Microsoft (R) KKCFUNC Version 1.12\n"
        "Copyright (C) Microsoft Corp. 1991 , 1993. All rights reserved.\n\n"
        "KKCFUNC が組み込まれました. \n\n"
        "    AIかな漢字変換が使用可能です\n"
        "    辞書は、ドライプA:の NECAI.SYS です\n"
        "To Load Mouse Driver, Type MOLISE.\n"
        "To Unload Mouse Driver , Type MOLISE /R."
    ]

    display_text(titles[0])
    sleep(2)

    display_text(titles[1])
    sleep(1)

def main():
    play_pipo_sound()
    animated_memory_check()
    display_title()

    os.chdir("C:\\")
    while True:
        current_path = os.getcwd()
        command = input(f"\n{current_path}> ")

        if command.startswith('cd '):
            new_directory = command[3:]
            try:
                os.chdir(new_directory)
                continue
            except:
                pass

        result: CompletedProcess = run(command, shell=True, capture_output=True, text=True)
        display_text(result.stderr)
        display_text(result.stdout)


if __name__ == "__main__":
    main()
