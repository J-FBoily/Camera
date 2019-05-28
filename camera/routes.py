from camera import camera
from flask import request,render_template
import os

@camera.route('/')
@camera.route('/index',methods=['POST'])
def fget():
    picsDir = os.listdir("static/pics/")
    return render_template("index.html", pics=picsDir)

@camera.route('/form_post',methods=['POST'])
def fpost():
    date = request.form['selectValue']
    picsDir = os.listdir("static/pics/")
    fetchPics = os.listdir("static/pics/" + date)
    return render_template("index.html",fetchedPics=fetchPics, dateDay=date, pics=picsDir)

#@pics.route("/bonjour_get")
#def bonjget():
#	nom = request.args.get('n')
#	prenom = request.args.get('p')
#	return render_template("patronbonjour.html",leprenom=prenom,lenom=nom)