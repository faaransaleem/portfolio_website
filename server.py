from flask import Flask,render_template,request
app = Flask(__name__)




@app.route('/')
def my_home():
    return render_template('index.html')

def write_to_file(data):
	with open('webserver\\database.txt', mode='a') as database:
		print('----------')
		print(data)
		name = data['name']
		print(data['name'])
		email = data['email']
		subject = data['subject']
		message = data['message']
		database.write(f"\n{name},{email},{subject},{message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	write_to_file(data)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "Thank you"