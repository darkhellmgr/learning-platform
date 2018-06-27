from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyBTCNgjJpStBaazWCTkn9WmOzRD1jHkTEY",
    'authDomain': "learning-management-7b9f2.firebaseapp.com",
    'databaseURL': "https://learning-management-7b9f2.firebaseio.com",
    'projectId': "learning-management-7b9f2",
    'storageBucket': "learning-management-7b9f2.appspot.com",
    'messagingSenderId': "482234388569"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()


def sign(request):
    return render(request, "accounts/signin.html")


def postsign(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"
        return render(request, "accounts/signin.html", {"messg": message})

    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "accounts/welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, "accounts/signin.html")


def signup(request):
    return render(request, "accounts/signup.html")


def postsignup(request):
    name = request.POST.get('name')
    category = request.POST.get('category')
    email = request.POST.get("email")
    passw = request.POST.get("pass")

    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "Unable to create account. Try again"
        return render(request, "accounts/signup.html", {"messg": message})

    uid = user['localId']
    data = {"name": name, "category": category, "status": "1"}
    database.child("users").child(uid).child("details").set(data)

    return render(request, "accounts/signin.html")
