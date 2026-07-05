from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Aquí podríamos conectar una base de datos en el futuro.
    # Por ahora, renderiza directamente nuestra landing page de ventas.
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecuta la aplicación en modo desarrollo
    app.run(debug=True)