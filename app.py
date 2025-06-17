from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# DB init
def init_db():
    conn = sqlite3.connect('guestbook.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('guestbook.db')
    c = conn.cursor()
    c.execute('SELECT id, name, message FROM messages')  # include id for delete
    messages = c.fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    name = request.form['name']
    message = request.form['message']
    if name and message:
        conn = sqlite3.connect('guestbook.db')
        c = conn.cursor()
        c.execute('INSERT INTO messages (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    conn = sqlite3.connect('guestbook.db')
    c = conn.cursor()
    c.execute('DELETE FROM messages WHERE id = ?', (message_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
