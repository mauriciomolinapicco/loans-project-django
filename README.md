# Sistema de Gestión de Préstamos

## 📝 Descripción
Sistema desarrollado en Django para gestión de solicitudes de préstamos con:
- Formularios de solicitud para usuarios
- Panel de administración
- Integración con API externa para validación

## ✨ Características principales
- **Para usuarios**:
  - Formulario de solicitud con validación
  - Visualización del estado de solicitud
- **Para administradores**:
  - Panel de gestión completo
  - Edición/eliminación de solicitudes
  - Aprobación manual

## 🛠 Tecnologías
| Tecnología        | Versión   | Uso                                      |
|-------------------|-----------|------------------------------------------|
| Django            | 4.2       | Backend principal                       |
| Tailwind CSS      | 3.3       | Diseño UI                               |
| Python-dotenv     | 1.0       | Manejo de variables de entorno           |
| Docker            | -         | Contenerización de la aplicación        |
| Amazon EC2        | -         | Despliegue en la nube (AWS)             |

### Instalación
Clonar el repositorio:

```bash
git clone https://github.com/mauriciomolinapicco/loans-project-django.git
cd loans-project-django
```

### Configurar el archivo .env:
Por obvias cuestiones de seguridad no subi la API KEY al repositorio por eso hay que configurar un .env:
```ini
API_KEY=codigo_para_api
```

### Construir la imagen Docker
```bash
docker build -t loan-project .
```

### Levantar el container:
```bash
docker-compose up
```
Esto iniciará el servidor en http://127.0.0.1:8001/.

## Uso
Página principal: Los usuarios pueden acceder al formulario de solicitud de préstamo y completar la información.
Panel de administración: Los administradores pueden gestionar las solicitudes, ver detalles, aprobar o rechazar solicitudes, y eliminar registros.

## Pruebas
Se incluyen pruebas unitarias para las vistas de aplicación, como la creación, edición, eliminación y detalles de la solicitud de préstamo.
Para ejecutar las pruebas:
```bash
python manage.py test
```


## Notas
El sistema usa API Key para realizar la validación de CUIL. Asegúrate de configurar correctamente la clave en el archivo .env para que la validación externa funcione.
Los mensajes de error y éxito en la interfaz de usuario están localizados en español para una mejor experiencia del usuario.

## Contribuciones
Si deseas contribuir al proyecto, por favor abre un pull request o un issue para sugerir cambios.

## Licencia
Este proyecto está bajo la licencia MIT.

