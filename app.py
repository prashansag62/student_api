from flask import Flask,render_template,request
from datetime import datetime
app=Flask(__name__) #value=app if run from another file
@app.route("/") #@-decorator
def index():
	return "Welcome"
	
@app.route("/hello")
def hello1(): 
	print(request.args)
	name="Prashansa"
	data=[["student","class","grade"],
	["ram",9,9],
	["shyam",8,9],
	["ravi",10,10]]
	colors=['red','green','yellow']
	return render_template("test.html", name=name,now=datetime.now().strftime("%d %B,%Y %I:%M %p"),data=data,colors=colors)
@app.route("/form",methods=['GET','POST'])
def submit_data():
	if request.method=='GET':
		return render_template("form.html")
	else:
		name=request.form.get('name')
		clas=request.form.get('class')
		image=request.files.get('image')
		ext=image.filename.split('.')[-1]
		image.save("static/images/{}.{}".format(name,ext))
		#print(request.form)
		#return "submitted!"
		return "your name is {} and class is {}".format(name,clas)
@app.route("/user/<id>/")
def users(id):
	return "your id is {}".format(id)
@app.route("/users/<int:id>/")
def users1(id):
	id+=1
	return "your id is {}".format(id)



if __name__=="__main__":
	app.run(use_reloader=True,debug=True)
