# Migración a Pipenv

## Resumen

El proyecto ha sido migrado de usar `requirements.txt` con `pip` a usar `pipenv` para la gestión de dependencias. Esto proporciona:

- ✅ **Lock-file reproducible**: `Pipfile.lock` asegura versiones exactas y reproducibles
- ✅ **Separación clara**: Dependencias de producción vs desarrollo
- ✅ **Mejor seguridad**: Detección automática de vulnerabilidades
- ✅ **Gestión simplificada**: Un archivo de configuración único

## Archivos Modificados

### Nuevos archivos:
- **`Pipfile`** - Definición de dependencias y configuración del proyecto
- **`Pipfile.lock`** - Lock-file con versiones exactas resueltas (DEBE estar en control de versiones)

### Archivos actualizados:
- **`Makefile`** - Todos los comandos de pip3 han sido reemplazados por pipenv
- **`Dockerfile`** - Instalación de pipenv y uso de Pipfile/Pipfile.lock
- **`.gitignore`** - Sin cambios (ya tenía configuración adecuada para pipenv)

### Archivo deprecado (pero mantenido para compatibilidad):
- **`requirements.txt`** - Ya no es necesario, pero se mantiene como referencia

## Instalación

### Primera vez (local):

```bash
# Instalar pipenv si no lo tienes
pip3 install pipenv

# Desde el directorio del proyecto
pipenv install --dev
```

### Activar el ambiente virtual:

```bash
pipenv shell
```

O ejecutar comandos dentro del ambiente sin activarlo:

```bash
pipenv run python3 script.py
```

## Comandos Principales

```bash
# Instalar dependencias (después de cambios en Pipfile)
make install
# o
pipenv install --dev

# Actualizar todas las dependencias
make upgrade

# Verificar dependencias obsoletas
make update

# Limpiar el ambiente
make clean

# Ejecutar tests
make test

# Ejecutar linting
make lint

# Cobertura
make coverage
```

## Cambios en el Makefile

| Comando antiguo | Comando nuevo |
|---|---|
| `pip3 install -r requirements.txt` | `pipenv install --dev` |
| `pip3 list --outdated` | `pipenv check` |
| `pip3 freeze > requirements.txt` | `pipenv update` |
| `python3 -m pytest` | `pipenv run python3 -m pytest` |

## Docker

El Dockerfile ha sido actualizado para:
1. Instalar pipenv en la imagen base
2. Usar `Pipfile` y `Pipfile.lock` en lugar de `requirements.txt`
3. Ejecutar `make dependencies` que ahora usa pipenv

```bash
# Construir imagen
docker compose build

# Ejecutar tests en contenedor
docker compose run --rm algorithm-exercises-py-test make test
```

## Beneficios

### Reproducibilidad
- El `Pipfile.lock` contiene exactamente las versiones que fueron instaladas
- Cualquiera que clone el proyecto obtendrá exactamente las mismas versiones

### Seguridad
```bash
pipenv check  # Detecta vulnerabilidades conocidas
```

### Gestión de dependencias
```bash
pipenv update package_name      # Actualizar paquete específico
pipenv graph                    # Ver árbol de dependencias
pipenv requirements             # Generar requirements.txt si es necesario
```

### Desarrollo
- Dependencias de desarrollo separadas en `[dev-packages]`
- Fácil colaboración sin instalar herramientas innecesarias

## Migración desde requirements.txt

Si necesitas volver a generar `Pipfile` desde un `requirements.txt`:

```bash
# Borrar Pipfile y Pipfile.lock actuales
rm Pipfile Pipfile.lock

# Generar nuevos desde requirements.txt
pipenv install --requirements requirements.txt

# Luego regenerar lock
pipenv lock
```

## Referencias

- [Documentación de Pipenv](https://pipenv.pypa.io/)
- [Guía de instalación](https://pipenv.pypa.io/en/latest/install.html)
- [Workflows comunes](https://pipenv.pypa.io/en/latest/workflows.html)
