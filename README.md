Importar biblioteca Colorama desde la consola de visual studio code --> pip install colorama

Errores al importar Colorama 
1. Verifica la instalación de Colorama: pip show colorama Si Colorama está instalado, deberías ver información sobre el paquete. 
2. Verifica tu entorno de Python: Asegúrate de que Visual Studio Code esté utilizando el intérprete de Python correcto.
3. Reinicia Visual Studio Code: A veces, reiniciar Visual Studio Code puede resolver problemas de configuración.
4 Actualiza pip y setuptools: Asegúrate de tener la última versión de pip y setuptools ejecutando estos comandos en la terminal:
  pip install --upgrade pip
  pip install --upgrade setuptools
5. Reinstala Colorama: Si sospechas que Colorama podría estar instalado incorrectamente, intenta desinstalarlo y volver a instalarlo:
  pip uninstall colorama
  pip install colorama

Importar biblioteca tabulate desde la consola de visual studio code --> pip install tabulate 

cambios en el diseño del boton 

relief=tk.RAISED agrega un efecto de relieve al botón.
bg="lightblue" establece el color de fondo del botón en azul claro.
fg="black" establece el color del texto del botón en negro.
font=("Helvetica", 12, "bold") establece el tipo de letra en Helvetica, el tamaño del texto en 12 puntos y lo hace en negrita.