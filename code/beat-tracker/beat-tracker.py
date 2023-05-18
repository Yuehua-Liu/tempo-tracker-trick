#%%
import subprocess
import threading
import time
import pygame
import librosa

def play_music(music_file):
    pygame.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

# 讀取音訊檔案
y, sr = librosa.load(r'.\crazy_frog.mp3')

# 節拍追蹤
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 獲取節拍時間點
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# 在一個新線程中播放音樂
music_thread = threading.Thread(target=play_music, args=(r'.\crazy_frog.mp3',))
music_thread.start()

start_time = time.time()

for beat_time in beat_times:
    # 等待到節拍時間點
    time.sleep(beat_time - (time.time() - start_time))
    
    # 執行你的操作
    # 創建一個字串，其中包含一個 Python script，該 script 打印 200 條消息
    script = """
for i in range(10):
    print(f'''⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⣠⠤⠶⣶⣶⠬⠦⡀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣀⣠⠭⠭⢍⡛⠲⣄⠂⠂⡴⢋⣴⣾⣿⣿⣿⣿⣿⣦⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⡰⠊⠁⠂⠂⠂⠂⠂⠂⣸⣷⣾⣇⠘⢿⣿⣿⣿⣿⣿⣿⠿⢀⣤⡀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠣⠂⠂⠂⠂⠂⠂⣠⣼⣿⡿⠉⠻⣿⣦⣬⣭⣭⣭⣭⣴⣶⣿⡿⣧⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣿⣶⣦⣤⣶⣶⣿⣿⣿⡥⠤⢤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⣥⣝⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢫⣿⠿⠛⠛⠛⠛⡻⢶⣶⣶⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣟⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢸⠃⢀⣤⠶⠶⠶⣤⣙⣮⡓⠉⠉⠂⢞⣟⣿⣟⣟⣯⡉⠙⣿⣿⣿⣦⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⡇⢀⡞⠁⠂⢀⣰⣟⣟⡿⣟⠌⠂⠌⣸⠹⣷⣾⣿⣟⡇⠂⢘⣿⡿⡿⢷⡀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢠⡇⢸⡁⠂⠂⠈⠻⠿⠟⢁⡿⠂⠂⠌⢋⢀⡙⠿⣟⣟⣤⣴⡿⠿⠊⠌⠌⠱⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠋⠂⠂⠙⠶⣶⣤⣤⡲⠖⠋⠂⠂⠂⠂⠂⠈⠙⠋⠛⠉⠉⠁⠂⣠⣴⣾⡿⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣦⣄⣀⣀⠂⠂⠂⠂⠂⣀⣀⣀⣀⣀⡤⣤⣤⣤⣤⣶⣶⣶⣿⡿⠛⠋⣠⣾⣦⣀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⠛⠏⠻⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⠋⠉⠉⠁⠂⠂⠂⣠⣼⣿⣿⣿⣿⣧⠄⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠉⠂⠂⠂⠂⠂⠂⠈⠂⠂⠂⠂⠂⠂⢀⣠⣶⣿⣿⣿⣿⣿⢿⣿⣿⣤⠐⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⡀⢀⣼⣿⣶⣤⣀⣀⠂⠂⠂⠂⣀⣀⣀⣤⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠈⠻⢿⠗⠂⠌⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⣰⣿⡿⠛⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⣀⣀⡀⠂⢠⠂⠐⡄⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⣴⡿⠟⠉⠂⠂⠂⠈⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠸⠿⠋⠁⢸⣟⣶⣶⣿⡄⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠌⣿⣶⠋⠁⠂⠂⠂⠂⠂⠂⠂⣿⣿⣿⣿⣿⣷⣟⣿⣿⠿⠛⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠂⠂⠂⠂⠐⠿⠿⣿⡿⠋⠂⠂⠂⠂
⠂⠂⠂⠂⠂⢀⣴⣤⡀⠌⣿⠟⠂⠂⠂⠂⠂⠂⠂⠂⠂⣿⣿⣿⣿⣿⡏⠉⠂⠂⠂⠂⠂⠂⠂⠌⠹⣿⣿⣿⣿⣿⣿⣿⣿⡏⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⣠⡀⠸⡿⣿⣷⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣀⣼⣿⣿⣿⣿⣿⠁⠂⠂⠂⠂⠂⠂⠂⠂⠂⠌⢻⣿⣿⣿⣿⣿⣿⣧⣤⣤⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⣾⣟⣷⣴⠃⣀⣀⡴⠚⠂⠂⠂⠂⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠂⠂⠂⠂⠂⣀⡀⠂⠂⠂⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠘⠿⠿⠋⠂⠉⠁⠂⠂⠂⠂⠂⠂⠈⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⡿⣷⣶⣤⣄⣀⡁⠌⣀⣀⣠⣾⣿⠟⠂⠂⠈⠁⠂⣠⣾⠇⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣀⣟⣆⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠉⠛⠿⣿⣿⣿⣿⣿⠿⠋⠂⠂⠂⠂⠂⢀⣼⣿⠏⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢸⣿⣿⣿⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⠛⠛⠂⠂⠂⠂⠂⠂⠂⢀⣾⡿⠋⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢸⣿⣿⠃⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢠⣾⠋⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⣿⠏⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠘⠇⠂⠂⢀⣴⣦⣄⣀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⣤⣴⣄⣼⣧⠂⠂⣻⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣷⠂⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠹⣿⣿⣿⣿⣶⣾⣿⡄⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠉⠙⠛⠋⠉⠉⠙⠛⠻⠿⠻⠟⠁⠂⠂⠂⠂⠂⠂⠂⠂
⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⠙⠻⢿⣿⡟⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂''')
    """

    # 寫入到一個暫時的 Python 檔案
    with open("temp_script.py", "w") as f:
        f.write(script)

    # 在新的命令提示字元窗口中運行這個 Python script
    subprocess.Popen(["start", "cmd.exe", "/k", "python temp_script.py"], shell=True)

# 確保音樂播放完畢
music_thread.join()

