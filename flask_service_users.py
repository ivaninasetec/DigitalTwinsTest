#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:03:19 2023

@author: pablo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:06:50 2023

@author: pablo
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for our "Todo" resources
users = [
    
    {'user': 'pcalleja', 'status': 'professor', 'name': 'Pablo', 'classes': [{'name':'Programming'}] },
    {'user': 'dchaves', 'status': 'professor', 'name': 'David', 'classes': [{'name':'Programming'}] },
    {'user': 'dgarijo', 'status': 'professor', 'name': 'Daniel', 'classes': [{'name':'Programming'}] },
    {'user': 'user', 'status': 'student', 'name': 'user', 'classes': [{'name':'Programming'},{'name':'Other'}] },
    
    
    ]


next_todo_id = 4

# Endpoint to get a list of all todos
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)



def find_user(user_id):
    user_find= None
    for us in users:
        if us['user'] == user_id:
            user_find=us
            break
    return user_find

def find_user_pos(user_id):
    user_find= None
    a=0
    for us in users:
        if us['user'] == user_id:
            user_find=a
            break
        a=a+1
    return user_find


# Endpoint to get a single todo by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    
    print('check'+user_id)
    user= find_user(user_id)

    if user is None:
        return  'User not found', 404
    return jsonify(user)

# Endpoint to create a new todo
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = data
    users.append(new_user)
    
    return jsonify(data), 201

# Endpoint to update a todo by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user= find_user_pos(user_id)
    if user is None:
        return 'User not found', 404
    
   
    data = request.get_json()
    users[user]=data
    return jsonify(data)

# Endpoint to delete a todo by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    #todo = todos.pop(todo_id, None)
    user= find_user_pos(user_id)
    print(user)
    if user is None:
        return 'User not found', 404
    
    users.pop(user)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)