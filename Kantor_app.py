from tkinter import *
from tkinter import messagebox
import requests


class NiedodatniaError(Exception):
    pass
class PustepoleError(Exception):
    pass
class Kantor(object):
# funkcja przelicajaca zł na 8 walut
    def przeliczaj(self):
        try:
            if self.kwota_dowymiany.get() == "":
                raise PustepoleError
            kwota=float(self.kwota_dowymiany.get())
            if kwota < 0:
                raise NiedodatniaError
        except PustepoleError:
            messagebox.showinfo("Błąd", "NIc nie wpisałeś")
        except ValueError:
            messagebox.showinfo("Błąd", "Zły format kwoty")
        except NiedodatniaError:
                messagebox.showerror("Błąd", "Wpisałeś za małą kwote")
        else:
            self.kwotaUsd.delete(0,END)
            self.kwotaUsd.insert(0, str(round(kwota*self.waluty['USD'],2)))   

            self.kwotaEUR.delete(0,END)
            self.kwotaEUR.insert(0, str(round(kwota*self.waluty['EUR'],2)))  


            self.kwotaGBP.delete(0,END)
            self.kwotaGBP.insert(0, str(round(kwota*self.waluty['GBP'],2)))

            self.kwotaCHF.delete(0,END)
            self.kwotaCHF.insert(0, str(round(kwota*self.waluty['CHF'],2))) 

            self.kwotaJPY.delete(0,END)
            self.kwotaJPY.insert(0, str(round(kwota*self.waluty['JPY'],2))) 

            self.kwotaCAD.delete(0,END)
            self.kwotaCAD.insert(0, str(round(kwota*self.waluty['CAD'],2)))

            self.kwotaAUD.delete(0,END)
            self.kwotaAUD.insert(0, str(round(kwota*self.waluty['AUD'],2))) 

            self.kwotaCOP.delete(0,END)
            self.kwotaCOP.insert(0, str(round(kwota*self.waluty['COP'],2))) 
    #konstruktor 
    def __init__(self):   
        url="https://api.exchangerate-api.com/v4/latest/PLN" # api z którego pobieram dane do wyliczania walut
        self.dane =requests.get(url).json()
        self.waluty = self.dane['rates']  #zmienna z wartoscia kursów 
        self.data=self.dane['date'] 
        self.okno=Tk()  
        self.okno.geometry("480x380")
        self.okno.title("Kantor wymiany PLN")
        self.okno.configure(bg='#ABC270')
        self.budujkantor()
        self.okno.mainloop() # pętla obsługi zdarzeń

    def budujkantor(self):

        self.górnynapis=Label(self.okno, font=('Italic', 18, 'bold'), text="Kantor wymiany walut", bg='#ABC270', fg="black" )
        self.górnynapis.grid(row=0, column=0,  padx=20, columnspan=2)

        self.plnnapis=Label(self.okno, font=('Italic', 12, 'bold'), text="Wpisujesz kwote w PLN", bg='#ABC270', fg="black" )
        self.plnnapis.grid(row=1, column=0, padx=5)

        self.kwota_dowymiany=Entry(self.okno, width=20)
        self.kwota_dowymiany.grid(row=1, column=1, pady=30, sticky=W)

        self.przycisk=Button(self.okno,font=('arial', 10, 'bold'), text="Przelicz",padx=2, pady=2, bg="lightblue", fg="white", command=self.przeliczaj)
        self.przycisk.grid(row=1, column=2, padx=2, sticky=W) 

        nazwy_walut=("Dolar Amerykański","Euro","Brytyjski funt","Frank Szwajcarski","Jen","Dolar kanadyjski", "Dolar australijski", "Peso kolumbijskie")

        for i in range(8):

            self.waluta_obca=Label(self.okno, font=("arial", 12), text=nazwy_walut[i], bg='#ABC270', fg="black")
            self.waluta_obca.grid(row=i+2, column=0, padx=5)
        
        self.kwotaUsd=Entry(self.okno,width=20)
        self.kwotaUsd.grid(row=2, column=1, sticky=W)

        self.kwotaEUR=Entry(self.okno,width=20)
        self.kwotaEUR.grid(row=3, column=1, sticky=W)

        self.kwotaGBP=Entry(self.okno,width=20)
        self.kwotaGBP.grid(row=4, column=1, sticky=W)

        self.kwotaCHF=Entry(self.okno,width=20)
        self.kwotaCHF.grid(row=5, column=1, sticky=W)

        self.kwotaJPY=Entry(self.okno,width=20)
        self.kwotaJPY.grid(row=6, column=1, sticky=W)

        self.kwotaCAD=Entry(self.okno,width=20)
        self.kwotaCAD.grid(row=7, column=1, sticky=W)

        self.kwotaAUD=Entry(self.okno,width=20)
        self.kwotaAUD.grid(row=8, column=1, sticky=W)

        self.kwotaCOP=Entry(self.okno,width=20)
        self.kwotaCOP.grid(row=9, column=1, sticky=W)

        self.d=Label(self.okno, font=("arial", 12), text="Przelicznik z dnia "+self.data, bg='#ABC270', fg="black")
        self.d.grid(row=10, column=0,columnspan=2, pady=20)

k=Kantor()       
