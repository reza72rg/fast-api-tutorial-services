
from fastapi import FastAPI

names_db = [
    {
        "id": 1,
        "name": "ali"
    },
    {
        "id": 2,
        "name": "maryam"
    },
    {
        "id": 3,
        "name": "reza"
    },
]

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "hi reza"}

@app.get("/names")
def names_list():
    return names_db

@app.post("/names")
def create_name(name: str):
    context = {"details": name}
    id_new = names_db[-1]["id"]

    new_name =  {
        "id": id_new+1,
        "name" : name,
    }
    names_db.append(new_name)
    return context

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for name in names_db:
        if name["id"] == item_id:
            return name
    return {"item_id": item_id}