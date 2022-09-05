from flask import render_template, request, session, redirect
from dalai_app import app
from dalai_app.models.User import User
from dalai_app.models.Postu import Postu
from dalai_app.models.Like import Like


from flask_bcrypt import Bcrypt


@app.route( "/home/post", methods = ['POST'] ) 
def sendPostu():
    if 'users_id' not in session:
        return redirect('/logout')
    posts_content = request.form['posts_content']
    user_id = request.form['users_id']

    data = (posts_content, user_id)

    print("FROM FORM 3 POSTU: ", data )
    print("END OF REGISTER PART", data)
    if Postu.validate_post(data):
        Postu.send_post(data)
    else:
        print("invalid values")
        return redirect('/home')
    print("END OF POST")
    return redirect('/home')


@app.route("/post/edit/<id>", methods = ['GET'])
def displayEditWindow(id):
    if 'users_id' not in session:
        return redirect('/logout')
    currentUser = session
    usersPost = Postu.get_single_post(id)
    return render_template( "editpost.html", inSessionData = currentUser, singleUserPost = usersPost)
    
@app.route( "/update/post/<id>", methods = ['POST'] ) 
def updatePostu(id):
    if 'users_id' not in session:
        return redirect('/logout')

    posts_content = request.form['update_posts_content']
    user_id = request.form['user_id']
    post_id = request.form['post_id']

    data = (posts_content, user_id, post_id)
    
    if Postu.validate_post(data):
        Postu.update_post(data)
    else:
        print("invalid values")
        return redirect('/post/edit/<id>')
    print("END OF POST")
    return redirect('/home')


@app.route("/home/delete/<id>")
def deleteThisPost(id):
    if 'users_id' not in session:
        return redirect("/logout")
    Postu.delete_post(id)
    return redirect('/home')

