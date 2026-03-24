from flask import Flask, render_template, request, Response
import io
import csv

app = Flask(__name__, 
            template_folder='View/templates', 
            static_folder='View/static')

@app.route('/')
def index():
    # Renderiza a página inicial (o formulário)
    return render_template('index.html')

@app.route('/gerar-csv', methods=['POST'])
def gerar_csv():
    # Pega os dados enviados pelo formulário HTML
    codigo_cursos = request.form.get('cursos', '').strip().splitlines()
    lista_bruta = request.form.get('matriculas', '').strip().splitlines()

    if not codigo_cursos or not lista_bruta:
        return "Por favor, preencha todos os campos.", 400

    # Gera o CSV na memória (sem salvar arquivo no servidor)
    output = io.StringIO()
    escritor = csv.writer(output)
    escritor.writerow(['course_id', 'user_id', 'role', 'status'])

    for matricula in lista_bruta:
        m_limpa = matricula.strip()
        if m_limpa:
            for curso in codigo_cursos:
                c_limpo = curso.strip()
                if c_limpo:
                    escritor.writerow([c_limpo, m_limpa, "student", "active"])

    # Faz o navegador baixar o arquivo automaticamente
    res = Response(output.getvalue(), mimetype="text/csv")
    res.headers["Content-Disposition"] = "attachment; filename=matriculas_sis.csv"
    return res

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)