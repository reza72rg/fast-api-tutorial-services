from fastapi import FastAPI, status, HTTPException


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
    {
        "id": 4,
        "name": "ahmad"
    },
    {
        "id": 5,
        "name": "ali"
    },
    {
        "id": 6,
        "name": "reza"
    },
]

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "hi reza"}


@app.post("/names", status_code=status.HTTP_201_CREATED)
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

@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
async def update_names(item_id : int, new_name: str):
    for name in names_db:
        if name["id"] == item_id:
            name["name"] = new_name
            return {"details": new_name}
    else:
        return {"your id does not found"}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_names(item_id : int):
    for name in names_db:
        if name["id"] == item_id:
            names_db.remove(name)
            return {"details": "item is delete"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")



@app.get("/names")
def names_list():
    return names_db


'''@app.get("/get_names")
def get_name(q : str | None = None):
    if q:
        return [name for name in names_db if name["name"] == q ]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}'''


