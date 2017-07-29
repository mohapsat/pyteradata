# https://developer.teradata.com/tools/reference/teradata-python-module

import teradata
# import logging

# logger = logging.getLogger(__name__)

sql = 'SELECT * from crmp.temp_t'

udaExec = teradata.UdaExec(appName="HelloWorld", version="1.0",
                           logConsole=False)

session = udaExec.connect(method="odbc", dsn="TDDEV",
                          username="***", password="***");

for row in session.execute(sql):
    print(row)
