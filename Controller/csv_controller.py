import io
import csv
from Model.excel_engine import BANCO_OFERTAS

def normaliza_codigo(raw):
    somente_digitos = ''.join(ch for ch in str(raw) if ch.isdigit())
    return somente_digitos[:6]

def processar_geracao_csv(lista_cursos_input, lista_matriculas_bruta):
    output = io.StringIO()
    escritor = csv.writer(output)
    escritor.writerow(['course_id', 'user_id', 'role', 'status'])
    
    erros = []
    
    for bloco_curso, bloco_matricula in zip(lista_cursos_input, lista_matriculas_bruta):
        codigos = [c.strip() for c in bloco_curso.split('\n') if c.strip()]
        matriculas = [m.strip() for m in bloco_matricula.split('\n') if m.strip()]
        
        if not codigos:
            erros.append("Bloco de cursos vazio")
            continue
        if not matriculas:
            erros.append("Bloco de matrículas vazio")
            continue
        
        for m in matriculas:
            for cod in codigos:
                cod_limpo = normaliza_codigo(cod)
                if not cod_limpo:
                    erros.append(f"Código inválido: '{cod}'")
                    continue
                
                sis_id_final = BANCO_OFERTAS.get(cod_limpo)
                if sis_id_final is None:
                    erros.append(f"Código de curso não encontrado no banco: {cod_limpo}")
                    continue
                
                escritor.writerow([sis_id_final, m, "student", "active"])
    
    csv_data = output.getvalue()
    return csv_data, erros