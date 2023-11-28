## Proyecto de Red Neuronal Multicapa para Clasificación Binaria

Este proyecto implementa una red neuronal multicapa para la clasificación binaria utilizando el algoritmo de Levenberg-Marquardt. La interfaz gráfica permite ajustar diversos parámetros y visualizar la evolución del entrenamiento en tiempo real.

### Contenido del Repositorio

- **Ventana.py:** Contiene la implementación de la interfaz gráfica utilizando CustomTkinter/Tkinter para configurar y visualizar la red neuronal.

- **RedMulticapa.py:** Implementa la clase `RedMulticapa` que representa la red neuronal multicapa, con soporte para el algoritmo de Levenberg-Marquardt.

- **Colors.py:** Define una paleta de colores utilizada en la interfaz gráfica.

- **Main.py:** Punto de entrada del programa que inicializa y muestra la interfaz gráfica.

### Requisitos Previos

- Python 3.11.2 (recomendado)
- Bibliotecas: NumPy, Tkinter, CTkMessagebox, customtkinter, matplotlib (instalables a través de `pip install numpy tkinter`)

### Uso del Programa

1. Ejecutar `Main.py`.

   ![image](https://github.com/Dmn117/Levemberg-Marquardt/assets/102609918/2f7fd6c8-3eb4-4548-bb99-deac23862490)

2. Ajustar los parámetros de la red neuronal desde la interfaz gráfica.

   ![image](https://github.com/Dmn117/Levemberg-Marquardt/assets/102609918/11c1bea7-6927-4379-a5f2-e2c4fca9822e)

3. Hacer clic en el área de la gráfica para etiquetar puntos como azules (clic izquierdo, clase 0) o rojos (derecho, clase 1).

   ![image](https://github.com/Dmn117/Levemberg-Marquardt/assets/102609918/feb9679c-d9af-4b2f-b1ed-1c595e709dc3)

4. Iniciar el entrenamiento y observar la evolución en tiempo real.

   ![image](https://github.com/Dmn117/Levemberg-Marquardt/assets/102609918/53668a7a-3c03-46c4-9bac-45f594cc2e2c)

5. Observa el resultado al terminar las epocas del entrenamiento.

   ![image](https://github.com/Dmn117/Levemberg-Marquardt/assets/102609918/edcc5f2f-d4a5-40a1-a6b9-73a083b1f58e)


### Parámetros Configurables

- **Número de Neuronas:** Ajusta la cantidad de neuronas en la capa oculta.
- **Tasa de Aprendizaje (LR):** Controla la velocidad de aprendizaje de la red.
- **Épocas Totales:** Define el número total de épocas para el entrenamiento.
- **Épocas:** Muestra el progreso del entrenamiento en tiempo real.

### Personalización Adicional

Si deseas realizar cambios o mejoras en el proyecto, puedes explorar las siguientes áreas:

- Ajustar la paleta de colores en `Colors.py`.
- Experimentar con la configuración de la red neuronal en `RedMulticapa.py`.
- Personalizar el diseño y la estructura de la interfaz en `Ventana.py`.

### Contribuciones y Problemas

Si encuentras problemas o deseas contribuir al proyecto, ¡siéntete libre de abrir un problema o enviar una solicitud de extracción! Tu participación es bienvenida.
