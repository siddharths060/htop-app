from flask import Flask
import subprocess
import pytz
from datetime import datetime
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    full_name = "Siddharth S"  
    
   
    system_username = getpass.getuser()
    
   
    ist = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    
   
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    
  
    return f"""
    <html>
      <body>
        <h1>HTOP Output</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {system_username}</p>
        <p><strong>Server Time (IST):</strong> {current_time_ist}</p>
        <pre>{top_output}</pre>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
