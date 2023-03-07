#include <bits/stdc++.h>
using namespace std;

#include "Human.cpp"
#include "CivitasAcademic.cpp" // Import file CivitasAcademic.cpp
#include "Course.cpp"          // Import file Course.cpp
#include "Major.cpp"           // Import file Major.cpp
#include "Student.cpp"         // Import file Student.cpp
#include "Lecturer.cpp"        // Import file Lecturer.cpp

int main()
{
    list<Student> studentList;                                               // Deklarasi list studentList dari kelas Student
    list<Lecturer> lecturerList;                                             // Deklarasi list lecturerList dari kelas Lecturer
    list<Course> courseListStudent1, courseListStudent2, courseListLecturer; // Deklarasi list courseListStudent dan courseListLecturer dari kelas Course

    courseListStudent1.push_back(Course("Rekayasa Termofluida"));            // Memasukkan data mata kuliah Pemrograman Berorientasi Objek ke dalam list courseListStudent
    courseListStudent1.push_back(Course("Metode Analisis Konversi Energi")); // Memasukkan data mata kuliah Pemrograman Berorientasi Objek ke dalam list courseListStudent
    studentList.push_back(Student(377120192823, "Maikel", 'L', "MIT", "FTMD", "maikel@mit.edu", 21098701, Major("Teknik Mesin", "MES1214", courseListStudent1)));

    courseListStudent2.push_back(Course("Desain Pemrograman Berorientasi Objek")); // Memasukkan data mata kuliah Pemrograman Berorientasi Objek ke dalam list courseListStudent
    studentList.push_back(Student(321341233212, "Thomas Shelby", 'L', "MIT", "STEI", "tommy@mit.edu", 20021214, Major("Teknik Informatika", "TIK1200", courseListStudent2)));

    cout
        << "==============DATA MAHASISWA==============" << endl;
    for (auto &student : studentList)
    {
        cout << "NIK                : " << student.getIdentity() << endl;
        cout << "Nama               : " << student.getName() << endl;
        cout << "Jenis Kelamin      : " << student.getGender() << endl;
        cout << "Universitas        : " << student.getUniversity() << endl;
        cout << "Fakultas           : " << student.getFaculty() << endl;
        cout << "Email              : " << student.getEmail() << endl;
        cout << "NIM                : " << student.getIdNumber() << endl;
        cout << "Program Studi      : " << student.getMajorObject().getMajorName() << endl;
        cout << "Kode Program Studi : " << student.getMajorObject().getCode() << endl;
        cout << "Mata Kuliah        : ";

        int no = 1;
        auto course_list = student.getMajorObject().getCourse();
        for (auto &course : course_list)
        {
            if (&course == &course_list.front())
                cout << no << ". " << course.getCourseName() << endl;
            else if (&course == &course_list.back())
                cout << "                     " << no << ". " << course.getCourseName() << '\n'
                     << endl;
            else
                cout << "                     " << no << ". " << course.getCourseName() << endl;
            no++;
        }
    }

    courseListLecturer.push_back(Course("Desain Pemrograman Berorientasi Objek")); // Memasukkan data mata kuliah Pemrograman Berorientasi Objek ke dalam list courseListStudent
    lecturerList.push_back(Lecturer(371789019822, "Mrs. Ocha", 'P', "MIT", "STEI", "ocha@mit.edu", 20350190, "Magister", "Koding", Major("Teknik Informatika", "TIK1200", courseListLecturer)));

    cout
        << "\n\n==============DATA DOSEN==============" << endl;
    for (auto &lecturer : lecturerList)
    {
        cout << "NIK                 : " << lecturer.getIdentity() << endl;
        cout << "Nama                : " << lecturer.getName() << endl;
        cout << "Jenis Kelamin       : " << lecturer.getGender() << endl;
        cout << "Universitas         : " << lecturer.getUniversity() << endl;
        cout << "Fakultas            : " << lecturer.getFaculty() << endl;
        cout << "Email               : " << lecturer.getEmail() << endl;
        cout << "NIP                 : " << lecturer.getOffRegNumber() << endl;
        cout << "Program Studi       : " << lecturer.getMajorObject().getMajorName() << endl;
        cout << "Kode Program Studi  : " << lecturer.getMajorObject().getCode() << endl;
        cout << "Pendidikan Terakhir : " << lecturer.getTeritaryEducation() << endl;
        cout << "Keahlian            : " << lecturer.getProficiency() << endl;
        cout << "Mata Kuliah         : ";

        int no = 1;
        auto course_list = lecturer.getMajorObject().getCourse();
        for (auto &course : course_list)
        {
            if (&course == &course_list.front())
                cout << no << ". " << course.getCourseName() << endl;
            else if (&course == &course_list.back())
                cout << "                     " << no << ". " << course.getCourseName() << '\n'
                     << endl;
            else
                cout << "                     " << no << ". " << course.getCourseName() << endl;
            no++;
        }
    }

    return 0;
}