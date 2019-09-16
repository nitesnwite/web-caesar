# MAIN.PY
from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
	<!DOCTYPE html>
	<html>
		<head>
			<style>
				form {{
					background-color: linen;
					padding: 25px;
					margin: 0 auto;
					width: 600px;
					font: 16px sans-serif;
					border-radius: 12px;
				}}
				textarea {{
				margin: 15px 0;
				width: 540px;
				height: 150px;
				}}
			</style>
		</head>
		<body>
			<form method='POST'>
				<label>Rotate By: 
				<input name="rot" type="text" value="0" />
				</label>
				<textarea name="text">{0}</textarea>
				<input type="submit" value="Encrypt" />
			</form>
		</body>
	</html>
'''
	

@app.route('/')
	
def index():
	return form.format('')

@app.route('/', methods=['POST'])

def encrypt():
	rot = request.form['rot']
	text = request.form['text']
	message = rotate_string(text, rot)
	return form.format(message) 

app.run()
