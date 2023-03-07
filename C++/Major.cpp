// Import library yang dibutuhkan
#include <bits/stdc++.h>

using namespace std; // Menggunakan standard namespace

class Major // Deklarasi class Major
{
private:                       // Membuat atribut berjenis private
    string majorName;          // Untuk menyimpan nama jurusan
    string code;               // Untuk menyimpan kode jurusan
    list<Course> courseObject; // Untuk menyimpan objek dari class Course

public:
    /* Konstruktor */
    Major() // Membuat konstruktor tanpa isian
    {
        this->majorName = "";
        this->code = "";
    }

    Major(string majorName, string code, list<Course> course) // Membuat konstruktor dengan isian dari parameter
    {
        this->majorName = majorName;
        this->code = code;
        this->courseObject = course;
    }

    /* Setter dan Getter untuk setiap atribut di dalam class Major */
    void setMajorName(string majorName)
    {
        this->majorName = majorName;
    }

    void setCode(string code)
    {
        this->code = code;
    }

    string getMajorName()
    {
        return this->majorName;
    }

    string getCode()
    {
        return this->code;
    }

    list<Course> getCourse()
    {
        return this->courseObject;
    }

    /* Destruktor */
    ~Major() // Membuat destruktor untuk menghapus semua objek yang telah dibuat
    {
    }
};