# Api python y Flask

### Instalacion Flask
> pip install flask

### Correr app de Flask
> flask --app main run 

# Comandos de Git Genericos
### Mostrar las ramas
> git branch

    Para salir de consola, usar letra:  
    "q , Q"
   

### Crear nueva rama
> git branch <nombre_nueva_rama>

### Saltar entre ramas
> git checkout <nombre_rama>

### Crear y saltar a una nueva rama
 > git checkout -b <nombre_rama>


### Fucionar Nueva_rama con Main
-    Posicionarse en rama Main:
-   > git marge <nombre_rama>
- Marge con mensaje
    - > git marge <nombre_rama> -m "Mensaje"

### Publicar ramar
> git push -u origin <nombre_rama>

### Borrar una rama
> git branch -d <nombre_rama>
- Borrado forzado de rama 
    - > git brach -D <nombre_rama>

# Api
## Post
- ### Json propuesto 
    - n1, indica el primer numero
    - n2, indica el segundo numero  
    ``` json
    {
        "n1" : 2,
        "n2" : 8 
    }
    ```
---
---
---
# Comandos Tarea1
### Creamos y nos posicionamos en la rama: "Calculadora_201480017"
- > git checkout -b Calculadora_201480017

### Creamos y nos posicionamos en la rama: "info_201480017"
<<<<<<< HEAD
- > git checkout -b info_201480017

### Entrega de primera version
- > git checkout main
- > git pull origin main
- > git tag -a v1.0.0 -m "Tarea1 version 1.0.0"
- > git push -u origin v1.0.0

### Cambio en Produccion "Hotfix"
-  Creamos rama hotfix
    - > git checkout main
    - > git pull origin main
    - > git checkout -b hotfix/endpoint_calculadora
    - creamos las modificaciones necesarias
    - > git add .
    - > git commit -m "se soluciono el error, en la operacion de multiplicacion, sobre endpoint Calculadora_201480017"
    - > git push -u oriign  hotfix/endpoint_calculadora
    - Agregando El tag correspondiente
        - > git checkout main
        - > git pull origin main
        - > git tag -a v2.0.0 -m "Version 2.0.0"
        - > git push -u origin v2.0.0

    
