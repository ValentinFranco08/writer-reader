class Write:
    def addNote(self, note):
        archivo = open('notes.txt', 'a')
        archivo.write(note + '\n')
        archivo.close()
