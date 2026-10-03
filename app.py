from flask import Flask, send_from_directory, request, jsonify, session
import os, secrets
app=Flask(__name__, static_folder=".", static_url_path="")
app.secret_key=os.environ.get("SECRET_KEY", secrets.token_hex(32))
PIX_KEY="d8bd8cb1-ddcb-464c-a373-c3d8e263f876"
PLANS={"start":{"name":"Start","price":30},"pro":{"name":"Pro","price":60},"presence":{"name":"Presença","price":100}}
@app.get("/")
def home(): return send_from_directory(".", "index.html")
@app.post("/checkout")
def checkout():
    data=request.get_json(silent=True) or {}; p=data.get("plan")
    if p not in PLANS: return jsonify({"error":"Plano inválido"}),400
    session["payment_verified"]=False
    return jsonify({"plan":PLANS[p],"pix_key":PIX_KEY})
@app.get("/contato")
def contato():
    if not session.get("payment_verified"): return send_from_directory(".", "locked.html"),403
    return send_from_directory(".", "contact.html")
@app.get("/api/contato")
def api_contato():
    if not session.get("payment_verified"): return jsonify({"error":"Pagamento não confirmado"}),403
    return jsonify({"contact":os.environ.get("PERSONAL_CONTACT","Configure seu contato no servidor")})
@app.post("/webhook/pix")
def webhook(): return jsonify({"ok":True,"note":"Conecte aqui o webhook oficial do seu provedor Pix."})
if __name__=="__main__": app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
