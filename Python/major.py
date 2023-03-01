class Major: # Deklarasi class Major
    __majorName = "" # Untuk menyimpan nama jurusan, atribut berjenis private
    __code = "" # Untuk menyimpan kode jurusan, atribut berjenis private 
    __courseObject = [] # Untuk menyimpan objek kelas Course, atribut berjenis private

    def __init__(self, majorName = "", code = "", courseName = []): # Membuat konstruktor
        self.__majorName = majorName # Menginisialisasi atribut __majorName
        self.__code = code # Menginisialisasi atribut __code
        self.__courseObject = courseName # Menginisialisasi atribut __courseObject

    def setMajorName(self, majorName): # Setter untuk atribut __majorName
        self.__majorName = majorName # Menginisialisasi atribut __majorName

    def setCode(self, code): # Setter untuk atribut __code
        self.__code = code # Menginisialisasi atribut __code
   
    def getMajorName(self): # Getter untuk atribut __majorName
        return self.__majorName # Mengembalikan nilai atribut __majorName

    def getCode(self): # Getter untuk atribut __code
        return self.__code # Mengembalikan nilai atribut __code
    
    def getCourse(self): # Getter untuk atribut __courseObject
        return self.__courseObject # Mengembalikan nilai atribut __courseObject
    
    def getCourseIndex(self, index): # Getter untuk atribut __courseObject
        return self.__courseObject[index] # Mengembalikan nilai atribut __courseObject