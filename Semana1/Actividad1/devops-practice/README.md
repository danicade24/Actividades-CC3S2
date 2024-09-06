# Instrucciones de la actividad

## 1. Configuración del entorno

### Descripción del proyecto

Este proyecto consiste en una aplicación web sencilla creada con Node.js. La aplicación incluye una API REST básica con un único endpoint que devuelve un mensaje de "Hello, World!".

### Pasos para configurar el entorno

#### 1.1 Inicializa el proyecto 

```bash
mkdir devops-practice
cd devops-practice
npm init -y
```
Creamos un nuevo directorio llamado devops-practice, nos movemos a ese directorio y inicializamos un nuevo proyecto de Node.js con un archivo package.json predeterminado.

![package.json creado](docs/image1.png)

#### 1.2. Instala las Dependencias Necesarias

Comando:

```bash
npm install express jest supertest
```
Instalamos express para crear la API y jest para las pruebas unitarias. Supertest se usa para realizar pruebas sobre los endpoints de la API.

![instalación de dependencias](docs/image2.png)


#### 1.3. Crea la estructura del proyecto:
```bash
mkdir src tests
touch src/app.js tests/app.test.js
```

![Estrucutura del proyecto](docs/image3.png)

#### 1.4. Implementa la API REST en src/app.js:

```bash
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/delay', (req, res) => {
    setTimeout(() => {
        res.send('This was delayed by 2 seconds');
    }, 2000);
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 3000; 
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}
```

#### 1.5. Escribe un test básico en tests/app.test.js
```bash
const request = require('supertest');
const app = require('../src/app');

describe('GET /', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0); // Usar 0 permite al sistema asignar un puerto libre automáticamente
    });

    afterAll(() => {
        server.close(); // Cierra el servidor después de que las pruebas hayan terminado
    });

    it('should return Hello, World!', async () => {
        const res = await request(app).get('/');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('Hello, World!');
    });
});

describe('GET /delay', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0); // Usar 0 permite al sistema asignar un puerto libre automáticamente
    });

    afterAll(() => {
        server.close(); // Cierra el servidor después de que las pruebas hayan terminado
    });

    it('should return after a delay', async () => {
        const start = Date.now();
        const res = await request(app).get('/delay');
        const end = Date.now();
        const duration = end - start;
        
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('This was delayed by 2 seconds');
        expect(duration).toBeGreaterThanOrEqual(2000);
    });
});

```

#### 1.6. Configura el Script de Test en package.json
```bash
{
  "name": "devops-practice",
  "version": "1.0.0",
  "main": "src/app.js",
  "scripts": {
    "test": "jest --detectOpenHandles"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "supertest": "^6.3.4"
  }
}
```
Se agregó `--detectOpenHandles` para detectar que las funciones asíncronas que seguían ejecutándose después de los tests.

#### 1.7. Ejecución de test
Para verificar que la aplicación funciona bien ejecutamos las pruebas en el terminal con `npm test`

![Tests realizados](docs/image4.png)


### 2. Pipeline CI/CD

 **Parte 1: Configuración de Integración Continua (CI) con GitHub Actions**

2.1. Crea un Archivo de Configuración para GitHub Actions

```bash
mkdir -p .github/workflows
touch .github/workflows/ci.yml
```

#### 2. Define el flujo de trabajo en `.github/workflows/ci.yml`:

```bash
name: CI Pipeline
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'

      - name: Install dependencies
        run: npm install
        working-directory: Semana1/Actividad1/devops-practice

      - name: Build Docker image
        run: docker build -t devops-practice Semana1/Actividad1/devops-practice

      - name: Run tests
        run: npm test
        working-directory: Semana1/Actividad1/devops-practice

      - name: Run Docker container
        run: docker run -d -p 3000:3000 devops-practice
```
Configuramos un flujo de trabajo para GitHub Actions que instala las dependencias y ejecuta los tests en cada `push` o `pull request` a la rama `main`.

#### 2.3. Sube el Código a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
![Proyecto subido a Github](docs/image6.png)

**Parte 2: Configuración de Entrega Continua (CD) con Docker**

#### 2.4. Crea un Archivo Docker para Contenerizar la Aplicación

```bash
# Usa la imagen oficial de Node.js
FROM node:14

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "src/app.js"]
```

Para crear el archivo `Dockerfile` nos ubicamos en la raíz del proyecto `$ devops-practice` y colocamos:
```bash
touch Dockerfile
nano Dockerfile
```
El primero crea el archivo y el segundo nos permite editar el contenido del archivo. 
![Archivo Dockerfile](docs/image7.png)

#### 2.5. Construye la Imagen de Docker

```bash
docker build -t devops-practice .
```

#### 2.6. Corre el Contenedor Localmente

```bash
docker run -p 3000:3000 devops-practice
```

![Construcción y ejecución del contenedor](docs/image8.png)

Abre un navegador web y accede a http://localhost:3000 para verificar que la aplicación esté funcionando.

![Ejecución del contenedor](docs/image9.png)


### 3. Automatización
- Automatiza la configuración y gestión del entorno local usando Docker Compose:

#### 3.1. Crea un archivo `docker-compose.yml`

```bash
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```

#### 3.2. Corre la Aplicación Usando Docker Compose:

Ejecuta el siguiente comando para construir la imagen y levantar el contenedor en segundo plano:

```bash
docker-compose up --build -d
```

![Construción del docker-compose](docs/image11.png)


- **Importante**: Antes de ejecutar este comando, asegúrate de que el puerto 3000 esté disponible. Si el puerto está ocupado, podrías recibir un error.

#### Pasos para liberar el puerto 3000:

Lista los contenedores activos:
```bash
docker ps
```

Detén los contenedores que usan el puerto 3000:
```bash
docker stop <container_id>
```
Forzar el cierre de contenedores:

```bash
docker kill <container_id>
```

También puedes usar el siguiente comando:

```bash
sudo lsof -i :3000
```
Lista los procesos que ocupan el puerto 3000. Para detener este proceso, usa el PID (ID del proceso) mostrado en la salida de `lsof`:

```bash
sudo kill -9 <PID>
```
Fuerza el cierre del proceso.

### Github Actions

Podemos observar como se completó exitosamente el proceso todos los trabajos en el archivo ci.yml se ejecutaron sin errores. Para ello tuvimos que añadir el campo `working-directory` en las etapas `Install dependencies` y `Run tests` para especificar la ruta correcta donde se encuentran los archivos del proyecto dentro del repositorio. Esto garantiza que los comandos  `npm install` y `npm test` se ejecuten en el contexto adecuado.

![](docs/image12.png)

### Conclusión

Pudimos ver los beneficios que nos trae usar un pipeline automatizado vimos que al automatizar la construcción, prueba y despliegue se garantiza que los procesos se realicen de manera uniforme en cada commit o pull request. Además, se facilita la detección temprana de errores mediante la ejecución automática de pruebas o tests, lo que nos ayuda a idetificar y corregir problemas antes de que lleguen a producción minimizando así los riesgos. La automatización también mejora la colaboración entre equipos de desarrollo y operaciones, porque permite que ambos equipos se puedan concentrar en sus respectivas áreas sin preocuparse por la integración continua(CI). Al ofrecernos escalabilidad y flexibilidad ya que puede adaptarse a diferentes entornos y configuraciones reduce significativamente el tiempo requerido para construir, probar y desplegar aplicaciones, acelerando así la entrega del proyecto.