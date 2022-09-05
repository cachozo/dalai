from flask import render_template, request, session, redirect
from dalai_app import app
from dalai_app.models.User import User
from dalai_app.models.Postu import Postu
from dalai_app.models.Like import Like


@app.route('/home/post/like', methods = ['POST'])
def sendLikeDB():
    if 'users_id' not in session:
        return redirect('/logout')
    post_likes = request.form['likes_counts']
    user_id = request.form['users_id']
    post_id = request.form['posts_id']

    data = ( post_likes, user_id, post_id )

    print("FROM FORM 4 LIKE: ", data )
    print("END OF SENDLIKE PART", data)
    result = Like.add_likes(data)
    print("SON: ", result)
    return redirect('/home')

@app.route('/post/likes/<id>', methods = ['GET'])
def likePostViews(id):
    if 'users_id' not in session:
        return redirect('/logout')
    currentUser = session
    usersPost = Postu.get_single_post(id)
    userWhoLiked = Like.users_who_liked(id)
    print("SIGUE A", userWhoLiked)
    return render_template( "likesview.html", inSessionData = currentUser, singleUserPost = usersPost, userWhoLiked = userWhoLiked)
