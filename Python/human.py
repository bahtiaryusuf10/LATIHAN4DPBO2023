class Human: # Deklarasi class Human (parent class)
    __identity = 0 # Untuk menyimpan NIK (Identity Number) mahasiswa, atribut berjenis private
    __name = "" # Untuk menyimpan nama mahasiswa, atribut berjenis private
    __gender = '' # Untuk menyimpan jenis kelamin mahasiswa, atribut berjenis private

    def __init__(self, identity = 0, name = "", gender = ''): # Membuat konstruktor
        self.__identity = identity # Menginisialisasi atribut __identity
        self.__name = name # Menginisialisasi atribut __name
        self.__gender = gender # Menginisialisasi atribut __gender

    def setIdentity(self, identity): # Setter untuk atribut __identity
        self.__identity = identity # Menginisialisasi atribut __identity

    def setName(self, name): # Setter untuk atribut __name
        self.__name = name # Menginisialisasi atribut __name

    def setGender(self, gender): # Setter untuk atribut __gender
        self.__gender = gender # Menginisialisasi atribut __gender

    def getIdentity(self): # Getter untuk atribut __identity
        return self.__identity # Mengembalikan nilai atribut __identity

    def getName(self): # Getter untuk atribut __name
        return self.__name # Mengembalikan nilai atribut __name

    def getGender(self): # Getter untuk atribut __gender
        return self.__gender # Mengembalikan nilai atribut __gender
