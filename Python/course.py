class Course: # Deklarasi class Course
    __courseName = "" # Untuk menyimpan nama Mata Kuliah, atribut berjenis private

    def __init__(self, courseName = ""): # Membuat konstruktor
        self.__courseName = courseName # Menginisialisasi atribut __courseName

    def setCourseName(self, courseName): # Setter untuk atribut __courseName
        self.__courseName = courseName # Menginisialisasi atribut __courseName

    def getCourseName(self): # Getter untuk atribut __courseName
        return self.__courseName # Mengembalikan nilai atribut __courseName
    