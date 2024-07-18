from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def average():  
    return "Average_Calculation";  
  
if __name__ =='__main__':  
    app.run(debug = True)  