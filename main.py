from flask import Flask, render_template, request, Response
from Controller.csv_controller import processar_geracao_csv

app = Flask(__name__, 
            template_folder='View/templates', 
            static_folder='View/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-csv', methods=['POST'])
def gerar_csv():
    csv_data, erros = processar_geracao_csv(
        request.form.getlist('cursos[]'),
        request.form.getlist('matriculas[]')
    )
    
    if erros:
        return f"Erros na geração do CSV: " + "<br>".join(erros), 400
    
    res = Response(csv_data, mimetype="text/csv")
    res.headers["Content-Disposition"] = "attachment; filename=matriculas_sis.csv"
    return res

if __name__ == '__main__':
    app.run(debug=True)