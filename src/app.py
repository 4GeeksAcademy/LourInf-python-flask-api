from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/") #define ruta (endpoint) y metodo
def hello_world(): #defino mi funcion
    # comando de python
    # return por default si es string, devuelve html
    # return por default si es dict, list, entonces devuelve un json
    response_body = {"mensaje": "hello world",
                     "result": "metodo GET del /"}
    #return "<h1>Hello!</h1>"
    return response_body


#creamos nueva ruta para los todos con metodo GET:
@app.route('/todos' , methods=['GET'])
def handle_todos():
    #return "<h1>Hello!</h1>" #(ejemplo 1: como es un string, me devolvera un html)
    my_json = jsonify(todos)  # Pass the 'todos' list to jsonify
    return my_json


some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

#creamos nueva ruta con metodo POST:
@app.route('/todos', methods=['POST']) #el endpoint es el mismo q en GET, solo cambia el metodo
def add_new_todo():
    #request_body = request.data   #(primero hicimos data) otra forma de escribirlo: data = request.data // data nos da un string. Json un dict
    request_body = request.json 
    #print("Incoming request with the following body", request_body)
    #return 'Response for the POST todo'  #esto lo recibimos en la terminal del back (terminal Python)
#para ejecutar este POST necesito hacerlo desde Postman (y primero tenemos que ponerlo publico para q Postman lo vea, sino me da error 401)
#en el browser no se puede ver un POST, solo un GET. Para ver el POST tenemos que usar herramientas como Postman
    todos.append(request_body) #lo q recibo del front se lo anado a la lista
    response_body = todos
    return response_body

#creamos nueva ruta con metodo DELETE:
@app.route('/todos/<int:position>', methods=['DELETE']) #para el DELETE tenemos que tener un parametro, en este caso lo llamamos position
def delete_todo(position):  #le pasamos la variable que me esta llegando
    print("This is the position to delete: ",position)
    del todos[position] #borramos la todo que le mandamos
    response_body = todos
    return response_body
#en postman pondria el metodo DELETE con la url: https://cautious-bassoon-669rw7rjjxph4wj6-3245.app.github.dev/todos/1  (el 1 es mi parametro que tiene q ser un numero, int, como he definido)
#en la terminal recibire ese 1

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)