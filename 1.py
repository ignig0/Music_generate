from music21 import *

stream2 = stream.Stream()

for _ in range(8):
    chord1 = chord.Chord(['C4', 'E4', 'A4'], quarterLength=0.75)
    stream2.append(chord1)

for _ in range(3):
    chord2 = chord.Chord(['B3', 'E4', 'A4'], quarterLength=0.75)
    stream2.append(chord2)

for _ in range(4):
    chord3 = chord.Chord(['B3', 'D4', 'G4'], quarterLength=0.75)
    stream2.append(chord3)



stream2.show('midi')
stream2.write('midi',fp=r'C:\Users\Velokoleso\Downloads\try1.midi')#сохранение файла