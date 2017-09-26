from flask import Flask, request 
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



form = """
<!DOCTYPE html>
<html>
	<head>
		<style>
			form {{
				background-color: #eee;
				padding: 20px;
				margin: 0 auto:
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;	
			}}
			textarea{{
				margin: 10px 0;
				width: 540px;
				height: 120px;

			}}
		</style>
	</head>
	<body>
			<form action="/" method="POST" id="encrypted">
					<label> Rotate by:
						<input type="text" name="rot" value=0>
					</label>
					<br>
					<textarea name="text" form="encrypted">{0}</textarea>
					<br>
					<input type="submit"/>
					
			</form>
	</body>
</html>
"""

@app.route('/', methods=["POST"])
def encrypt():
	rot = request.form['rot']
	text = request.form['text']

	print(rot)
	print(text)

	if not is_integer(rot):
		return "Not a valid integer"
		rot = ''
	else:

		return form.format(rotate_string(text, int(rot)))

@app.route('/')
def index():
	return form.format('')

def is_integer(i):
	try:
	 	int(i)
	 	return True
	except ValueError:
		return False






app.run()