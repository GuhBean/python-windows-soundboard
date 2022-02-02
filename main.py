from player import Player
from config import Settings

player = Player()
config = Settings()

if __name__ == "__main__":

    # get keybinding settings from config file
    keybinds = config.keybinds

    # assume key press
    while True:
        if input("what key\n") == "f1":
            player.load_audio_file(config.audio_folder + "\\" + keybinds[1][1])
            player.play_audio_file()

        elif input("what key/n") == "f2":
            player.load_audio_file(config.audio_folder + "\\" + keybinds[2][1])
            player.play_audio_file()
        else:
            print("break")
            break
