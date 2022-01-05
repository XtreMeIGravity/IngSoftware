# IngSoftware
1. Integrantes del equipo:
2. Bustamante Mendoza Miguel Imanol
3. Hernández Ramírez Juan Daniel
4. López Hernández David
5. Najera Coronel Axel Imanol
6. Salguero Gatica Victor Manuel

---
# Como ejecutar el programa
1. Crear un entorno virtual con python o usar python por defecto, se recomienda version 3.6 >
2. Ejecutar el comando pip install -m Requirements.txt
3. Crear la base de datos con el nombre db_plantas y su respectivo usuario:userplantas y contraseña:rootPlantas en mysql 
4. Si desea modificar el usuario lo puede hacer dentro de la carpeta IngSofware/settings/local.py
5. Ejecutar el comando python manage.py makemigrations para ver los cambios que se realizaran en la base de datos y si existen conflictos en esto con la base de datos
6. Ejecutar el comando python manage.py migrate para crear la estructura de datos
7. Finalmente:Encender el servidor con "python manage.py runserver"
