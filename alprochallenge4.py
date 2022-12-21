import mysql.connector
import matplotlib.pyplot as plt
import getpass

#Koneksi ke database
db = mysql.connector.connect(
    host = 'localhost', #atau '127.0.0.1'
    user = 'root',
    password = '',
    database = 'db_kuliah'
)

def menuAdmin():
    user = input("Username: ")
    sandi = getpass.getpass()
    if sandi == 'admin123' and user == 'Admin':
        print ("Anda Telah Login")   

    else:
        print ("Username atau Password Anda Salah")
        
    while True:
        print("="*20)
        print("=======MENU ADMIN=======")
        print("""
            1. Input Data
            2. Tampil Semua Data
            3. Cari Data dengan Nama Atau Nim
            4. Exit
            """)
        print("="*20)
        pilihan = int(input("Masukan Pilihan Menu: "))
        if pilihan == 1:
            mycursor = db.cursor()
            sql = "INSERT INTO tb_mahasiswa (nim, nama, nilai_alpro, nilai_agama, nilai_tbo) VALUES (%s, %s, %s, %s, %s)"
            nim = input("masukan nim: ")
            nama = input("masukan nama: ")
            nilai_alpro = input("masukan nilai alpro: ")
            nilai_agama = input("masukan nilai agama:  ")
            nilai_tbo = input("masukan nilai tbo : ")
            val = (nim, nama, nilai_alpro, nilai_agama, nilai_tbo)
            mycursor.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(mycursor.rowcount))

        elif pilihan == 2:
            mycursor = db.cursor()
            sql = "SELECT * FROM tb_mahasiswa"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            
            if mycursor.rowcount < 0:
                print("Data Not Found")
            else :
                for data in result:
                    print(data[1:])

        elif pilihan == 3:
            mycursor = db.cursor()
            keyword = input("Masukan nim atau nama sebagai kata kunci: ")
            sql = "SELECT * FROM tb_mahasiswa WHERE nim=%s"
            val = (keyword,)
            mycursor.execute(sql,val)
            result = mycursor.fetchall()
            print("Data yang dicari: ", result)
            print("{} Data berhasil dicari: ".format(mycursor.rowcount))
        else:
            print("tidak ada pilihan menu")

def menuMahasiswa():
        print("="*20)
        print("=======MENU ADMIN=======")
        print("""
            1. Lihat Data Berdasarkan Nim
            2. Tampil Grafik Nilai
            3.  Exit
            """)
        print("="*20)
        menu2 = int(input("Masukan Pilihan Menu: "))
        if menu2 == 1 :
            mycursor = db.cursor()
            keyword = input("Masukan nim sebagai kata kunci: ")
            sql = "SELECT * FROM tb_mahasiswa WHERE nim=%s"
            val = (keyword,)
            mycursor.execute(sql,val)
            result = mycursor.fetchall()
            print("Data yang dicari: ", result)
            print("{} Data berhasil dicari: ".format(mycursor.rowcount))
            
        elif menu2 == 2:
            cursor = db.cursor()
            sql = "SELECT * FROM tb_mahasiswa"
            cursor.execute(sql)
            result = cursor.fetchone()
            sql2 = "SELECT * FROM tb_matkul"
            cursor.execute(sql2)
            result2 = cursor.fetchone()
            nama = result2[1:]
            data= result[3:]
            dataint = list(map(int, data))
            position= range(len(dataint))
            plt.bar(position, dataint)
            plt.xticks(position, nama)
            plt.show()
            
        else:
            print("tidak ada pilihan menu")


# MENU UTAMA
while True:
    print("="*20)
    print("=======MENU ADMIN=======")
    print("""
        1. Menu Admin
        2. Menu Mahasiswa
        3. Exit
        """)
    print("="*20)
    menu = int(input("masukan pilihan  menu: "))
    if menu == 1:
        menuAdmin()
    elif menu == 2:
        menuMahasiswa()
    else:
        print("tidak ada pilihan")
        break