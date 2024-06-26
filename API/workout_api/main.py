from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title="Workout Api")
app.include_router(api_router)

#if __name__ == '__main__':
    #import uvicorn

    #print("[-] link: http://127.0.0.1:8000")
    #uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)