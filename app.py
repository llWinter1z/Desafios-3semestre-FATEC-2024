from flask import Flask, render_template, request, redirect, url_for, render_template_string
from flask_mysqldb import MySQL

app = Flask("__name__")


#Configuração do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'fabiodb'
mysql = MySQL(app)


@app.route("/")
def sobremim ():
    return render_template ('sobremim.html')

@app.route("/sobremim.html")
def sobremim2 ():
    return render_template ('sobremim.html')

@app.route("/artes.html")
def artes ():
    return render_template ('artes.html')

@app.route("/redes.html")
def redes ():
    return render_template ('redes.html')

# Rota para exibir a lista de tarefas
@app.route('/feedback.html')
def feedback():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM feedbacktb")
    tasks = cur.fetchall()
    cur.close()
    return render_template('feedback.html', tasks=feedback)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        feedback = request.form['feedback']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO feedbacktb (nome, email, feedback) VALUES (%s, %s, %s)", (nome, email, feedback))
        mysql.connection.commit()
        cur.close()
        return render_template('feedbackdone.html', tasks=feedback)
    
# Rota para atualizar uma tarefa
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        feedback = request.form['feedback']
        status = request.form['status']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE feedbacktb SET nome=%s, email=%s, feedback=%s, status=%s WHERE id=%s", (nome, email, feedback, status, task_id))
        mysql.connection.commit()
        cur.close()
        return render_template('feedbackdone.html', tasks=feedback)
    
# Rota para excluir uma tarefa
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM feedbacktb WHERE id=%s", (task_id,))
        mysql.connection.commit()
        cur.close()
        return render_template('feedbackdone.html', tasks=feedback)

if __name__ == '__main__':
    app.run(debug=True)