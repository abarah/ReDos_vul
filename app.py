from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# Exemple d'expression régulière vulnérable à ReDoS
username_pattern = re.compile(r"^(a+)+b$")  # Vulnérabilité ReDoS ici

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Validation du nom d'utilisateur (vulnérabilité ici)
        if username_pattern.match(username):
            if password == "securepassword":
                message = "✅ Connexion réussie !"
            else:
                message = "❌ Mot de passe incorrect."
        else:
            message = "⚠️ Nom d'utilisateur invalide."

    # Page HTML avec un design amélioré
    page = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Connexion</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 350px;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            form {
                margin-top: 15px;
            }
            input[type="text"], input[type="password"] {
                width: 90%;
                padding: 10px;
                margin: 8px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
            }
            button:hover {
                background-color: #218838;
            }
            .message {
                margin-top: 15px;
                font-size: 16px;
                color: #d9534f;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Connexion</h1>
            <form method="POST">
                <input type="text" name="username" placeholder="Nom d'utilisateur" required>
                <input type="password" name="password" placeholder="Mot de passe" required>
                <button type="submit">Se connecter</button>
            </form>
            <p class="message">{{ message }}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(page, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
