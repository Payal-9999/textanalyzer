from flask import Flask, render_template, request


app =Flask (__name__)

@app.get("/")
def showpage():
    return render_template('index.html')

@app.post('/analyze')
def analyze():
    text= request.form['text']
    action=request.form['action']
    answer=""
    if(action == "cntchr"):
        answer =f"The number of characters are:-{len(text)}"
    if(action == "cntws"):
        answer =f"The number of spaces are:-{text.count(' ')}"
    if(action == "cap"):
        answer =f"The text after capitalizing:-{text.capitalize()}"
    if(action == "chkalp"):
        answer =f"The number of Alphabets are:-{text.isalpha()}"
    if(action == "chkdig"):
        answer =f"The number of digits are:-{text.isdigit()}"
    if(action == "chklow"):
        answer =f"The number of lowercase are:-{text.islower()}"
    if(action == "chkupp"):
        answer =f"The number of uppercase are:-{text.isupper()}"
    if(action == "conlow"):
        answer =f"covert into lowercase:-{text.lower()}"
    if(action == "conupp"):
        answer =f"convert into uppercase:-{text.upper()}"
    if(action == "endsp"):
        answer =f"ending space from right:-{text.rstrip()}"
    if(action == "rmvsp"):
        answer =f"Removing starting and ending spaces :-{text.strip()}"
    if(action == "chkwdnm"):
        answer =f"checking words and name :-{text.isalnum()}"
    
    return render_template('index.html', output = answer)


app.run(debug=True)
