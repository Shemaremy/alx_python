from flask import Flask, render_template

app = Flask(__name__)

@app.route("/flacko/")
def basic_html():
    return render_template('mypage.html')
    
if __name__=='__main__' :
    app.run(host='0.0.0.0', debug = True)
    


'''
In the above code, we wanted to run an html
webpage which is in a file called mypage using
python. 

We import a class called render_template always
And instead of returning a normal prompt, we 
return that html page we created 

'''
