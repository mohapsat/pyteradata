from flask import Flask, url_for, request, render_template, Response, jsonify, json
import teradata
from sqlalchemy import create_engine

app = Flask(__name__)


# routes and methods
@app.route('/')
def index():
    return "Welcome to tdPyInterface"


@app.route('/tddev/tplib/<query>', methods=['GET'])
def show_qry_result(query):
    data = []
    print ("SQL ISSUED : %s" % query)
    udaExec = teradata.UdaExec(appName="tdPyInterface", version="1.0",
                               logConsole=False, appConfigFile="tdPyInterface.ini")
    session = udaExec.connect(method="odbc", dsn="TDDEV",
                              username="crmp_su", password="crmp_pass")

    # session = udaExec.connect(method="rest", dsn="TDDEV", username="crmp_su",
    #                             password="crmp_pass")

    for row in session.execute(query):
        data.append(str(row))



    return jsonify(results=data)


@app.route('/tddev/sa/<query>')
def show_sa_results(query):
    # return 'Query issued: %s' % query

    user = 'crmp_user'
    pasw = 'crmp_pass'
    # host = '172.18.48.172'
    dsn = 'tddev'

    td_engine = create_engine('teradata://' + user + ':' + pasw + '@' + dsn + ':22/crmp')
    # return str(td_engine)
    result = td_engine.execute(query)

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)