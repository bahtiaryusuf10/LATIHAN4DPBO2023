// Import library yang dibutuhkan
#include <bits/stdc++.h>

using namespace std; // Menggunakan standard namespace

class CivitasAcademic : public Human // Membuat class CivitasAcademic (child) yang mengextends ke class Human (parent)
{
private:               // Membuat atribut berjenis private
    string university; // Untuk menyimpan nama universitas mahasiswa
    string faculty;    // Untuk menyimpan nama fakultas mahasiswa
    string email;      // Untuk menyimpan email mahasiswa

public:
    /* Konstruktor */
    CivitasAcademic() : Human() // Membuat konstruktor tanpa isian, class yang di-extends akan diinstansiasi terlebih dahulu
    {
        this->university = "";
        this->faculty = "";
        this->email = "";
    }

    CivitasAcademic(long long identity, string name, char gender, string university, string faculty, string email) : Human(identity, name, gender) // Membuat konstruktor dengan isian dari parameter
    {
        this->university = university;
        this->faculty = faculty;
        this->email = email;
    }

    /* Setter dan Getter untuk setiap atribut di dalam class CivitasAcademic */
    void setUniversity(string university)
    {
        this->university = university;
    }

    void setFaculty(string faculty)
    {
        this->faculty = faculty;
    }

    void setEmail(string email)
    {
        this->email = email;
    }

    string getUniversity()
    {
        return this->university;
    }

    string getFaculty()
    {
        return this->faculty;
    }

    string getEmail()
    {
        return this->email;
    }

    /* Destruktor */
    ~CivitasAcademic()
    {
    }
};