from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pegando os dados do formulário
        try:
            area = float(request.form['area'])
            dose = float(request.form['dose'])
            concentracao = float(request.form['concentracao'])
        except ValueError:
            return render_template('index.html', mensagem="Por favor, insira números válidos!")

        # Cálculos
        total_produto = area * dose
        ingrediente_ativo = total_produto * (concentracao / 100)

        # Formatar números (separador de milhar e 2 casas decimais)
        total_produto_fmt = f"{total_produto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        ingrediente_ativo_fmt = f"{ingrediente_ativo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Mensagem formatada
        mensagem = (
            f"✅ <b>Resultado do cálculo</b><br>"
            f"📍 Área: <b>{area} ha</b><br>"
            f"🧪 Concentração: <b>{concentracao}%</b><br>"
            f"💧 Dose: <b>{dose} kg/ha</b><br>"
            f"📦 <b>Total de produto</b>: <b>{total_produto_fmt} kg</b><br>"
            f"🔬 <b>Ingrediente ativo</b>: <b>{ingrediente_ativo_fmt} kg</b>"
        )

        return render_template('index.html', mensagem=mensagem)

    return render_template('index.html')


if __name__ == '__main__':
    # Rodar na rede local, porta 5000
    app.run(host="0.0.0.0", port=5000)