
# Práctica #5 - Consumo de API con HTML y JavaScript

La Práctica #5 agrega un endpoint que devuelve una lista de velas y una página
HTML que consulta dicho endpoint mediante la función `fetch()`.

## Endpoint utilizado

**Método:** GET

```text
/estudiantes/api/v1/velas
```

## Ejecución

1. Ubicarse en la carpeta:

```bash
cd estudiantes/data/v1
```

2. Ejecutar la API:

```bash
py run.py
```

3. Sin cerrar la terminal de la API, abrir en el navegador el archivo:

```text
estudiantes/data/v1/practica5/index.html
```

La página realiza una petición a la API y muestra todas las velas recibidas
en una tabla creada dinámicamente con JavaScript.
