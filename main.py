import fastapi
import uvicorn
import fastapi_chameleon
import os

app = fastapi.FastAPI()
folder = os.path.dirname(__file__)
template_folder = os.path.join(folder, "templates")
template_folder = os.path.abspath(template_folder)

fastapi_chameleon.global_init(template_folder, auto_reload=True)


@app.get("/")
@fastapi_chameleon.template(template_file="index.html")
def index(user: str = "anon"):
    return {"user_name": user}


if __name__ == "__main__":
    uvicorn.run(app)
