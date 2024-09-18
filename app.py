from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import wave
import os
import json
from pydub import AudioSegment

app = Flask(__name__)

# Cargar el modelo Vosk preentrenado
model = Model(r"C:\Users\..\vosk-model-small-es-0.42\vosk-model-small-es-0.42")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Leer el archivo en memoria para verificar que tiene contenido
    file_content = audio_file.read()
    if not file_content:
        return jsonify({'error': 'The audio file is empty'}), 400

    # Restablecer el puntero de lectura
    audio_file.seek(0)

    # Guardar el archivo temporalmente
    audio_path = "temp.wav"
    audio_file.save(audio_path)

    try:
        # Convertir el archivo a mono si es necesario
        audio = AudioSegment.from_wav(audio_path)
        if audio.channels > 1:
            audio = audio.set_channels(1)  # Convertir a mono
            audio.export(audio_path, format="wav")  # Sobrescribir el archivo convertido

        # Procesar el archivo de audio
        with wave.open(audio_path, "rb") as wf:
            recognizer = KaldiRecognizer(model, wf.getframerate())

            # Transcribir el audio
            result = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result += recognizer.Result()

            result += recognizer.FinalResult()

        # Convertir el resultado en un diccionario de Python
        final_result = json.loads(result)

        # Retornar solo el campo "text" del resultado
        return jsonify({'transcription': final_result.get('text', '')})

    except wave.Error as e:
        return jsonify({'error': str(e)}), 400

    except EOFError:
        return jsonify({'error': 'Unexpected end of file. Please upload a valid audio file'}), 400

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == '__main__':
    app.run(debug=True)
