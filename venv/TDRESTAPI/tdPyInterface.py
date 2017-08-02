from flask import Flask, json
import teradata
import datetime
import logging
from sqlalchemy import create_engine

app = Flask(__name__)


# routes and methods
@app.route('/check')
def index():
    status = "pyTeradata Interface is operating normally!"
    return json.dumps({'status': status}, indent=3)


@app.route('/tddev/tQueryRaw/<query>', methods=['GET'])
def show_tddev_tqueryraw_result(query):
    data = []

    vals = []  # to store data
    cols = []  # to store cols
    master = []  # to store tuples of both

    print ("SQL ISSUED : %s" % query)

    udaExec = teradata.UdaExec(appName="tdPyInterface", version="1.0",
                               logConsole=False, appConfigFile="tdPyInterface.ini")

    session = udaExec.connect("${dataSourceName}")
    cursor = session.execute(query)

    for row in cursor.description:
        cols.append(row[0])

    for row in cursor:
        vals.append(str(row))

    for item in vals:
        data = item[item.find('[') + 1:item.find(']')]
        parts = data.split(',')
        for x, y in zip(cols, parts):
            master.append({x.strip(): y.strip()})

    return json.dumps({'data': master}, indent=3)

    # return jsonify(results=data)


@app.route('/tddev/tQueryFile/<file>', methods=['GET', 'POST'])
def show_tddev_tqueryfile_result(file):
    return "work in progress"


@app.route('/tdprod/tQueryRaw/<query>', methods=['GET', 'POST'])
def show_tdprod_tqueryraw_result(query):
    return "work in progress"


@app.route('/tdprod/tQueryFile/<file>', methods=['GET', 'POST'])
def show_tdprod_tqueryfile_result(file):
    return "work in progress"

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