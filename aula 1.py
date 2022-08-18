from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")


    

def main():

    def vazio(primeira):
        if primeira == None:
            return 1
        else:
            return 0
        

    def media(primeira,segunda,terceira,quarta,quinta):
        b = [primeira,segunda,terceira,quarta,quinta]

        a = 10000
        c = 0

        for i in range(len(b)):
            if b[i] < a:
                a = b[i]
            
        b.remove(a)

        for j in range(len(b)):
            c = c + b[j]

        c = c/4
        
        return c

    resultado = None

    

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')
    terceira = request.args.get('terceira')
    quarta = request.args.get('quarta')
    quinta = request.args.get('quinta')

    if vazio(primeira) == False:
        primeira = float(primeira)
    if vazio(segunda) == False:
        segunda = float(segunda)
    if vazio(terceira) == False:
        terceira = float(terceira)
    if vazio(quarta) == False:
        quarta = float(quarta)
    if vazio(quinta) == False:
        quinta = float(quinta)  

    try:
        media = media(primeira,segunda,terceira,quarta,quinta)
    except TypeError:
        media = -1

    try:
        if media >= 7:
            resultado = 'O maluco é um genio! Aprovado'
        elif media >= 4:
            resultado = 'Reprovado'
        elif media < 0:
            resultado = 'Erro'
        else:
            resultado = 'Reprovado e Banido'
    except TypeError:
        return render_template('index.html')
    

    return render_template('index.html', media=media, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
 
