// Import library yang dibutuhkan
#include <bits/stdc++.h>

using namespace std; // Menggunakan standard namespace

class Student : public CivitasAcademic // Membuat class Student (child) yang mengextends ke class CivitasAcademic (parent)
{
private:               // Membuat atribut berjenis private
    int idNumber;      // Untuk menyimpan NIM (ID number) mahasiswa
    Major majorObject; // Membuat objek dari class Major

public:
    /* Konstruktor */
    Student() : CivitasAcademic() // Membuat konstruktor tanpa isian, class yang di-extends akan diinstansiasi terlebih dahulu
    {
        this->idNumber = 0;
        this->majorObject = Major();
    }

    Student(long long identity, string name, char gender, string university, string faculty, string email, int idNumber, Major major) : CivitasAcademic(identity, name, gender, university, faculty, email) // Membuat konstruktor dengan isian dari parameter
    {
        this->idNumber = idNumber;
        this->majorObject = major;
    }

    /* Setter dan Getter untuk setiap atribut di dalam class Student */
    void setIdNumber(int idNumber)
    {
        this->idNumber = idNumber;
    }

    int getIdNumber()
    {
        return this->idNumber;
    }

    Major getMajorObject()
    {
        return this->majorObject;
    }

    /* Destruktor */
    ~Student() // Membuat destruktor untuk menghapus semua objek yang telah dibuat
    {
    }
};