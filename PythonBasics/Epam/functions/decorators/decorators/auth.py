class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False


def is_auth_dec(function): # перекрутить на проверку токена
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_auth_dec
def create_post(user: User):
    print(f'This is {user.name} is new')


new_user = User('Stas')
new_user.is_logged_in = True
create_post(new_user)
