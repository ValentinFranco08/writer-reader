class Reader:
    def getAllNotes(self):
        try:
            archivo = open('notes.txt', 'r')
            notas = archivo.readlines()
            archivo.close()
            return notas
        except:
            return []
