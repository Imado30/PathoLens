from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect



def signupView(request):

    information = {"availableUser": True, "equalPasswords": True, "passwordStrength": True, "entryComplete": True}

    # user is already loged in
    if request.user.is_authenticated:
        # TODO: rediretc to starting page
        print("user ist already logged in")
    
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        
        
        # stirp checks if one element is empyt or None
        webParameters = [firstName.strip(), lastName.strip(), email.strip(), password.strip(), confirmPassword.strip()]
        
        # one parameter is missing 
        if not all(webParameters):
            information["entryComplete"] = False
            print("in no all parm are filled")
            return termination(request, information)

        
        elif confirmPassword != password:
            information["equalPasswords"] = False
            return termination(request, information)
        
        
        # our username it the email but without the special characters
        username = email.replace("@", "AT")
        username = username.replace(".", "POINT")

        
        # check if a user exists with one of these variables
        usernameExists = User.objects.filter(username=username).exists()
        nameExists = User.objects.filter(first_name=firstName, last_name=lastName).exists()
        emailExists = User.objects.filter(email=email).exists()

        alreadyExistent = [
            usernameExists,
            nameExists,
            emailExists,
        ]

        if any(alreadyExistent):
            information["availableUser"] = False                
            return termination(request, information)


        # check if password is strong enough        
        try:
            validate_password(password)

        # reason why password is not strong enough
        except ValidationError as e:
            print(e.messages)

            information["passwordStrength"] = False
            return termination(request, information)

        # user creation
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=firstName,
            last_name=lastName,
            password=password,
        )
        
        # login of user 
        login(request, user)
        
        print("user was successfully signed up")

    else:
        print("Error: POST was not used")

    return render(request, "accounts/signup.html", {"information": information})



def termination(request, information):
    logout(request)
    return render(request, "accounts/signup.html", {"information": information})



def loginView(request):

    information = {"username": True,
                   "password": True,
                   }

    # user is already logged in
    if request.user.is_authenticated:
        # TODO: rediretc to starting page
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # remove '@' and '.' so that the usernmae is the email but without the special characters
        email = email.replace("@", "AT")
        email = email.replace(".", "POINT")

        userExistent = User.objects.filter(username=email).exists()

        
        # user is not existent 
        if (userExistent == False):
            information["username"] = False
            return render(request, "accounts/login.html", {"information" : information})
        
        
        user = authenticate(username=email, password=password)

        # login was successful
        if user is not None:
            login(request, user)
            return redirect("/")
        
        # password is incorrect
        else:
            information["password"] = False
    
    else:
        print("Error as POST was not used")
        
    return render(request, "accounts/login.html", {"information": information})