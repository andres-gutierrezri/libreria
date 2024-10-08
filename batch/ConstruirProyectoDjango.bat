@echo off

echo -----------------------------------
echo PYTHON 3 + Entorno Virtual + Django
echo -----------------------------------

echo Version de Python y PIP
python --version
python -m pip --version
echo.

:: Actualizar PIP
echo Actualizar PIP
python.exe -m pip install --upgrade pip
echo.

echo ------------------------
echo Instalar Entorno Virtual
echo ------------------------

pip install virtualenv
echo.

echo ---------------------
echo Crear Entorno Virtual
echo ---------------------

:: Ingresar al Directorio del Proyecto
cd ..

:: Crear Entorno Virtual
python -m venv .venv
echo OK
echo.

echo -----------------------
echo Activar Entorno Virtual
echo -----------------------

call .\.venv\Scripts\activate.bat

:: Lista de Paquetes Instalados (PIP Python) 
pip list
echo.

echo ---------------------
echo Instalar Dependencias
echo ---------------------

:: Actualizar PIP en el Entorno Virtual
echo Actualizar PIP Entorno Virtual
python.exe -m pip install --upgrade pip
echo.

:: Instalar Dependencias para el Proyecto
pip install -r requirements.txt
echo.

echo -----------------
echo Version de Django
echo -----------------

:: Version de Django
python -m django --version
echo.

echo -----------------------------------
echo Lista de Paquetes Instalados en PIP
echo -----------------------------------

:: Lista de Paquetes Instalados (PIP Python) 
pip list
echo.

echo ------------------------
echo Migraciones del Proyecto
echo ------------------------

python manage.py makemigrations
echo.
python manage.py migrate
echo.

echo Abrir el Proyecto en el Navegador
start http://localhost:8000/

echo Iniciar Servidor
python manage.py runserver