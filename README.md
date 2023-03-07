### Saya Muhammad Yusuf Bahtiar NIM 2107980 mengerjakan Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

<br>

## Deskripsi Tugas
Buatlah program berbasis OOP menggunakan bahasa pemrograman C++ dan Python  yang mengimplementasikan konsep inheritance, composition, dan array of object pada kelas-kelas tersebut: 
* Mahasiswa : NIM, nama, jenis_kelamin, fakultas, prodi
* Human : NIK, nama, jenis_kelamin
* SivitasAkademik : asal_universitas, email_edu
* Dosen : NIP, nama, jenis_kelamin, fakultas, prodi, pend_terakhir, keahlian
* Course : nama_matakuliah
* Program Studi : nama_prodi, kode, course

<br>

## Desain Program
![Desain](https://user-images.githubusercontent.com/100776170/223378730-e6900d05-cf73-41cb-b41b-b681a752a7e6.png)

Program didesain menjadi 6 class :
* *Human* sebagai super class, dalam class ini terdapat 3 atribut diantaranya:
  + identity -> berisikan NIK Mahasiswa, bertipe data `default : long long`
  + name     -> berisikan Nama Mahasiswa, bertipe data `string`
  + gender   -> berisikan Jenis Kelamin Mahasiswa, bertipe data `character`
  
  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `Human`.

* *CivitasAcademic* sebagai sub class dari class Human (CivitasAcademic menjadi intermediary class), dalam class ini terdapat 3 atribut diantaranya :
  + university -> berisikan Universitas Asal, bertipe data `string`
  + faculty    -> berisikan Fakultas, bertipe data `string`
  + email      -> berisikan Email Mahasiswa, bertipe data `string`

  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `CivitasAcademic`.

* *Student* sebagai sub class dari class CivitasAcademic, dalam class ini terdapat 2 atribut diantaranya :
  + idNumber    -> berisikan NIM Mahasiswa, bertipe data `integer`
  + majorObject -> berisikan sesuai atribut yang terdapat di dalam class Major, bertipe data `object`

  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `Student`. 

* *Lecturer* sebagai sub class dari class CivitasAcademic, dalam class ini terdapat 4 atribut diantaranya :
  + offRegNumber      -> berisikan NIP Dosen, bertipe data `integer`
  + teritaryEducation -> berisikan Pendidikan Terakhir Dosen, bertipe data `string`
  + proficiency       -> berisikan Keahlian Dosen, bertipe data `string`
  + majorObject -> berisikan sesuai atribut yang terdapat di dalam class Major, bertipe data `object`

  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `Lecturer`. 

* *Major* sebagai composite dari class Student dan Lecturer, dalam class ini terdapat 4 atribut diantaranya :
  + majorName    -> berisikan Nama Program Studi Mahasiswa/Dosen, bertipe data `string`
  + code         -> berisikan Kode Program Studi, bertipe data `string`
  + indexCourse  -> berisikan index array course (mata kuliah), bertipe data `int`
  + courseObject -> berisikan sesuai atribut yang terdapat di dalam class Course, bertipe data `object`

  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `Major`.

* *Course* sebagai composite dari class Major (Sekaligus class Student dan class Lecturer), dalam class ini terdapat 1 atribut, yaitu :
  + courseName    -> berisikan Nama Mata Kuliah yang dikontrak oleh Mahasiswa/diampu oleh Dosen, bertipe data `string`

  Atribut tersebut memiliki setter dan getter yang berada pada class `Course`.
  

Dalam tugas ini saya mendesain program dengan menggunakan jenis inheritance : `multi-level` dengan urutan *Human* => *CivitasAcademic* => *Student* dan *Human* => *CivitasAcademic* => *Lecturer*, karena menurut saya sivitas akademik merupakan sekumpulan manusia yang memiliki posisinya masing-masing, contohnya di sini terdapat kumpulan dosen dan kumpulan mahasiswa. Oleh karena itu, penggunaan multi-level sudah cukup baik untuk kondisi yang ada. 

Selain itu, sehubungan dengan apa yang diinginkan pada soal, saya membuat beberapa atribut komposit dari beberapa class, yakni class *Major* dan class *Course*. Saya memiliki argumen bahwa seorang dosen dan seorang mahasiswa pasti akan memiliki masing-masing 1 program studi dalam suatu universitas, tidak hanya itu, karena dalam suatu program studi umumnya memiliki berbagai mata kuliah yang akan dibentuk menjadi suatu kurikulum, maka perlu untuk membuat array untuk menampung list nama mata kuliah yang akan diampu oleh dosen dan dikontrak oleh mahasiswa.

<br>

## Alur Program
Kedua program, baik itu python maupun c++ dibuat dengan memiliki alur yang sama, yakni data diinput secara hardcode. Sehingga, pengguna cukup menjalankan atau mengkompilasi saja filenya, maka system akan menampilkan semua data mahasiswa dan dosen yang ada pada listMahasiswa dan listDosen ke layar.

<br>

## Dokumentasi
Pada program Python

![Screenshot - Python](https://user-images.githubusercontent.com/100776170/223392606-73f0b640-d595-4ba6-b8d3-c11717fb97ef.png)

<br>

Pada program C++
