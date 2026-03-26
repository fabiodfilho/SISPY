from flask import Flask, render_template, request, Response
import io
import csv

app = Flask(__name__, 
            template_folder='View/templates', 
            static_folder='View/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-csv', methods=['POST'])
def gerar_csv():
    lista_cursos_bruta = request.form.getlist('cursos[]')
    lista_matriculas_bruta = request.form.getlist('matriculas[]')

    if not lista_cursos_bruta or not lista_matriculas_bruta:
        return "Dados insuficientes.", 400

    output = io.StringIO()
    escritor = csv.writer(output)
    escritor.writerow(['course_id', 'user_id', 'role', 'status'])

    for bloco_curso, bloco_matricula in zip(lista_cursos_bruta, lista_matriculas_bruta):
        
        ids_cursos = [c.strip() for c in bloco_curso.split('\n') if c.strip()]
        matriculas = [m.strip() for m in bloco_matricula.split('\n') if m.strip()]

        for m in matriculas:
            for c in ids_cursos:
                escritor.writerow([c, m, "student", "active"])

    res = Response(output.getvalue(), mimetype="text/csv")
    res.headers["Content-Disposition"] = "attachment; filename=matriculas_sis.csv"
    return res

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)