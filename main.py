import tkinter as tk
from tkinter import messagebox
import requests
from threading import Thread
import time


class IrrigationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Irrigation App")

        self.ip_label = tk.Label(root, text="ESP32 IP Address:")
        self.ip_label.pack()

        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()
        self.ip_entry.insert(tk.END, "127.0.0.1:5000")  # Endereço do servidor Flask simulado

        self.duration_label = tk.Label(root, text="Duração (minutos):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.hour_label = tk.Label(root, text="Hora Programada (HH:MM): ")
        self.hour_label.pack()

        self.hour_spinbox = tk.Spinbox(root, from_=0, to=23, width=10)
        self.hour_spinbox.pack()

        self.start_button = tk.Button(root, text="Iniciar Irrigação", command=self.start_irrigation)
        self.start_button.pack()

        self.schedule_button = tk.Button(root, text="Programe IrrigaçãoAltomática", command=self.start_auto_irrigation)
        self.schedule_button.pack()

    @staticmethod
    def irrigate(duration, ip):
        try:
            requests.get(f"http://{ip}/on")
            time.sleep(duration)
            requests.get(f"http://{ip}/off")
            messagebox.showinfo("Info", "Fim da Irrigação")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def start_irrigation(self):
        try:
            duration = int(self.duration_entry.get()) * 60  # Converte minutos para segundos
            ip = self.ip_entry.get()
            Thread(target=self.irrigate, args=(duration, ip)).start()
            messagebox.showinfo("Info", "Irrigação Iniciada")
        except ValueError:
            messagebox.showerror("Error", "Por Favor entre com um número valido para duração da irrigação!")

    def auto_irrigation(self):
        while True:
            current_hour = time.localtime().tm_hour
            scheduled_hour = int(self.hour_spinbox.get())  # Você precisará adicionar um widget para hora programada
            if current_hour == scheduled_hour:
                duration = int(self.duration_entry.get()) * 60  # Converte minutos para segundos
                ip = self.ip_entry.get()
                self.irrigate(duration, ip)
                time.sleep(60)  # Espera uma hora antes de verificar novamente

    def start_auto_irrigation(self):
        Thread(target=self.auto_irrigation).start()
        messagebox.showinfo("Info", "Irrigação Automática Programada")


if __name__ == "__main__":
    root = tk.Tk()
    app = IrrigationApp(root)
    root.mainloop()
