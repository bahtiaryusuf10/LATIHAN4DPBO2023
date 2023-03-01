from civitasacademic import CivitasAcademic # Import class CivitasAcademic dari file CivitasAcademic.py
from major import Major # Import class Major dari file major.py

class Lecturer(CivitasAcademic): # Deklarasi class Lecturer (child class dari CivitasAcademic)
    __offRegNumber = 0 # Untuk menyimpan nomor induk dosen, atribut berjenis private
    __teritaryEducation = "" # Untuk menyimpan pendidikan terakhir dosen, atribut berjenis private
    __proficiency = "" # Untuk menyimpan keahlian dosen, atribut berjenis private
    __majorObject = Major("", "", []) # Untuk menyimpan jurusan dosen, atribut berjenis private

    def __init__(self, identity, name, gender, university, email, faculty, offRegNumber, teritaryEducation, proficiency, major): # Membuat constructor
        super().__init__(identity, name, gender, university, email, faculty) # Menginisialisasi setiap atribut yang ada di dalam konstruktor parent class CivitasAcademic
        self.__offRegNumber = offRegNumber # Menginisialisasi atribut __offRegNumber
        self.__teritaryEducation = teritaryEducation # Menginisialisasi atribut __teritaryEducation
        self.__proficiency = proficiency # Menginisialisasi atribut __proficiency
        self.__majorObject = major # Menginisialisasi atribut __majorObject

    def setOffRegNumber(self, offRegNumber): # Setter untuk atribut __offRegNumber
        self.__offRegNumber = offRegNumber # Menginisialisasi atribut __offRegNumber 

    def setTeritaryEducation(self, teritaryEducation): # Setter untuk atribut __teritaryEducation
        self.__teritaryEducation = teritaryEducation # Menginisialisasi atribut __teritaryEducation

    def setProficiency(self, proficiency): # Setter untuk atribut __proficiency
        self.__proficiency = proficiency # Menginisialisasi atribut __proficiency

    def getOffRegNumber(self): # Getter untuk atribut __offRegNumber
        return self.__offRegNumber # Mengembalikan nilai atribut __offRegNumber
    
    def getTeritaryEducation(self): # Getter untuk atribut __teritaryEducation
        return self.__teritaryEducation # Mengembalikan nilai atribut __teritaryEducation
    
    def getProficiency(self): # Getter untuk atribut __proficiency
        return self.__proficiency # Mengembalikan nilai atribut __proficiency
    
    def getMajor(self): # Getter untuk atribut __majorObject
        return self.__majorObject # Mengembalikan nilai atribut __majorObject
