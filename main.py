import fastapi
import uvicorn
import fastapi_chameleon

from views import home

app = fastapi.FastAPI()
fastapi_chameleon.global_init("templates")


def main():
    configure()
    uvicorn.run(app)


def configure():
    fastapi_chameleon.template(template_file="index.html")
    app.include_router(home.router)


if __name__ == "__main__":
    main()
else:
    configure()
