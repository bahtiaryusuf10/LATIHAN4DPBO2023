// Import library yang dibutuhkan
#include <bits/stdc++.h>

using namespace std; // Menggunakan standard namespace

class Lecturer : public CivitasAcademic // Membuat class Lecturer (child) yang mengextends ke class CivitasAcademic (parent)
{
private:                      // Membuat atribut berjenis private
    int offRegNumber;         // Untuk menyimpan NIP dosen
    string teritaryEducation; // Untuk menyimpan pendidikan terakhir dosen
    string proficiency;       // Untuk menyimpan keahlian dosen
    Major majorObject;        // Untuk menyimpan objek dari class Major

public:
    /* Konstruktor */
    Lecturer() : CivitasAcademic() // Membuat konstruktor tanpa isian, class yang di-extends akan diinstansiasi terlebih dahulu
    {
        offRegNumber = 0;
        teritaryEducation = "";
        proficiency = "";
        majorObject = Major();
    }

    Lecturer(long long identity, string name, char gender, string university, string faculty, string email, int offRegNumber, string teritaryEducation, string proficiency, Major major) : CivitasAcademic(identity, name, gender, university, faculty, email) // Membuat konstruktor dengan isian dari parameter
    {
        this->offRegNumber = offRegNumber;
        this->teritaryEducation = teritaryEducation;
        this->proficiency = proficiency;
        this->majorObject = major;
    }

    /* Setter dan Getter untuk setiap atribut di dalam class Lecturer */
    void setOffRegNumber(int offRegNumber)
    {
        this->offRegNumber = offRegNumber;
    }

    void setTeritaryEducation(string teritaryEducation)
    {
        this->teritaryEducation = teritaryEducation;
    }

    void setProficiency(string proficiency)
    {
        this->proficiency = proficiency;
    }

    int getOffRegNumber()
    {
        return this->offRegNumber;
    }

    string getTeritaryEducation()
    {
        return this->teritaryEducation;
    }

    string getProficiency()
    {
        return this->proficiency;
    }

    Major getMajorObject()
    {
        return this->majorObject;
    }

    /* Destruktor */
    ~Lecturer() // Membuat destruktor untuk menghapus semua objek yang telah dibuat
    {
    }
};