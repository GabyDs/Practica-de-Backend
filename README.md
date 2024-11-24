# Práctica Backend - Django Tutorial

Una aplicación de encuestas desarrollada siguiendo el tutorial oficial de Django. Esta aplicación permite crear encuestas, votar en ellas y visualizar los resultados.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.8 o superior** 
- **pip** (gestor de paquetes de Python)
- **Virtualenv** (opcional, pero recomendado)

## Instalación

### Clona este repositorio
```bash
git clone https://github.com/GabyDs/Practica-de-Backend.git
cd Practica-de-Backend
```
### Crea y activa un entorno virtual (opcional, pero recomendado)

- En Linux/Mac:

```bash
python3 -m venv env
source env/bin/activate
```

- En Windows:

```bash
python -m venv env
env\Scripts\activate
```

### Instala dependencias
```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto

### Aplica las migraciones iniciales

```bash
python mysite/manage.py migrate
```

### Inicia el servidor de desarrollo

```bash
python mysite/manage.py runserver
```

#### Información Adicional

- Este proyecto sigue el tutorial oficial de Django. Si deseas aprender más, consulta la [documentación oficial de Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/).