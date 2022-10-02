from fastapi import FastAPI

video_app = FastAPI()


@video_app.get("/home")
def homepage():
    return {"Hello": "welcome to video tutorials"}