class User:
    def __init__(self, name):
        self.name = name
        self.is_authenticated = False

def check_auth_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_authenticated: 
            function(args[0])
    return wrapper

@check_auth_decorator
def create_blog_post(user):
    print(f"This post is made by {user.name}")

new_user = User("Harshit")

new_user.is_authenticated = True
create_blog_post(new_user)