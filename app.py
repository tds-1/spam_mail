import os
from os import environ
import smtplib
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, jsonify, make_response
import flask
import xlrd

app = Flask(__name__, static_folder="static_dir")


if __name__ == "__main__":
	app.run(debug=True)
	


@app.route("/", methods=["GET"])
def first_page():
	return render_template("addnewvisitor.html")

@app.route("/", methods=["POST"])
def first_page_post():
	MAIL_ID=request.form["email"]
	MAIL_PASSWORD=request.form["password"]
	row=request.form["row"]
	myfile=request.form["myFile"]
	print(MAIL_ID,MAIL_PASSWORD,row,myfile)
	
	print ("---------------------------")
	# print (type(row))
	# print(row)

	loc = (myfile) 
	
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	sheet.cell_value(0, 0) 
	row=int(row)

	for i in range (0,sheet.nrows):
		print (sheet.cell_value(i,row))
		app.config.update(dict(
		    DEBUG = True,
		    MAIL_SERVER = 'smtp.gmail.com',
		    MAIL_PORT = 587,
		    MAIL_USE_TLS = True,
		    MAIL_USE_SSL = False,
		    MAIL_USERNAME = MAIL_ID,
		    MAIL_PASSWORD = MAIL_PASSWORD,
		))
		mymail = Mail(app)
	
		msg = Message("test",#subject
		sender=("Admin", MAIL_ID), 
		recipients=[sheet.cell_value(i,row)],
		body="this is a test mail")
		mymail.send(msg)	

	return render_template("addnewvisitor.html")
