import numpy as np
import tkinter as tk

from CTkMessagebox import CTkMessagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import ListedColormap
from matplotlib.figure import Figure

from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkToplevel, CTkComboBox

from RedMulticapa import RedMulticapa
from Colors import *

class Ventana(CTk):
    def __init__(self):
        super().__init__()
        # Atributos para la construccion de la Red Neuronal
        self.__neuronas = tk.IntVar(value=10)
        self.__error = tk.DoubleVar(value=0.1)
        self.__epocasTotales = tk.IntVar(value=100)
        self.__lr = tk.DoubleVar(value=0.1)
        self.__epocas = tk.IntVar(value=0)

        # Opciones de Configuración de la Ventana(Semi Automatico pero distingue pantalla principal)
        self.__anchoVentana = 900
        self.__altoVentana = 600

        self.__xVentana = self.winfo_screenwidth() // 2 - self.__anchoVentana // 2
        self.__yVentana = self.winfo_screenheight() // 2 - self.__altoVentana // 2

        self.__posicion = f'{str(self.__anchoVentana)}x{str(self.__altoVentana)}+{str(self.__xVentana)}+{str(self.__yVentana-40)}'
        # self.minsize(self.__anchoVentana, self.__altoVentana)
        self.geometry(self.__posicion)

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        self.title("Practica 5_6 - Multicapa")
        self.iconbitmap('img/logo.ico')
        
        # Configuracions para el grafico

        self.colors = ("blue", "red",)
        self.cmap = ListedColormap(self.colors[: len(np.unique([0, 1]))])

        self.points = np.zeros((0,3))
        self.pointsY = np.zeros(0)

        self.entryLabels = ["No Neuronas: ", "LR: ", "A: "]
        # self.entries: Entry = []

        self.figure = None
        self.graph = None
        self.label = None
        self.canvas = None
        self.limits = [-5, 5] #limites de grafica

        self.x = np.linspace(self.limits[0], self.limits[1], 50)
        self.y = np.linspace(self.limits[0], self.limits[1], 50)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.inputs = np.array([np.ones(len(self.xx.ravel())), self.xx.ravel(), self.yy.ravel()]).T
        self.outputs = np.zeros(len(self.inputs))
        self.startUI()


    def startUI(self):
        # Comfiguración de Frame Superior
        self.principalFrame = CTkFrame(self, fg_color=OXFORD_3)
        self.principalFrame.rowconfigure(index=0, weight=3)
        self.principalFrame.rowconfigure(index=1, weight=1)
        self.principalFrame.columnconfigure(index=0, weight=1)
        self.principalFrame.grid(row=0, column=0, sticky='news')

        # Comfiguración de Frame Superior
        self.upperFrame = CTkFrame(self.principalFrame, fg_color=OXFORD_3)
        self.upperFrame.columnconfigure(index=0, weight=1)
        self.upperFrame.columnconfigure(index=1, weight=5)
        self.upperFrame.rowconfigure(index=0, weight=1)
        self.upperFrame.rowconfigure(index=1, weight=1)
        self.upperFrame.grid(row=0, column=0, sticky='news')

        # Configuración de Frame Inferior
        self.downFrame = CTkFrame(self.principalFrame, fg_color=OXFORD_3, bg_color=OXFORD_3)
        self.downFrame.grid(row=1, column=0, sticky='news')

        # Llama a la función que agrega los componenetes principales, al Frame Superior
        self.principalComponents(self.upperFrame)
        self.secondComponents(self.downFrame, '')

        # self.startBtn = Button(master=lowerFrame,style = 'W.TButton', text="Iniciar", command=self.start, width=8)
        # self.startBtn.grid(row=1, column=0)
        # self.figure = Figure(figsize=(6, 5), dpi=100,facecolor='#dcdcdc')
        # self.graph = self.figure.add_subplot(111)
        # self.ConfigGrafica()

        # self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
        # self.canvas.get_tk_widget().grid(row=0, column=2)

        # cid = self.figure.canvas.mpl_connect('button_press_event', self.onClick)


    def principalComponents(self, frame):
        sidebarFrame = CTkFrame(frame, fg_color=OXFORD_3)
        sidebarFrame.grid(row=0, column=0, sticky='news')
        sidebarFrame.columnconfigure(index=0, weight=1)
        sidebarFrame.columnconfigure(index=1, weight=1)
        sidebarFrame.rowconfigure(index=0, weight=1)
        sidebarFrame.rowconfigure(index=1, weight=10)

        self.graphFrame = CTkFrame(frame)
        self.graphFrame.grid(row=0, column=1, sticky='news')

        # Funciones Locales
        def validateEntry(*args):
            self.validateEntry(entry_x1, *args)
