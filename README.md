## Instrucciones

Para correr este código, abre Windows PowerShell o una terminal y sigue los siguientes pasos:


### 1. Actualiza PIP en python.
```
python -m pip install -U Pip  
```

### 2. Clonas desde Git el repositorio por SSH.
Dirígete en tu máquina local a la dirección donde vas a guardar el código de este repositorio y corre el siguiente código:

```
git clone git@github.com:ecostichp/Pandas-Practicas.git
```

### 3. Crea un entorno para el proyecto.
Métete a la carpeta que creo el comando anterior (Pandas-Practicas). Dentro de ella crea un entorno que llamaras "env_pandas_practicas".

```
python -m venv env_pandas_practicas
```

### 3. Activa el entorno.
```
env_pandas_practicas\Scripts\activate
```

### 4. Actualiza PIP en tu entorno e instala las dependencias del proyecto.
```
python -m pip install -U Pip  
python -m pip install Pandas iPyKernel OpenPyXL MatPlotLib Seaborn
```
