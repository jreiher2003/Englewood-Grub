from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hello!</body></html>"
				self.wfile.write(output)
				print output
				return
		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)

def main():
	try:
		port = 9090
		server = HTTPServer(('', port), webserverHandler)
		print "My server is running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C to close server connection"
		server.socket.close()

if __name__ == '__main__':
	main()