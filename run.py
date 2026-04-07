import importlib

if __name__ == "__main__":
    uvicorn = importlib.import_module("uvicorn")
    uvicorn.run("src.main:app", reload=True)
