
from fastapi import FastAPI
from httpx import delete

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
    new_name =  {
        "id": names_db[-1]["id"]+1,
        "name" : name,
    }
    names_db.append(new_name)

    return {"details" : new_name}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for name in names_db:
        if name["id"] == item_id:
            return name
    return {"item_id": item_id}

@app.put("/items/{item_id}")
async def update_names(item_id : int, new_name: str):
    for name in names_db:
        if name["id"] == item_id:
            name["name"] = new_name
            return {"details": new_name}
    else:
        return {"your id does not found"}


@app.delete("/items/{item_id}")
async def delete_names(item_id : int):
    for name in names_db:
        if name["id"] == item_id:
            names_db.remove(name)
            return {"details": "item is delete"}
    else:
        return {"your id does not found"}