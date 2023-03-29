from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')
	
@app.route('/<string:page_name>')
def other_page(page_name):
	return render_template(page_name)
	
def store_data(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		name = data['name']
		message = data['message']
		file = database.write(f'n Email:{email}, Name:{name}, Message:{message}')
		
def store_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data['email']
		name = data['name']
		message = data['message']
		csv_file = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([name,email,message])
	
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
			data = request.form.to_dict()
			store_data(data)
			store_csv(data)
			return redirect('/submitform.html')
	else:
		return 'Please Try Again'		
			
	

	
	
