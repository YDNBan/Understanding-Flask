from flask import Flask, render_template, request, redirect

app = Flask(__name__)

event_list = {}
event_NAME_list = {"DGC Cultural Kickoff", "ASA APIDA Market", "Yard Fest", "UREC Pool Party", "Lambda Phi Epsilon, Founders Day"}

@app.get('/')
def index():
    error_message = request.args.get('message')
    if error_message != None:
        return render_template('index.html', message=error_message) # Only runs when the user doesn't select an event
    else:
        return render_template('index.html') # Default rendering



@app.get('/registered')
def registered():

    return render_template('registered.html', event_list=event_list)

@app.post('/adding')
def adding():
    this_event = request.form.get('event')
    this_user = request.form.get('name')
    if (this_event not in event_NAME_list):
        return redirect('/?message=Please%20submit%20valid%20event.')
    if(this_user == ''):
        return redirect('/?message=Please%20fill%20out%20all%20forms') # This redirects you to '/' and triggers the if statement
    event_list[this_user] = this_event
    return redirect('/registered') # This redirects you to the app.get(/'registered')

@app.post('/remove')
def remove():
    name = request.form.get('delete') # grab's 'delete' from form
    del event_list[name]
    return redirect('/registered?hidden=hidden')
