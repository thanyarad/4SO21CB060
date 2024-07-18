from flask import Flask  
  
app = Flask(__name__)  
WINDOW_SIZE=10
THIRD_PART_URL="http://20.244.56.144/test/primes"
TIMEOUT=0.5
window_state=[]
@app.route('/')


def average():  
    return "Average_Calculation";  
  
if __name__ =='__main__':  
    app.run(debug = True)  