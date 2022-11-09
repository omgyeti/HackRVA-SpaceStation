from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      uID = request.form['uID']
      return """
      <!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<style>
			body 	{ padding-top:50px; }
		</style>
		<title>Space Station</title>
	</head>
	<body class="container">
		<header>
			<nav class="navbar navbar-default">
				<div class="container-fluid">
					<div class="navbar-header">
						<a class="navbar-brand" href="/">HackRVA Space Station</a>
					</div>
					<ul class="nav navbar-nav">
						<li><a href="/">Home</a></li>
						<li><a href="/">Lookup/Edit</a></li>
						<li><a href="/">Zones</a></li>
						<li><a href="/">Whats in use</a></li>
					</ul>
				</div>
			</nav>
		</header>
		<main class="text-center">
			<h2>Welcome """+uID+"""</h2>
		</main>
		<footer>
		<p class="text-center text-muted"></p>
		</footer>
	</body>
</html>"""
   else:
      uID = request.args.get('uID')
      return """
      <!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<style>
			body 	{ padding-top:50px; }
		</style>
		<title>Space Station</title>
	</head>
	<body class="container">
		<header>
			<nav class="navbar navbar-default">
				<div class="container-fluid">
					<div class="navbar-header">
						<a class="navbar-brand" href="/">HackRVA Space Station</a>
					</div>
					<ul class="nav navbar-nav">
						<li><a href="/">Home</a></li>
						<li><a href="/">Lookup/Edit</a></li>
						<li><a href="/">Zones</a></li>
						<li><a href="/">Whats in use</a></li>
					</ul>
				</div>
			</nav>
		</header>
		<main class="text-center">
			<form action="http://localhost:5000/" method="post">
				<h2>Enter/Scan ID</h2>
				<label for="uID">ID:</label>
				<input type="text" id="uID" name="uID"><br>
				<input type="submit" value="Submit">
			</form>
		</main>
		<footer>
		<p class="text-center text-muted"></p>
		</footer>
	</body>
</html>"""
if __name__ == '__main__':
   app.run()