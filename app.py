from flask import Flask
import json
import dbhelper


app=Flask(__name__)

@app.get('/cars')
def get_cars():
    results = dbhelper.run_procedure('CAll  get_cars()',[])
    if(type(results)==list):
        cars_json= json.dumps(results,default=str)
        return cars_json
    else:
        return 'sorry please try again'
    
app.run(debug=True)

