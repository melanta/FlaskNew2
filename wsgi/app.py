from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
#from flask.ext.cors import CORS


app = Flask(__name__)
#CORS(app)

registroAlunni = {0:{"numeroReg":0,"nome":"ignoto","cognome":"ignoto","annoNascita":"1900"}}

@app.route("/")
def hello():
    return send_from_directory('.', 'index.html')

@app.route("/test")
def test():
    return send_from_directory('.', 'indexTest.html')

@app.route("/js/<nomeFileJs>")
def jsLoad(nomeFileJs):
    return send_from_directory('js', nomeFileJs)

@app.route("/css/<nomeFileCss>")
def cssLoad(nomeFileCss):
    return send_from_directory('css', nomeFileCss)
   
@app.route("/insertAlunno/")  # metodo GET per chiamare dalla barra del browser
def inserisciAlunno ():
    # spedizione in formato html
    numeroReg =  request.args.get('numeroReg')
    nome =       request.args.get('nome')
    cognome =    request.args.get('cognome')
    annoNascita =request.args.get('annoNascita') 
    dizAlunno = { "numeroReg": numeroReg, "nome": nome,
                  "cognome" : cognome , "annoNascita":annoNascita}
    registroAlunni[int(numeroReg)]= dizAlunno
    return "OK"   #restituisce status = 200  OK , ma nessuna stringa
    
    
@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato html
    
    numeroReg =  request.json['numeroReg']
    
    dizAlunno = registroAlunni[int(numeroReg)]
    # in casi piu' complessi usare render_templates e quindi jsonify
    return jsonify( ** dizAlunno)   #aggiunge content-type => json

@app.route("/insertAlunnoPOST/", methods = ["POST"])
def inserisciAlunnoPOST():
    
    numeroReg =     request.json['numeroReg']
    nome =          request.json['nome']
    cognome =       request.json['cognome']
    annoNascita =   request.json['annoNascita']
    
    dizAlunno = {"numeroReg" : numeroReg, "nome" : nome, 
                "cognome" : cognome, "annoNascita"  : annoNascita}
                
    registroAlunni[int(numeroReg)]= dizAlunno
    print dizAlunno
    print registroAlunni[int(numeroReg)]
    return jsonify("")
    
if __name__ == "__main__":
    #app.debug=True
    app.run()
