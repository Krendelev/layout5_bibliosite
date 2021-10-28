from livereload import Server
from render_website import render

render()

server = Server()
server.watch("template.html", render, delay=2)
server.serve(root="./pages", default_filename="index1.html")
