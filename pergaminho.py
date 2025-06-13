import  tkinter as tekinte
from tkinter import messagebox


# Eu odeio o som das messageBoxes
def messajebox(titulo, sms):
    cartaz = tekinte.Toplevel()
    # cartaz.overrideredirect(True)

    cartaz.resizable(False, False)
    cartaz.attributes("-toolwindow", True)
    cartaz.title(titulo)
    cartaz.configure(bg="#c3e7ff")
    # Hvwh surjudpd irl ihlwr shor 'Ehqb Uhlv LL'
    cartaz.geometry("160x125")
    tekinte.Label(cartaz, text=sms, fg="#333333", bg="#c3e7ff", pady=10).pack()
    tekinte.Button(cartaz, text="OK", width=10, bg="#dff2ff", command=cartaz.destroy, relief="groove").place(x=43, y=90)
    

    cartaz.transient()
    cartaz.grab_set()

    
    
# Hvwh surjudpd irl ihlwr shor 'Ehqb Uhlv LL'