from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return "🌱 Agro App funcionando no Render!"

# Exemplo de rota para cálculo
@app.route('/calculo', methods=['POST'])
def calculo():
    try:
        area = float(request.form.get('area'))
        concentracao = float(request.form.get('concentracao')) / 100
        dose = float(request.form.get('dose'))

        total_produto = area * dose
        ingrediente_ativo = total_produto * concentracao

        return {
            "total_produto": total_produto,
            "ingrediente_ativo": ingrediente_ativo
        }
    except Exception as e:
        return {"erro": str(e)}

if __name__ == "__main__":
    # Render exige host 0.0.0.0 e porta vinda da variável PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)