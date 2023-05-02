# Práctica de la librería PANDAS

### Comandos para checar los datos

`.shape` Te devuelve número de rows y columnas  
`.head()` Te devuelve los primeros 5 rows y sus headers  
`.info()` Te devuelve los NON-NULL y tipo de datos de las columnas  
`.describe()` Te devuelve conteo, media, desviación estandar, mínimo, 25%,50%,75% y máximo  






### Para crear el entorno python de trabajo en el proyecto:  

##### 1. Actualiza PIP global.
```
python -m pip install -U Pip  
```

##### 2. Crea el entorno para el proyecto (lo llamaremos 'env').
```
python -m venv Pandas-Practicas-env
Pandas-Practicas-env\Scripts\activate
```

##### 3. Actualiza PIP en tu entorno e instala las dependencias del proyecto.
```
python -m pip install -U Pip
python -m pip install -U Pandas OpenPyXL iPyKernel
python -m pip install -U iPyChart MatPlotLib Seaborn
```