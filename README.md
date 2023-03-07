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
Pada program Python

![Screenshot - Python](https://user-images.githubusercontent.com/100776170/223392606-73f0b640-d595-4ba6-b8d3-c11717fb97ef.png)

<br>

Pada program C++
