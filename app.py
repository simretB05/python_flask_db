from flask import Flask
import json
import dbhelper
app=Flask(__name__)

    @app.get('')
    def ():
        results = dbhelper.run_statement('CAll ()',[])
        if(type(results)==list):
            _json= json.dumps(results,default=str)
            return _json
        else:
            return 'sorry please try again'
    app.run(debug=True)
