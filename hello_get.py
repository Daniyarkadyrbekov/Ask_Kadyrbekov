from cgi import parse_qs

def application(env, start_responce):
	query = parse_qs(env['QUERY_STRING'], keep_blank_values=True)
	body = []
	body.append('<h1>Hello, World!</h1>' + "<br>")

	for key, values in query.items():
		for item in values:
			body.append(key + ' = ' + item + "<br>")


	start_responce('200 OK', [('Content-Type', 'text/html')])

	return body
