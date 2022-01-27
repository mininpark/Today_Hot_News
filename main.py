from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__, template_folder='template')

# to read the csv file using the pandas library 
df = pd.read_csv('combined.csv') 
df.to_csv('combined.csv', index=None)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/report") 
def report(): 
    name = request.args.get('name')
    # for making as lowercase
    if name:
        name = name.lower()
    else:
        redirect("/")

	# to read the csv file using the pandas library 
    df = pd.read_csv('combined.csv') 
    return render_template('report.html', tables=[data.to_html()], titles=[''], SearchingBy = name) 


# @ is as decorator to decorate the function under them ./contact  
# dynamc url
#@app.route("/<username>")
#def potato(username):
#    return f"Hello {username} How are you doing"

# debug True is for refreshing automatically
if __name__ =="__main__":
    app.run(host="0.0.0.0", debug=True)
