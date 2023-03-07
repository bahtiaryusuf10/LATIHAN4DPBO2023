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
  + indexCourse  -> berisikan Keahlian Dosen, bertipe data `int`
  + courseObject -> berisikan sesuai atribut yang terdapat di dalam class Course, bertipe data `object`

  Tiap atribut memiliki setter dan getternya masing-masing yang berada pada class `Major`.

* *Course* sebagai composite dari class Major (Sekaligus class Student dan class Lecturer), dalam class ini terdapat 1 atribut, yaitu :
  + courseName    -> berisikan Nama Mata Kuliah yang dikontrak oleh Mahasiswa/diampu oleh Dosen, bertipe data `string`

  Atribut tersebut memiliki setter dan getter yang berada pada class `Course`.
  

Selain itu, di dalam class `Student` juga terdapat beberapa method untuk memproses data mahasiswa, diantaranya ialah addStudentData untuk menambahkan data, updateStudentData untuk melakukan perubahan terhadap data, deleteStudentData untuk menghapus data dari daftar, dan showListOfStudent untuk menampilkan daftar data mahasiswa.

Jika diasumsikan 1 class merupakan 1 tabel, maka terdapat primary key di masing-masing tabel tersebut diantaranya :
* *Human* -> identity
* *CivitasAcademic* -> email
* *Human* -> idNumber

Oleh sebab itu, ketika pengguna ingin mengubah record data mahasiswa pilihan atribut yang dapat diubah terbatas yakni university, email, major, dan faculty. Meskipun atribut email dikatergorikan atribut yang dapat diubah, tetapi akan dilakukan pengecekkan apakah email baru sudah digunakan atau belum oleh mahasiswa lain. 

Dalam tugas ini saya mendesain program dengan menggunakan jenis inheritance : `multi-level` dengan urutan *Human* => *CivitasAcademic* => *Student* , karena menurut saya sivitas akademik merupakan sekumpulan manusia yang memiliki posisinya masing-masing, seperti kumpulan dosen, kumpulan mahasiswa, kumpulan staff keuangan, dan lain sebagainya. Oleh karena itu, penggunaan multi-level sudah dirasa pas dengan kondisi yang ada.

<br>

## Alur Program
*Pada umumnya, semua program yang dibuat memiliki alur yang sama, hanya saja pada source code Php tidak tersedia menu input dari pengguna (data diinput secara hardcode).*

Pertama program akan membersihkan terlebih dahulu terminal, lalu akan menampilkan menu CRUD yang dapat dipilih oleh pengguna. Pengguna akan diminta untuk memasukan perintah pilihannya dan jika program sudah selesai menjalankan perintah maka proses (inputan untuk pemilihan menu) akan dijalankan berulang sampai pengguna menginput perintah untuk mengakhiiri program. 
Kelima perintahnya yaitu:
* Masukan (0) untuk keluar dari program program.
Jika pengguna menjalankan perintah ini maka program akan langsung keluar.
* Masukan (1) untuk menjalankan perintah `addStudentData`
Jika pengguna menjalankan perintah ini maka program akan meminta pengguna untuk menginputkan serangakian data mahasiswa, yaitu nik, nama, jenis kelamin, universitas, email, nim, program studi dan fakultas. Lalu, sebelum ditambah ke list, program akan melakukan pengecekan terlebih dahulu apakah list dalam keadaan kosong atau tidak. Proses pengecekkan dilakukan menggunakan nik/email/nim yang akan ditambah ke dalam list, jika nik/email/nim sudah tersedia di dalam list maka program akan mengeluarkan error handling dan data tidak akan diinput ke list.
* Masukan (2) untuk menjalankan perintah `updateStudentData`
Jika pengguna menjalankan perintah ini maka program akan meminta pengguna untuk menginput nik mahasiswa yang datanya akan diubah, jika nim tersedia pada list maka program akan meminta user menginputkan data mahasiswa yang baru yakni universita, email, program studi, dan fakultas, tidak dengan nik karena berkedudukan sebagai primary key. Jika nik tidak tersedia maka akan mengeluarkan error handling.
* Masukan (3) untuk menjalankan perintah `deleteStudentData`
Jika pengguna menjalankan perintah ini maka program akan meminta pengguna untuk menginput nik mahasiswa yang datanya akan dihapus, jika nik tersedia maka data tersebut akan dihapus dari list, tetapi jika data nik tidak tersedia pada list maka akan mengeluarkan error handling.
* Masukan (4) untuk menjalankan perintah `showListOfStudents`
Jika pengguna menjalankan perintah ini maka program akan menampilkan semua data mahasiswa yang ada pada list dalam bentuk tabel sederhana ke layar.

<br>

## Dokumentasi
Pada program Java

![Screenshot - Java](https://user-images.githubusercontent.com/100776170/218934153-3144f3b7-153a-4139-80c4-90764e81b57d.png)

<br>

Pada program Python

![Add - Python](https://user-images.githubusercontent.com/100776170/220263508-b24d0cf0-9a5d-4967-a30f-2f4bc603982c.png)
![Update - Python](https://user-images.githubusercontent.com/100776170/220263539-b4f1c9ad-b7bb-435e-a8ed-fbbf79edf8dc.png)
![Delete - Python](https://user-images.githubusercontent.com/100776170/220263555-d9761e68-a04d-4cb9-b684-a32ee4baf42b.png)

<br>

Pada program PHP

![Add - PHP](https://user-images.githubusercontent.com/100776170/220263669-1180bc4a-6f72-4742-8040-c320e224ec0f.png)
![Update - PHP](https://user-images.githubusercontent.com/100776170/220263682-540f719b-1807-4f83-8e4a-323d4c0028b7.png)
![Delete - PHP](https://user-images.githubusercontent.com/100776170/220263689-41c8be5e-c874-41e1-8c8c-fc8d2e848f2f.png)
