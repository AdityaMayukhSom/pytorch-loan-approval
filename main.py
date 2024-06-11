import uvicorn
from backend import application

if __name__ == "__main__":
    uvicorn.run(application, port=8080)
