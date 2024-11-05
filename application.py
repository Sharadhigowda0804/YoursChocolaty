from flask import Flask, render_template, request, redirect, url_for
from database import connect_db

app = Flask(__name__)

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavors")
    flavors = cursor.fetchall()
    conn.close()
    return render_template('index.html', flavors=flavors)

@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        flavor_id = request.form['flavor_id']
        customer_name = request.form['customer_name']
        allergies = request.form['allergies']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO suggestions (flavor_id, customer_name, allergies) VALUES (?, ?, ?)",
                       (flavor_id, customer_name, allergies))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('suggestion.html')

if __name__ == '__main__':
    app.run(debug=True)
