from tkinter import Tk, ttk
from tkinter import *
import requests
import json

# colors
cor0 = "#FFFFE0"  # Light yellow
cor1 = "#333333"  # Black
cor2 = "#FFD700"  # Gold

window = Tk()
window.geometry('300x320')
window.title('Currency Converter')
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)

# frames
top = Frame(window, width=300, height=60, bg=cor2)
top.pack(fill="x")

main = Frame(window, width=300, height=260, bg=cor0)
main.pack()

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = "Converted: {:.2f} {}".format(converted_amount, currency_2)

    result.config(text=formatted)

# top frame
app_name = Label(top, text="Currency Converter", height=1, padx=13, pady=5, anchor=CENTER,
                 font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.pack(fill="x")

# main frame
result = Label(main, text=" ", width=24, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 12 bold'),
               bg=cor0, fg=cor1)
result.grid(row=0, column=0, columnspan=2, pady=10)

currencies = [
    'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
    'MXN', 'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'RUB', 'INR', 'BRL', 'ZAR',
    'AED', 'SAR', 'PLN', 'THB', 'IDR', 'MYR', 'HUF', 'PHP', 'CZK', 'ILS',
    'CLP', 'DKK', 'COP', 'TWD', 'PEN', 'ARS', 'KWD', 'IQD', 'OMR', 'NPR',
    'JOD', 'BHD', 'GTQ', 'LBP', 'PYG', 'JMD', 'TTD', 'TZS', 'BDT', 'DOP',
    'KES', 'XCD', 'EGP', 'HNL', 'NAD', 'CRC', 'MUR', 'ISK', 'AZN', 'UYU',
    'AFN', 'RSD', 'XPF', 'XOF', 'AWG', 'TND', 'BAM', 'BWP', 'GYD', 'UGX',
    'MOP', 'YER', 'BND', 'LKR', 'GHS', 'NIO', 'MKD', 'SCR', 'AMD', 'SYP',  
    'ANG', 'MWK', 'LRD', 'XAF', 'KZT', 'SRD', 'ALL', 'GIP', 'BZD', 'GGP',
    'SVC', 'BRL'
]

from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),
                   bg=cor0, fg=cor1)
from_label.grid(row=1, column=0, padx=20, pady=10)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currencies)
combo1.grid(row=2, column=0)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),
                 bg=cor0, fg=cor1)
to_label.grid(row=1, column=1, pady=10)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currencies)
combo2.grid(row=2, column=1)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"), command=convert)
button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
