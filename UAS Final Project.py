                                            #Proyek Akhir Membuat Program Multi Window
                                                           #Kelompok NVA
                                            #1.Nabilah Qurrotua'yun      (20507334003) 
                                            #2.Verlenda Sarma Qur'Aini  (20507334021)
                                            #3.Abid Syafara Muhibuddin  (20507334066)

import tkinter as tk
import time;



def jendelaInput(): 
    def saveInput1():
        a4 = inputA4.get()
        viewerA4.config(state='normal')
        viewerA4.delete(0, 'end')
        viewerA4.insert(0, a4)
        viewerA4.config(state='readonly')
        inputWindow.destroy()
    inputWindow = tk.Tk()
    inputWindow.title("Configuration Paper A4")
    inputWindow.geometry("250x120")
    inputA4 = tk.Entry(inputWindow, justify="center")

    tk.Label(inputWindow, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA4.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow, text="Save Changes", command=saveInput1).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper2():
    def saveInput2():
        a3 = inputA3.get()
        viewerA3.config(state='normal')
        viewerA3.delete(0, 'end')
        viewerA3.insert(0, a3)
        viewerA3.config(state='readonly')
        inputWindow2.destroy()
    inputWindow2 = tk.Tk()
    inputWindow2.title("Configuration Paper A3")
    inputWindow2.geometry("250x120")
    inputA3 = tk.Entry(inputWindow2, justify="center")

    tk.Label(inputWindow2, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA3.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow2, text="Save Changes", command=saveInput2).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper3():
    def saveInput3():
        a2 = inputA2.get()
        viewerA2.config(state='normal')
        viewerA2.delete(0, 'end')
        viewerA2.insert(0, a2)
        viewerA2.config(state='readonly')
        inputWindow3.destroy()
    inputWindow3 = tk.Tk()
    inputWindow3.title("Configuration Paper B1")
    inputWindow3.geometry("250x120")
    inputA2 = tk.Entry(inputWindow3, justify="center")

    tk.Label(inputWindow3, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA2.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow3, text="Save Changes", command=saveInput3).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper4():
    def saveInput4():
        b1 = inputB1.get()
        viewerB1.config(state='normal')
        viewerB1.delete(0, 'end')
        viewerB1.insert(0, b1)
        viewerB1.config(state='readonly')
        inputWindow4.destroy()
    inputWindow4 = tk.Tk()
    inputWindow4.title("Configuration Paper B1")
    inputWindow4.geometry("250x120")
    inputB1 = tk.Entry(inputWindow4, justify="center")

    tk.Label(inputWindow4, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB1.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow4, text="Save Changes", command=saveInput4).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper5():
    def saveInput5():
        b2 = inputB2.get()
        viewerB2.config(state='normal')
        viewerB2.delete(0, 'end')
        viewerB2.insert(0, b2)
        viewerB2.config(state='readonly')
        inputWindow5.destroy()
    inputWindow5 = tk.Tk()
    inputWindow5.title("Configuration Paper B2")
    inputWindow5.geometry("250x120")
    inputB2 = tk.Entry(inputWindow5, justify="center")

    tk.Label(inputWindow5, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB2.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow5, text="Save Changes", command=saveInput5).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def naik():
    global penambahan1
    penambahan1 += 1
    numberPrint3.config(state='normal')
    numberPrint3.delete(0,5)
    numberPrint3.insert(0,penambahan1)
    numberPrint3.config(state='readonly')
    if (penambahan1 >= 24):
        penambahan1 = 24
        numberPrint3.delete(0,5)
        numberPrint3.insert(0,penambahan1) #jika sudah maks

def turun():
    global penambahan2
    penambahan2 -= 1
    viewerInk.config(state='normal')
    viewerInk.delete(0,5)
    viewerInk.insert(0,penambahan2)
    viewerInk.config(state='readonly')
    if (penambahan2 <= 1):
        penambahan2 = 1
        viewerInk.delete(0,5)
        viewerInk.insert(0, penambahan2)

master = tk.Tk()
master.title("Monitor")
master.geometry("230x350")

def naik():
    global penambahan1
    penambahan1 += 1
    numberPrint3.config(state='normal')
    numberPrint3.delete(0,5)
    numberPrint3.insert(0,penambahan1)
    numberPrint3.config(state='readonly')
    if (penambahan1 >= 24):
        penambahan1 = 24
        numberPrint3.delete(0,5)
        numberPrint3.insert(0,penambahan1) #jika sudah maks

def turun():
    global penambahan2
    penambahan2 -= 1
    viewerInkA.config(state='normal')
    viewerInkA.delete(0,5)
    viewerInkA.insert(0,penambahan2)
    viewerInkA.config(state='readonly')
    if (penambahan2 <= 1):
        penambahan2 = 1
        viewerInkA.delete(0,5)
        viewerInkA.insert(0, penambahan2)


master = tk.Tk()
master.title("Monitor")
master.geometry("230x350")

viewerA4 = tk.Entry(master, justify="center")
viewerA4.insert(0, 0)
viewerA3 = tk.Entry(master, justify="center")
viewerA3.insert(0, 0)
viewerB1 = tk.Entry(master, justify="center")
viewerB1.insert(0, 0)
viewerB2 = tk.Entry(master, justify="center")
viewerB2.insert(0, 0)
viewerA2 = tk.Entry(master, justify="center")
viewerA2.insert(0, 0)
viewerInk = tk.Entry(master, justify="center")
viewerInk.insert(0,25)
viewerInkA = tk.Entry(master, justify="center")
viewerInkA.insert(0,25)
numberPrint3 = tk.Entry(master, justify="center")
numberPrint3.insert(0, 0)
status = tk.Entry(master)

tk.Label(master, text="Jumlah Kertas", font = ('Google Sans','15', 'bold')).grid(row=0, column=0, columnspan = 4)
# Untuk Cek Ketersediaan Kertas
tk.Label(master, text="A4").grid(row=1, column=0, sticky=tk.E)
viewerA4.grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = jendelaInput).grid(row=1, column = 3, sticky=tk.W)

tk.Label(master, text="A3").grid(row=2, column=0, sticky=tk.E)
viewerA3.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper2).grid(row=2, column = 3, sticky=tk.W)

tk.Label(master, text="A2").grid(row=3, column=0, sticky=tk.E)
viewerA2.grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper3).grid(row=3, column = 3, sticky=tk.W)

tk.Label(master, text="B1").grid(row=4, column=0, sticky=tk.E)
viewerB1.grid(row=4, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper4).grid(row=4, column = 3, sticky=tk.W)

tk.Label(master, text="B2").grid(row=5, column=0, sticky=tk.E)
viewerB2.grid(row=5, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper5).grid(row=5, column = 3, sticky=tk.W)

# Untuk Mengecek Ketersediaan Tinta
tk.Label(master).grid(row = 6, column = 0)
tk.Label(master, text="Banyaknya Tinta yang Berkurang per 25x Cetak", font = ('Google Sans','15', 'bold')).grid(row=7, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Hitam").grid(row=8, column=0, sticky=tk.E)
tk.Button(master, text = "use", command = turun).grid(row=8, column = 3, sticky=tk.W)
viewerInk.grid(row=8, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
penambahan2 = int(viewerInk.get())

tk.Label(master).grid(row = 7, column = 0)
tk.Label(master, text="Banyaknya Tinta yang Berkurang per 25x Cetak", font = ('Google Sans','15', 'bold')).grid(row=7, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Merah").grid(row=9, column=0, sticky=tk.E)
tk.Button(master, text = "use", command = turun).grid(row=9, column = 3, sticky=tk.W)
viewerInkA.grid(row=9, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
penambahan2 = int(viewerInkA.get())

# Untuk Pengecekan Sudah Mencetak Berapa Kali Cetak
tk.Label(master).grid(row = 9, column = 0)
tk.Label(master, text="Cetakan ke-", font = ('Google Sans','15', 'bold')).grid(row=10, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Total").grid(row=11, column=0, sticky=tk.E)
numberPrint3.grid(row=11, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
penambahan1 = int(numberPrint3.get())

# Tombol Untuk Melakukan Mencetak /Print
tk.Button(master, text = "PRINT", command = naik, width = 20, font = ('Google Sans','10', 'bold')).grid(row=13, column = 0, columnspan = 4, pady = 10, padx = 5, sticky=tk.N+tk.E+tk.S+tk.W)


viewerA4.config(state='readonly')
viewerA3.config(state='readonly')
viewerA2.config(state='readonly')
viewerB1.config(state='readonly')
viewerB2.config(state='readonly')
viewerInk.config(state='readonly')
viewerInkA.config(state='readonly')
numberPrint3.config(state='readonly')


tk.mainloop()
