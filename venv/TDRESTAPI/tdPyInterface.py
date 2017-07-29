from flask import Flask, url_for, request, render_template, Response, jsonify
import teradata

app = Flask(__name__)


# routes and methods
@app.route('/')
def index():
    return "Welcome to tdPyInterface"


@app.route('/<qry>', methods=['GET'])
def show_qry_result(qry):
    data = []
    print ("SQL ISSUED : %s" % qry)
    udaExec = teradata.UdaExec(appName="tdPyInterface", version="1.0",
                               logConsole=False, appConfigFile="tdPyInterface.ini")
    session = udaExec.connect(method="odbc", dsn="TDDEV",
                              username="crmp_su", password="crmp_pass")
    for row in session.execute(qry):
        data.append(str(row))

    return jsonify(results=data)

if __name__ == '__main__':
    app.run(debug=True)