from civitasacademic import CivitasAcademic # Import class CivitasAcademic dari file CivitasAcademic.py
from major import Major # Import class Major dari file major.py

class Student(CivitasAcademic): # Deklarasi class Student (child class dari CivitasAcademic)
    __idNumber = 0 # Untuk menyimpan NIM mahasiswa, atribut berjenis private
    __majorObject = Major("", "", []) # Untuk menyimpan jurusan mahasiswa, atribut berjenis private

    def __init__(self, identity, name, gender, university, email, faculty, idNumber, major): # Membuat constructor
        super().__init__(identity, name, gender, university, email, faculty) # Menginisialisasi setiap atribut yang ada di dalam konstruktor parent class CivitasAcademic
        self.__idNumber = idNumber # Menginisialisasi atribut __idNumber
        self.__majorObject = major # Menginisialisasi atribut __majorObject
    
    def setIdNumber(self, idNumber): # Setter untuk atribut __idNumber
        self.__idNumber = idNumber # Menginisialisasi atribut __idNumber

    def getIdNumber(self): # Getter untuk atribut __idNumber
        return self.__idNumber # Mengembalikan nilai atribut __idNumber
    
    def getMajor(self): # Getter untuk atribut __majorObject
        return self.__majorObject # Mengembalikan nilai atribut __majorObject