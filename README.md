## Proyecto de Red Neuronal Multicapa para Clasificación Binaria

Este proyecto implementa una red neuronal multicapa para la clasificación binaria utilizando el algoritmo de Levenberg-Marquardt. La interfaz gráfica permite ajustar diversos parámetros y visualizar la evolución del entrenamiento en tiempo real.

### Contenido del Repositorio

- **Ventana.py:** Contiene la implementación de la interfaz gráfica utilizando Tkinter para configurar y visualizar la red neuronal.

- **RedMulticapa.py:** Implementa la clase `RedMulticapa` que representa la red neuronal multicapa, con soporte para el algoritmo de Levenberg-Marquardt.

- **Colors.py:** Define una paleta de colores utilizada en la interfaz gráfica.

- **Main.py:** Punto de entrada del programa que inicializa y muestra la interfaz gráfica.

### Requisitos Previos

- Python 3.x
- Bibliotecas: NumPy, Tkinter (instalables a través de `pip install numpy tkinter`)

### Uso del Programa

1. Ejecutar `Main.py`.
2. Ajustar los parámetros de la red neuronal desde la interfaz gráfica.
3. Hacer clic en el área de la gráfica para etiquetar puntos como azules (clic izquierdo, clase 0) o rojos (derecho, clase 1).
4. Iniciar el entrenamiento y observar la evolución en tiempo real.

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
