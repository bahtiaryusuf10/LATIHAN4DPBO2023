from human import Human # Import class Human dari file human.py

class CivitasAcademic(Human): # Deklarasi class CivitasAcademic (child class dari Human)
    __university = "" # Untuk menyimpan nama universitas, atribut berjenis private
    __email = "" # Untuk menyimpan email mahasiswa, atribut berjenis private
    __faculty = "" # Untuk menyimpan fakultas mahasiswa, atribut berjenis private

    def __init__(self, identity = 0, name = "", gender = '', university = "", email = "", faculty = ""): # Membuat konstruktor
        super().__init__(identity, name, gender) # Menginisialisasi setiap atribut yang ada di dalam konstruktor parent class Human
        self.__university = university # Menginisialisasi atribut __university
        self.__email = email # Menginisialisasi atribut __email
        self.__faculty = faculty # Menginisialisasi atribut __faculty

    def setUniversity(self, university): # Setter untuk atribut __university
        self.__university = university # Menginisialisasi atribut __university

    def setEmail(self, email): # Setter untuk atribut __email
        self.__email = email # Menginisialisasi atribut __email

    def setFaculty(self, faculty): # Setter untuk atribut __faculty
        self.__faculty = faculty # Menginisialisasi atribut __faculty

    def getUniversity(self): # Getter untuk atribut __university
        return self.__university # Mengembalikan nilai atribut __university

    def getEmail(self): # Getter untuk atribut __email
        return self.__email # Mengembalikan nilai atribut __email
    
    def getFaculty(self): # Getter untuk atribut __faculty
        return self.__faculty # Mengembalikan nilai atribut __faculty
