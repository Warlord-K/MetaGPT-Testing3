from flask import Flask, render_template
from portfolio_ai_engineer import PortfolioAIEngineer

app = Flask(__name__)

@app.route('/')
def index():
    portfolio_ai_engineer = PortfolioAIEngineer()
    return render_template('index.html', portfolio_ai_engineer=portfolio_ai_engineer)

if __name__ == '__main__':
    app.run(debug=True)
