import tkinter as tk
bag = []
root = tk.Tk()
root.title("Påse 2")
root.geometry("500x500")

skriv_text =tk.Label(root, text="skriv något här")
skriv_text.pack()

texten = tk.Entry(root)
texten.pack()

ruta = tk.Text(root, height=10, width=35)
ruta.pack()
               
def visa_påsen():
    ruta.delete(1.0, tk.END)
    if len(bag) == 0:
        ruta.insert(tk.END, "påsen är tom")
    else:
        ruta.insert(tk.END, "i påsen finns")
        for sak in bag:
            ruta.insert(tk.END, "\n" + sak)
 
def lägg_till(event = None):
    ruta.delete(1.0, tk.END)
    sak = texten.get()
    if sak == "":
        ruta.insert(tk.END, "skriv något först")
        return
    bag.append(sak)
    ruta.insert(tk.END, sak + "lades i påsen")
    texten.delete(0, tk.END)    
    

visa = tk.Button(root, text="visa innehål i påsen", command=visa_påsen)
visa.pack()

läggtill = tk.Button(root, text="lägg till föremål", command=lägg_till)
läggtill.pack()

avsluta = tk.Button(root, text="Avsluta", command=quit)
avsluta.pack()



root.mainloop()