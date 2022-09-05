from dalai_app.config.MySQLConnection import connectToMySQL
from dalai_app import app 
from datetime import date, datetime
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, users_id, first_name, last_name, email, users_password, created_at):
        self.users_id = users_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.users_password = users_password
        self.created_at = created_at


    @classmethod
    def user_Registration(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, users_password, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(encryptedpassword)s, SYSDATE(), SYSDATE());"
        data2 = {
            "first_name" : data[0],
            "last_name" : data[1],
            "email" : data[2],
            "users_password" : data[3],
            "encryptedpassword" : data[4],
            "confirm_users_password" : data[5]
        }
        result = connectToMySQL('project_app').query_db( query, data2 )
        print("RESULT LOGIN", result)
        return result
    


    @classmethod
    def user_login(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data2 = {
            "email" : data[0],
            "users_password" : data[1],
        }
        result = connectToMySQL('project_app').query_db( query, data2 )
        return result


    @classmethod
    def get_userInformationBy_id( cls, data ):
        query = "SELECT * FROM users WHERE users_id = %(id)s;"
        results = connectToMySQL('project_app').query_db( query, data )
        print("RESULT USER BY ID", results)
        
        user = []
        for n in results:
            user.append( User( n['users_id'], n['first_name'], n['last_name'], n['email'], n['users_password'], n['created_at'] ) )
        return user



    @classmethod 
    def get_all_users( cls, data ):
        query = "SELECT * FROM users WHERE users_id != %(users_id)s ORDER BY first_name;"
        results = connectToMySQL('project_app').query_db(query,data)
    
        users = []
        for n in results:
            users.append( User( n['users_id'], n['first_name'], n['last_name'], n['email'], n['users_password'], n['created_at'] ) )
        return users



    @classmethod
    def delete_user_account(cls, id):
        data = {
            "id" : id
        }
        query = "DELETE FROM users WHERE users_id = %(id)s;"
        result2 = connectToMySQL('project_app').query_db( query, data )

        query = "DELETE FROM posts WHERE user_id = %(id)s;"
        result = connectToMySQL('project_app').query_db( query, data )

        query = "DELETE FROM likes WHERE user_id = %(id)s;"
        result1 = connectToMySQL('project_app').query_db( query, data )
        return result, result1, result2


    @classmethod
    def get_user_to_validate( cls, username ):
        query = "SELECT * FROM users WHERE username=%(username)s;"
        data = {
            "username" : username
        }
        result = connectToMySQL( "project_app" ).query_db( query, data )
        return result



    @staticmethod
    def validate_login():
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Email no válido")
            is_valid = False
        if len(data['users_password']) < 9:
            flash("La constraseña debe tener más de nueve caracteres")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_registration(data):
        isValid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data2 = {
            "first_name" : data[0],
            "last_name" : data[1],
            "email" : data[2],
            "users_password" : data[3],
            "encryptedpassword" : data[4],
            "confirm_users_password" : data[5]
        }
        results = connectToMySQL('project_app').query_db( query, data2 )
        print("FROM VALIDATE REGISTRATION: ", results)
        if len(results)>=1:
            flash("Este correo ya fue registrado")
            print("Este correo ya fue registrado")
            isValid = False
        if len( data[0] ) < 4:
            flash( "Su nombre debe tener al menos 4 caracteres" ),
            print( "Su nombre debe tener al menos 4 caracteres" )
            isValid = False 
        if len( data[1] ) < 4:
            flash( "Su apellido debe tener al menos 4 caracteres")
            isValid = False
        if not EMAIL_REGEX.match(data[2]):
            flash("Su correo tiene un formato inválido"),
            print("Su correo tiene un formato inválido")
            isValid = False
        if len(data[3]) < 10:
            flash("Su contraseña debe tener más de 10 caracteres"),
            print("Su contraseña debe tener más de 10 caracteres")
            isValid = False
        if data[3] != data[5]:
            flash("Las contraseñas no coinciden"),
            print("Las contraseñas no coinciden")
            isValid = False
        if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0:
            flash("Falta información"),
            print("Falta información")
            isValid = False
        return isValid


