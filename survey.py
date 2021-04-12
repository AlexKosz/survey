
from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def ma():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name= request.form['name']
    location = request.form['location']
    language = request.form.get('language')
    comment = request.form['comment']

    return render_template("show.html", name=name, location=location, language=language, comment=comment)


if __name__=="__main__":    
    app.run(debug=True)    

