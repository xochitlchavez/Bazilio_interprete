from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compilar', methods=['POST'])
def compilar():
    datos = request.json
    codigo_bzl = datos.get('codigo', '')
    accion = datos.get('accion', '')  # 'audio' o 'pdf'

    # Guarda el código en index.bzl
    with open('index.bzl', 'w', encoding='utf-8') as f:
        f.write(codigo_bzl)

    try:
        # Ejecuta el script del intérprete
        proceso = subprocess.run(
            ['python3', 'bazilio.py', 'index.bzl'],
            capture_output=True,
            text=True,
            check=True
        )
        
        if accion == 'audio':
            logs = proceso.stdout + "\n[ÉXITO] 🎵 ¡Melodía procesada y audio listo!"
        else:
            logs = proceso.stdout + "\n[ÉXITO] 📄 ¡Documento PDF generado correctamente!"
            
        return jsonify({'success': True, 'logs': logs})
    
    except Exception as e:
        error_msg = f"Error al procesar:\n{str(e)}"
        if hasattr(e, 'stderr') and e.stderr:
            error_msg += f"\n{e.stderr}"
        return jsonify({'success': False, 'logs': error_msg})

if __name__ == '__main__':
    app.run(debug=True, port=5000)