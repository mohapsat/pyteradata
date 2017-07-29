from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/project")
def project():
    return "Project Page"


@app.route("/about")
def about():
    return "About Page"


@app.route('/project/<expr>')
def show_expr(expr):
    return 'Current Project is: %s' % expr


@app.route('/runid/<int:runid>')
def show_runid(runid):
    return 'RUNID is: %d' % runid


# @app.route("/login",methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         # login_user()
#         pass
#     else:
#         # show_login_form()
#         pass

if __name__ == '__main__':
    app.run()
