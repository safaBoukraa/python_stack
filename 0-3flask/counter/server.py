from flask import flask,render_template,session,redirect, url_for, request
app=flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/',methods=['GED','POST'])
def index():
    if 'counter' not in session :
        session['counter']=1
        
    if request.method == 'POST':
             action = request.form.get('action')
        if action == 'increment':
            session['counter'] += 1
        elif action == 'reset':
            session['counter'] = 1

    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session', methods=['GET', 'POST'])
def destroy_session():
    session.clear()
    return redirect(url_for('index'))




if __name__ =='__main__':
    app.run(debug=True)