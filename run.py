import uvicorn
from main import app




if __name__ == '__main__':
    uvicorn.run("__main__:app", reload=True)