## Speech Transcription API

Este es un proyecto básico que utiliza **Flask** y **Vosk** para crear una API que permite la transcripción de archivos de audio en formato **WAV**. La API recibe un archivo de audio, lo procesa utilizando un modelo de reconocimiento de voz entrenado y devuelve el texto transcrito en formato JSON.

### Requisitos

*   **Python 3.x**
*   **Vosk** (para reconocimiento de voz)
*   **Flask** (para la API)
*   **FFmpeg** (solo si usas `pydub` para la conversión de formatos de audio, opcional)

### Instalación

Clona este repositorio en tu máquina local.

Crea un entorno virtual e instala las dependencias:

Instala las dependencias del archivo `requirements.txt`:

Si estás utilizando la versión con conversión de audio (pydub), asegúrate de tener **FFmpeg** instalado en tu sistema y configurado en el **PATH**.

Descarga un modelo de Vosk en español desde [Vosk Models](https://alphacephei.com/vosk/models) y descomprímelo. Actualiza la ruta al modelo en el archivo `app.py` si es necesario.

### Uso

Ejecuta la aplicación Flask:

Usa una herramienta como **Postman** o **cURL** para enviar un archivo de audio **WAV en formato mono** al endpoint `/transcribe`.

**Ejemplo usando cURL**:

**Ejemplo usando Postman**:

*   Método: `POST`
*   URL: `http://localhost:5000/transcribe`
*   Tipo de cuerpo: `form-data`
*   Clave: `audio`, Tipo: `File`, Selecciona un archivo `.wav` válido.

La API devolverá una respuesta JSON con el texto transcrito:

### Consideraciones

*   **Formato de archivo**: Actualmente, la API solo acepta archivos **WAV** en formato **mono**. Si deseas admitir otros formatos, puedes habilitar el uso de `pydub` y FFmpeg para realizar la conversión de audio.

### Dependencias

Las principales dependencias del proyecto son:

*   **Flask**: Framework web para Python.
*   **Vosk**: Reconocimiento de voz offline.
*   **pydub** (opcional): Biblioteca para manejar la conversión de audio (si estás trabajando con múltiples formatos de audio).

### Ejemplo de respuesta JSON
```
{
  "transcription": "Esto es una prueba de audio"
}
```
