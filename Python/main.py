from student import Student # Import class Student dari file Student.py
from lecturer import Lecturer # Import class Lecturer dari file Lecturer.py
from major import Major # Import class Major dari file Major.py
from course import Course # Import class Course dari file Course.py


studentList = [] # List untuk menyimpan objek mahasiswa
lecturerList = [] # List untuk menyimpan objek dosen
courseStudent1 = [] # List untuk menyimpan objek mata kuliah
courseStudent2 = [] # List untuk menyimpan objek mata kuliah

course1 = Course("Rekayasa Termofluida") # Membuat objek dari class Course
courseStudent1.append(course1) # Menambahkan objek course1 ke dalam list courseStudent
course2 = Course("Metode Analisis Konversi Energi") # Membuat objek dari class Course
courseStudent1.append(course2) # Menambahkan objek course1 ke dalam list courseStudent

studentObject1 = Student(377120192823, "Maikel", "L", "MIT", "maikel@mit.edu", "FTMD", 21098701, Major("Teknik Mesin", "MES1214", courseStudent1)) # Membuat objek dari class Student
studentList.append(studentObject1) # Menambahkan objek studentObject1 ke dalam list studentList

course3 = Course("Desain Pemrograman Berorientasi Objek") # Membuat objek dari class Course
courseStudent2.append(course3) # Menambahkan objek course1 ke dalam list courseStudent

studentObject2 = Student(321341233212, "Tommy Shelby", "L", "MIT", "tommy@mit.edu", "STEI", 20021214, Major("Teknik Informatika", "TIK1200", courseStudent2)) # Membuat objek dari class Student
studentList.append(studentObject2) # Menambahkan objek studentObject1 ke dalam list studentList

print("==============DATA MAHASISWA==============")
for i in range(len(studentList)): # Looping untuk menampilkan data mahasiswa
    print("NIK              : " + str(studentList[i].getIdentity()))
    print("Nama             : " + studentList[i].getName())
    print("Jenis Kelamin    : " + studentList[i].getGender())
    print("Universitas      : " + studentList[i].getUniversity())
    print("Email            : " + studentList[i].getEmail())
    print("NIM              : " + str(studentList[i].getIdNumber()))
    print("Fakultas         : " + studentList[i].getFaculty())
    print("Jurusan          : " + studentList[i].getMajor().getMajorName())
    print("Kode Jurusan     : " + studentList[i].getMajor().getCode())
    for j in range(len(studentList[i].getMajor().getCourse())): # Looping untuk menampilkan data mata kuliah
        print("Mata Kuliah ke-" + str(j + 1) + " : " + studentList[i].getMajor().getCourseIndex(j).getCourseName())
    print()

courseDosen = [] # List untuk menyimpan objek mata kuliah
courseDosen.append(course3) # Menambahkan objek course1 ke dalam list courseStudent

lecturerObject1 = Lecturer(371789019822, "Mrs. Ocha", "P", "MIT", "ocha@mit.edu", "STEI", 20350190, "Magister", "Koding", Major("Teknik Informatika", "TIK1200", courseDosen)) # Membuat objek dari class Lecturer
lecturerList.append(lecturerObject1) # Menambahkan objek lecturerObject1 ke dalam list lecturerList

print("\n==============DATA DOSEN==============")
for i in range(len(lecturerList)): # Looping untuk menampilkan data dosen
    print("NIK                 : " + str(lecturerList[i].getIdentity()))
    print("Nama                : " + lecturerList[i].getName())
    print("Jenis Kelamin       : " + lecturerList[i].getGender())
    print("Universitas         : " + lecturerList[i].getUniversity())
    print("Email               : " + lecturerList[i].getEmail())
    print("NIP                 : " + str(lecturerList[i].getOffRegNumber()))
    print("Fakultas            : " + lecturerList[i].getFaculty())
    print("Jurusan             : " + lecturerList[i].getMajor().getMajorName())
    print("Kode Jurusan        : " + lecturerList[i].getMajor().getCode())
    print("Pendidikan Terakhir : " + lecturerList[i].getTeritaryEducation())
    for j in range(len(lecturerList[i].getMajor().getCourse())): # Looping untuk menampilkan data mata kuliah
        print("Mata Kuliah ke-" + str(j + 1) + "    : " + lecturerList[i].getMajor().getCourseIndex(j).getCourseName())
    print()