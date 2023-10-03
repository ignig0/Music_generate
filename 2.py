from tkinter import Tk
from tkinter.filedialog import askopenfilename
from music21 import *
from pydub import AudioSegment


def neuro(file):#нейронка
    #магия нейросетей
    pass


def convert_mp3_to_mid(path): #функция для конвертации
    mp3 = AudioSegment.from_mp3(path)
    file_name = path.split(".")[0]
    mp3.export(file_name + ".midi", format="midi")

root = Tk()
root.withdraw()
path = askopenfilename()

print("Выбранный файл:", path)

#new = convert_mp3_to_mid(path)
new_path = r"C:\Users\Robot\Downloads\MiConv.com__Piano_Classics_Lyudvig_van_Betkhoven_-_Moonlight_Sonata_48186103.midi"
print(new_path)

score = converter.parse(new_path)
print(f"{type(score)} длина {len(score)}")
score.show('midi')
score.show('text')
notes = score.flat.notes[::]
print(type(notes),"ноты", notes)
