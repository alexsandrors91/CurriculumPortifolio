from flask import Flask, render_template_string

app = Flask(__name__)

html_portfolio = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Portfólio - Alexsandro Ribeiro</title>
    <style>
        body {
        margin: 0;
        padding: 0;
        font-family: "Inter", Arial, sans-serif;
        background-color: #0d1117;
        color: #e6edf3;
        line-height: 1.6;
    }

    .container {
        width: 90%;
        max-width: 900px;
        margin: auto;
        padding-top: 40px;
    }

    /* ======== TITULOS ======== */
    h1, h2, h3 {
        color: #58a6ff;
        font-weight: 600;
    }

    /* ======== CARDS ======== */
    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.1);
        border: 1px solid #21262d;
    }

    .project {
        margin-bottom: 20px;
    }

    /* ======== LINKS ======== */
    a {
        color: #79c0ff;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* ======== BADGES DE HABILIDADES ======== */
    .skills {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .skill-badge {
        background-color: #21262d;
        padding: 8px 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        font-size: 14px;
    }

    /* ======== RODAPÉ ======== */
    footer {
        text-align: center;
        margin-top: 30px;
        padding: 20px;
        color: #8b949e;
    }

    </style>
</head>
<body>

<div class="container">

    <h1>Alexsandro Ribeiro da Silva</h1>
    <p>Desenvolvedor Web | Python | React | Automação de Processos</p>

    <div class="card">
        <h2>Sobre mim</h2>
        <p>
            Profissional com experiência sólida em automação e sistemas supervisórios, 
            migrando com sucesso para o desenvolvimento de software. Trabalho com 
            React, JavaScript, Python e SQL, criando aplicações escaláveis e automatizadas.  
            Tenho facilidade em integração entre sistemas e foco em soluções práticas para negócios.
        </p>
    </div>

    <div class="card">
        <h2>Contato</h2>
        <p><strong>Telefone:</strong> (11) 97770-7765</p>
        <p><strong>Email:</strong> Alexsandrors91@gmail.com</p>
        <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/alexsandroribeiro" target="_blank">abrir</a></p>
        <p><strong>GitHub:</strong> <a href="https://github.com/alexsandrors91" target="_blank">abrir</a></p>
    </div>

    <div class="card">
        <h2>Habilidades</h2>
        <div class="skills">
            <span class="skill-badge">HTML</span>
            <span class="skill-badge">CSS</span>
            <span class="skill-badge">JavaScript</span>
            <span class="skill-badge">React</span>
            <span class="skill-badge">Python</span>
            <span class="skill-badge">SQL</span>
            <span class="skill-badge">VBA</span>
            <span class="skill-badge">Web Scraping</span>
            <span class="skill-badge">APIs</span>
            <span class="skill-badge">SCADA</span>
            <span class="skill-badge">Automação Industrial</span>
            <span class="skill-badge">CLP</span>
        </div>
    </div>

    <div class="card">
        <h2>Experiência Profissional</h2>

        <div class="project">
            <h3>São Vicente Contabilidade – Desenvolvedor de TI (Fev/2025 – Mai/2025)</h3>
            <ul>
                <li>Desenvolvimento de sistema interno com React e JavaScript</li>
                <li>Criação de automações e web scraping em Python</li>
                <li>Automação de planilhas com VBA</li>
            </ul>
        </div>

        <div class="project">
            <h3>Brato Engenharia – Técnico de Automação Pleno (Jun/2024 – Fev/2025)</h3>
            <ul>
                <li>Integração entre automação industrial e TI</li>
                <li>Análise de sistemas SCADA e redes industriais</li>
                <li>Programação de CLPs</li>
            </ul>
        </div>

        <div class="project">
            <h3>Microblau Automação – Técnico de Automação Jr. (Jul/2023 – Jun/2024)</h3>
            <ul>
                <li>Implantação de sistemas automatizados</li>
                <li>Avaliação de sistemas SCADA</li>
                <li>Integração de dispositivos inteligentes</li>
            </ul>
        </div>
    </div>

    <div class="card">
        <h2>Educação</h2>
        <ul>
            <li><strong>UNICID — Engenharia Elétrica (2012–2016)</strong></li>
            <li><strong>DNC — Formação em Dados (2023–2024)</strong></li>
            <li><strong>DNC — Front End (2024–Atual)</strong></li>
        </ul>
    </div>

</div>

<footer>
    © 2025 Alexsandro Ribeiro — Portfólio Profissional
</footer>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(html_portfolio)

if __name__ == "__main__":
    app.run(debug=True)
