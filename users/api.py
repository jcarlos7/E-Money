from ninja import Router
from users.models import User
from django.contrib.auth.hashers import make_password
from .schemas import UserSchema

users_router = Router()

@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    user.save()
    return {'ok': 'ok'}