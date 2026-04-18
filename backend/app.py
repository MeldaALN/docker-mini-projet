from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route("/api")
def api():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 'Connexion à PostgreSQL réussie ✅';")
        result = cur.fetchone()[0]
        cur.close()
        conn.close()

        return jsonify({
            "message": result
        })
    except Exception as e:
        return jsonify({
            "message": f"Erreur : {str(e)}"
        }), 500

@app.route("/")
def home():
    return jsonify({"message": "Backend Flask en ligne ✅"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)