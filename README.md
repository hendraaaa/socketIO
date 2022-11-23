# Membuat visualisasi data IoT menggunakan flask,SocketIo dan Chart
project ini membuat visualisasi data IoT dengan menggunakan charJS sebagai library untuk visualisasi, Flask sebagai framework berbasis python, socketIO library yang digunakan untuk komunikasi  secara realtime

<h2>Requirement</h2>
<ul>
  <li>python 3.X</li>
  <li>flask-socketio</li>
  <li>chartJS</li>
</ul>

<h2>How to running</h2>
## Cara Install Aplikasi

Untuk menginstall aplikasi, perintah yang digunakan adalah:
```terminal
$ sudo apt [nama_aplikasi]
```

`sudo` kependekan dari `SuperUserDo`. Digunakan untuk perintah yang memerlukan *`root's permission`*. `root` adalah user yang punya hak akses paling tinggi dalam sistem operasi ubuntu (administrator). 

`apt` adalah contoh perintah yang hanya bisa dilakukan oleh admin. Digunakan untuk menangani penambahan dan penghapusan perangkat lunak (package).

Misalnya kamu ingin coba membuat file bernama `hello.json` via terminal menggunakan file editor bernama `vim`. Tapi biasanya `vim` belum terpasang.

Coba ketik perintah:
```terminal
$ vim hello.json
```
Hasilnya:
```terminal
bash: vim: command not found
```

Maka kamu harus install dulu vim tersebut memakai `apt`:

```terminal
$ apt install vim  
```
Hasilnya:
```terminal
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?
```

### Cara install vim
Sekarang tambahkan `sudo` sebelum command line:
```terminal
$ sudo apt install vim
```
Hasilnya:
```terminal
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libpython3.6 vim-common vim-runtime xxd
Suggested packages:
  ctags vim-doc vim-scripts
The following NEW packages will be installed:
  libpython3.6 vim vim-common vim-runtime xxd
0 upgraded, 5 newly installed, 0 to remove and 19 not upgraded.
Need to get 8123 kB of archives.
After this operation, 37.3 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```

Enter `Y` untuk melanjutkan proses.   
Setelah instalasi selesai, ketik perintah ini untuk memastikan instalasi berhasil:

```terminal
$ vim -version
```
Hasilnya:
```terminal
VIM - Vi IMproved 8.0 (2016 Sep 12, compiled Apr 10 2018 21:31:58)
Garbage after option argument: "-version"
More info with: "vim -h"
```
### Cara menggunakan vim  
Dengan asumsi kamu sudah [install vim](#cara-install-vim), ketik perintah berikut untuk step-by-step tutorial-nya.  
```terminal
$ vimtutor
  ```
Pastikan kamu paham perintah dasar ini sebelum lanjut.  

### Selanjutnya
Jika kamu sudah memahami perintah dasar Vim, ikuti langkah [selanjutnya](#contoh-penggunaan-command-line)
