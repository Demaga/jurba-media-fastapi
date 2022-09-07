from database.database import engine, get_db
from fastapi import FastAPI
from models.user import User
from sqladmin import Admin, ModelView

app = FastAPI()

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.is_active]


admin.add_view(UserAdmin)


@app.get("/")
async def root():
    return {"message": "Hello World"}
