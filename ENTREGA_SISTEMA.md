# 🏢 Manual de Entrega y Operación del Sistema: Amelia RTA 2.0

Este documento contiene toda la información necesaria para que la empresa asuma el control del software, garantizando su funcionamiento automático y explicando cómo realizar modificaciones futuras.

---

## ☁️ 1. Funcionamiento y Arquitectura del Sistema
El sistema opera de forma **100% autónoma en la nube (sin costos de mantenimiento)**:
1. **GitHub Pages (Hospedaje)**: Muestra el dashboard interactivo (`index.html`) en la web.
2. **GitHub Actions (Actualizador en la Nube)**: Un servidor virtual gratuito que ejecuta automáticamente el script `actualizador_rta.py` **todos los lunes a las 8:00 AM (COT)**.
3. **Base de Datos Dinámica (`data.json`)**: Contiene el histórico de todas las semanas y la configuración de los **24 canales B2B**. Se lee de forma asíncrona mediante `fetch()`.

---

## 📦 2. Cómo Transferir el Software a la Empresa (Handover)

### Paso A: Transferir el Repositorio de GitHub
Para que el software pertenezca a la cuenta corporativa de la empresa:
1. Inicia sesión en **GitHub** con tu cuenta actual.
2. Entra al repositorio del proyecto.
3. Ve a la pestaña **Settings** (Configuración) -> Desplázate hasta abajo a la sección **Danger Zone**.
4. Haz clic en **Transfer ownership** (Transferir propiedad).
5. Escribe el nombre de usuario de GitHub de la empresa o de la Organización corporativa y acepta la transferencia.
6. El nuevo administrador corporativo recibirá una invitación por correo para aceptar el repositorio.

### Paso B: Configurar la IA de Gemini (Opcional)
Si la empresa desea utilizar el modo inteligente con IA para redactar los discursos de venta y análisis semanales:
1. Crea una cuenta gratuita en [Google AI Studio](https://aistudio.google.com/).
2. Genera una **API Key** gratuita.
3. En el repositorio de GitHub de la empresa, ve a **Settings** -> **Secrets and variables** -> **Actions**.
4. Haz clic en **New repository secret** (Nuevo secreto del repositorio).
5. Nómbralo exactamente `GEMINI_API_KEY` y pega la clave de Google.
*Nota: Si no configuran esta clave, no hay problema. El sistema cuenta con un generador lógico en Python que simulará y creará datos coherentes de forma gratuita para siempre.*

---

## 🛠️ 3. Cómo Realizar Cambios en el Futuro

Cualquier persona autorizada en la empresa puede realizar modificaciones directamente desde el navegador (sin instalar programas) o clonando el proyecto:

### A. Modificar la Lista de Canales de Venta (Clientes B2B)
Si en el futuro se añade un nuevo cliente, se elimina uno o cambian sus páginas web:
1. Abre el archivo `actualizador_rta.py` (puedes editarlo en la web de GitHub presionando la tecla `.` para abrir el editor online).
2. Busca el diccionario `CLIENTS_RAW_DATA` (cerca de la línea 15).
3. Añade, edita o elimina la información del cliente siguiendo la estructura:
```python
    "NOMBRE DEL CANAL": {
        "short_name": "Nombre Corto",
        "url_menu": "https://url-del-canal.com",
        "urls_ingesta": ["https://url-del-canal.com"],
        "base_traffic": 80,  # Tráfico base del 10 al 100
        "own_brand": 30.0,   # % de marca propia
        "country": "País",
        "cities": [
            {"ciudad": "Nombre Ciudad", "es_costera": True o False, "humedad_relativa_promedio": 80}
        ],
        ...
    }
```
4. Guarda y confirma el cambio (Commit). El sistema en la nube correrá automáticamente y adaptará la interfaz.

### B. Forzar una Actualización Inmediata (Manual)
Si no deseas esperar al lunes por la mañana y quieres ver reflejado un cambio de inmediato:
1. Ve a la pestaña **Actions** en tu repositorio de GitHub.
2. En la barra lateral izquierda, haz clic en **Actualizar Dashboard Amelia RTA**.
3. Haz clic en el botón desplegable **Run workflow** (Ejecutar flujo) a la derecha y presiona **Run workflow** en color verde.
4. El servidor compilará todo en unos 30 segundos y actualizará la página web de inmediato.

---

## 👤 4. Credenciales de Acceso a Entregar
* **Cuenta de GitHub**: `[Entregar usuario y contraseña o transferir repositorio]`
* **Enlace Público del Dashboard**: `https://[organización-o-usuario].github.io/Amelia-2.0_V1FINAL/`
