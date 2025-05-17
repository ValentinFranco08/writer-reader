from writer import Write
from reader import Reader

w = Write()
r = Reader()

# Agregar una nota simple
w.addNote("Nota de ejemplo")

# Leer las notas
notas = r.getAllNotes()
print("Notas guardadas:")
for nota in notas:
    print(nota)
