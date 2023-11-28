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

        def graficar():
            if not self.__puntos:
                CTkMessagebox(
                    title="Error", 
                    message='''No se Puede Graficar sin antes seleccionar puntos en el Plano
                            \n\nFavor de seleccionar al menos un punto coordenado del Plano 
                            antes de Generar la Grafica''', 
                    icon="cancel"
                )
            else:
                self.generarGrafica()


        def mostrarMatriz():
            if not self.__X:
                CTkMessagebox(
                    title="Error", 
                    message='''No se Puede Graficar sin antes seleccionar puntos en el Plano
                            \n\nFavor de seleccionar al menos un punto coordenado del Plano 
                            antes de Generar la Grafica''', 
                    icon="cancel"
                )
            else:
                self.mostrarMatriz()


        # Definicion de Propiedades visuales dentro de la Pestaña
        labelName = CTkLabel(
            sidebarFrame, 
            text='\n\n',
            padx=5,
            fg_color="transparent",
            text_color=WHITE,
            font=(
                "Arial",
                12
            )
        )
        labelName.grid(row=0, column=0, columnspan=2, pady=5, sticky='news')


        label_puntos = CTkLabel(
            sidebarFrame, 
            text='Neuronas: ', 
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                16
            )
        )
        label_puntos.grid(row=2, column=0, padx=5, sticky='w')

        entry_puntos = CTkEntry(sidebarFrame, width=100, textvariable=self.__neuronas)
        entry_puntos.bind("<KeyRelease>", validateEntry)
        entry_puntos.grid(row=2, column=1, padx=5, pady=5, sticky='e')


        label_w1 = CTkLabel(
            sidebarFrame, 
            text='Error: ', 
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                16
            )
        )
        label_w1.grid(row=3, column=0, padx=5, sticky='w')

        entry_w1 = CTkEntry(sidebarFrame, width=100, textvariable=self.__error)
        entry_w1.grid(row=3, column=1, padx=5, pady=5, sticky='e')

        label_x1 = CTkLabel(
            sidebarFrame, 
            text='Epocas Totales: ', 
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                15
            )
        )
        label_x1.grid(row=4, column=0, padx=5, sticky='w')

        entry_x1 = CTkEntry(sidebarFrame, width=100, textvariable=self.__epocasTotales)
        entry_x1.bind("<KeyRelease>", validateEntry)
        entry_x1.grid(row=4, column=1, padx=5, pady=5, sticky='e')

        label_tasa = CTkLabel(
            sidebarFrame, 
            text='Tasa Ap: ',
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                16
            )
        )
        label_tasa.grid(row=6, column=0, padx=5, sticky='w')

        entry_tasa = CTkEntry(sidebarFrame, width=100, textvariable=self.__lr)
        entry_tasa.bind("<KeyRelease>", validateEntry)
        entry_tasa.grid(row=6, column=1, padx=5, pady=5, sticky='e')

        label_epocas = CTkLabel(
            sidebarFrame, 
            text='Epocas: ',
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                16
            )
        )
        label_epocas.grid(row=7, column=0, padx=5, sticky='w')

        entry_epocas = CTkEntry(sidebarFrame, width=100, textvariable=self.__epocas)
        entry_epocas.bind("<KeyRelease>", validateEntry)
        entry_epocas.grid(row=7, column=1, padx=5, pady=5, sticky='e')

        buttonGraficar = CTkButton(sidebarFrame, text=f'Graficar',  command=self.start)
        buttonGraficar.grid(row=9, column=0, columnspan=2, padx=5, pady=6, sticky='news')

        buttonDetener = CTkButton(sidebarFrame, text=f'Detener',  command=self.stop)
        buttonDetener.grid(row=10, column=0, columnspan=2, padx=5, pady=6, sticky='news')

        buttonLimpiar = CTkButton(sidebarFrame, text=f'Limpiar', command=self.generarGrafica)
        buttonLimpiar.grid(row=12, column=0, columnspan=2, padx=5, sticky='news')

        self.generarGrafica()

    def secondComponents(self, frame, text):
        if self.label:
            self.label.destroy()
        self.label = CTkLabel(
            frame, 
            text=f'{text}',
            fg_color="transparent", 
            text_color=WHITE,
            font=(
                "Arial",
                16
            )
        )
        self.label.pack()

    def configuracionDePunto(self, output):
        if output == 0:
            return 'o', 'blue'
        if output == 1:
            return 'x', 'red'


    def generarGrafica(self):
        # Restablece variables
        self.__epocas.set(0)
        self.points = np.zeros((0,3))
        self.pointsY = np.zeros(0)
        # Generación de Figura y colgado de canva
        self.figure = Figure(figsize=(6.7, 5.6), dpi=100,)
        self.graph = self.figure.add_subplot(111)
        self.ConfigGrafica()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graphFrame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='news')

        cid = self.figure.canvas.mpl_connect('button_press_event', self.onClick)


    def ConfigGrafica(self):
        self.graph.cla()
        self.graph.set_title('Multicapa')
        self.graph.set_xlabel('X1')
        self.graph.set_ylabel('X2')
        self.graph.set_xlim([self.limits[0], self.limits[1]])
        self.graph.set_ylim([self.limits[0], self.limits[1]])
        # self.graph.grid(color='r', linestyle='--', linewidth=.3)
        # self.graph.axhline(y=0, color="k",linewidth=.6)
        # self.graph.axvline(x=0, color="k",linewidth=.6)
        self.graph.grid(True)


    def stop(self):
        self.__epocas.set(self.__epocasTotales.get())


    def start(self): # Obtener valores
        hiddenLayer = np.array([])
        #crear pesos y capa salida
        outputLayer = RedMulticapa(lr=self.__lr.get(), inputs=self.__neuronas.get() + 1, outputLayer=True)
        #crear capa entrada
        for i in range(self.__neuronas.get()):
            hiddenLayer = np.append(hiddenLayer, RedMulticapa(lr=self.__lr.get()))
        #crear matriz identidad 
        grid = np.zeros((self.__neuronas.get(), len(self.inputs)))

        if self.__epocas.get() > 0:
            self.__epocas.set(0)

        while self.__epocas.get() <= self.__epocasTotales.get():
            self.update()
            self.ConfigGrafica()
            #m= outputLayer.Jacobiana(error)
            #verificar los puntos de la grafica para hacerlos converger   
            for i in range(len(self.points)):
                [layer.ObtenerSalida(self.points[i]) for layer in hiddenLayer]
                outputLayer.ObtenerSalida(np.array([1] + [n.y for n in hiddenLayer]))
                outputLayer.hessiana(CapaAnteriorY=[1] + [n.y for n in hiddenLayer], PuntoY=self.pointsY[i])   
                [layer.hessiana(CapaAnteriorY=self.points[i], CapaSiguiente=outputLayer) for layer in hiddenLayer]
            # puntos grafica
            for i in range(len(self.points)):
                marker, color = self.configuracionDePunto(self.pointsY[i])
                self.graph.plot(self.points[i][1], self.points[i][2], marker=marker, markersize=15, linewidth=8, color=color)
            
            self.__epocas.set(self.__epocas.get() + 1)
            #imprimir funcion contorno
            for j in range(self.__neuronas.get()):
                grid[j] = hiddenLayer[j].Suposicion(self.inputs)
            self.outputs = [outputLayer.Suposicion(np.concatenate((np.array([1]), [g]), axis=None)) for g in grid.T]
            self.outputs = np.array(self.outputs)
            self.graph.contourf(self.xx, self.yy, self.outputs.reshape(self.xx.shape), cmap="seismic")
            self.canvas.draw()


    def onClick(self, event):
        deseado: int
        if event.button == 1:
            deseado = 0
        elif event.button == 3:
            deseado = 1
        
        coordenadas = f'Coordenadas del clic: x={event.xdata:.2f}, y={event.ydata:.2f}'
        marker, color = self.configuracionDePunto(deseado)
        
        self.points = np.append(self.points, [[1, float(event.xdata), float(event.ydata)]], axis=0)
        self.pointsY = np.append(self.pointsY, [deseado])
        self.graph.scatter(event.xdata, event.ydata, marker=marker, s=180, linewidths=5, c=color)
        self.canvas.draw()

        self.secondComponents(self.downFrame, coordenadas)
