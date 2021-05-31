import sqlite3
import dbclass as dbc
import datetime

databaseName = 'dbtoko.db'

#connect ke db
conn = sqlite3.connect(databaseName)

#create table db
conn.execute(
    "CREATE TABLE IF NOT EXISTS produk (id_produk integer primary key autoincrement, nama_produk text, jenis_produk text, stok integer, terjual integer)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS pemasukan (id integer primary key autoincrement, tanggal DATE, keterangan text, nominal integer)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS pengeluaran (id integer primary key autoincrement, tanggal DATE, keterangan text, nominal integer)"
)
produklist = [
    dbc.produk("Masker duckbill", "Masker", 0, 0),
    dbc.produk("Kemeja pendek", "Fashion", 0, 0),
    dbc.produk("Strapmask", "Aksesoris", 0, 0),
    dbc.produk("Scrunchie", "Aksesoris", 0, 0),
    dbc.produk("Kaos stylish", "Fashion", 0, 0)
]
for pl in produklist:
    tempo = conn.execute("select * from produk where nama_produk = ?", (pl.getNama(),))
    if tempo.fetchone() is None:
        conn.execute("insert into produk (nama_produk, jenis_produk, stok, terjual) values (?,?,?,?)", (pl.getNama(), pl.getJenis(), pl.getStok(), pl.getTerjual()))
        conn.commit()

pemasukanlist = [
    dbc.moneyin(datetime.date(2021, 5, 21), "3 Box Masker terjual", 150000),
    dbc.moneyin(datetime.date(2021, 5, 21), "Pembelian 12 kemeja", 600000),
    dbc.moneyin(datetime.date(2021, 5, 25), "13 strapmask", 156000),
    dbc.moneyin(datetime.date(2021, 5, 26), "Penjualan 4 scrunchie", 20000),
    dbc.moneyin(datetime.date(2021, 5, 29), "2 kaos dipesan", 40000)
]
for pml in pemasukanlist:
    tempo = conn.execute("select * from pemasukan where keterangan = ?", (pml.getKeterangan(),))
    if tempo.fetchone() is None:
        conn.execute("insert into pemasukan (tanggal, keterangan, nominal) values (?,?,?)", (pml.getTanggal(), pml.getKeterangan(), pml.getNominal()))
        conn.commit()

pengeluaranlist = [
    dbc.moneyout(datetime.date(2021, 5, 23), "Kain batik", 550000),
    dbc.moneyout(datetime.date(2021, 5, 25), "Tali karet 10 meter", 70000),
    dbc.moneyout(datetime.date(2021, 5, 25), "150 buah kancing merah", 46500),
    dbc.moneyout(datetime.date(2021, 5, 27), "Kain mori", 228000),
    dbc.moneyout(datetime.date(2021, 5, 30), "Manik - manik 12 set", 375000)
]
for pnl in pengeluaranlist:
    tempo = conn.execute("select * from pengeluaran where keterangan = ?", (pnl.getKeterangan(),))
    if tempo.fetchone() is None:
        conn.execute("insert into pengeluaran (tanggal, keterangan, nominal) values (?,?,?)", (pnl.getTanggal(), pnl.getKeterangan(), pnl.getNominal()))
        conn.commit()

#menutup koneksi ke database
conn.close()