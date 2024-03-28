from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    plt.plot(x, y)
    
    # Enregistrer le graphique sous forme d'image dans le dossier statique de Flask
    graph_filename = 'static/sine_wave_plot.png'
    plt.savefig(graph_filename)
    
    # Rendre le modèle HTML et passer le nom du fichier graphique comme argument
    return render_template('index.html', graph_filename=graph_filename)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contat():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)

