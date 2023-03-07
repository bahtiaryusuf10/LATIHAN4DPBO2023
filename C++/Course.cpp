// Import library yang dibutuhkan
#include <bits/stdc++.h>

using namespace std; // Menggunakan standard namespace

class Course // Deklarasi class Course
{
private:               // Membuat atribut berjenis private
    string courseName; // Untuk menyimpan nama mata kuliah

public:
    /* Konstruktor */
    Course() // Membuat konstruktor tanpa isian
    {
        this->courseName = "";
    }

    Course(string courseName) // Membuat konstruktor dengan isian dari parameter
    {
        this->courseName = courseName;
    }

    /* Setter dan Getter untuk setiap atribut di dalam class Course */
    void setCourseName(string courseName)
    {
        this->courseName = courseName;
    }

    string getCourseName()
    {
        return this->courseName;
    }

    // Destruktor
    ~Course()
    {
    }
};