import os
from csv import reader
import pandas as pd
from flask import Flask, redirect, render_template, request
from datetime import date

app = Flask(__name__, template_folder='template')
dirname = os.path.dirname(os.path.abspath(__file__))
headline_file = os.path.join(dirname, 'combined.csv')
headline_list = []

today = date.today()
today_n = today.strftime("%B %d, %Y")

# open file in read mode
with open(headline_file, 'r') as read_obj:
# pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
    #          # row variable is a list that represents a row in csv
        headline_list.append(row)
    df = headline_list[1:]
    #df = pd.DataFrame (data=df, columns=['head','link'])


# homepage
@app.route("/")
def home():
    return render_template('index.html')

# report page
@app.route("/report") 
def report(): 
    name = request.args.get('name')
    # for making as lowercase
    if name:
        name = name.lower()
        #print(headline_list)
    else:
        redirect("/")

    return render_template(
        'report.html', 
        SearchingBy = name,
        resultsNumber = len(df),
        headline_list = df,
        today = today_n
        ) 

#@app.route("/export") 
#def report(): 

# @ is as decorator to decorate the function under them ./contact  
# d/ynamc url
#@app.route("/<username>")
#def potato(username):
#    return f"Hello {username} How are you doing"

# debug True is for refreshing automatically
if __name__ =="__main__":
    app.run(host="0.0.0.0", debug=True)
