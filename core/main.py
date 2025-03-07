import random
from fastapi import FastAPI, status, HTTPException, Query, Form, Body, UploadFile, File, Path
from fastapi.responses import JSONResponse
from typing import Optional, List, Union
from dataclasses import dataclass
from schema import PersonRequestSchema, PersonResponseSchema, PersonUpdateSchema


app = FastAPI()

'''
@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Application startup")
    yield
    print("Application shutdown")'''


names_db = [
    {
        "id": 1,
        "name": "ali",
        "email": "test@gmail.com"
    },
    {
        "id": 2,
        "name": "maryam",
        "email": "test@gmail.com"
    },
    {
        "id": 3,
        "name": "reza",
        "email": "test@gmail.com"
    },
]


'''@dataclass
class Item:
    name: str
'''

@app.post("/items/", response_model=PersonResponseSchema)
async def create_item(item: PersonRequestSchema):
    new_name = {
        "id": random.randint(1, 1000),
        "name": item.name,
        "email": item.email,
    }
    names_db.append(new_name)
    return JSONResponse(content=new_name, status_code=status.HTTP_201_CREATED)


@app.get("/names", response_model=List[PersonResponseSchema])
def names_list(search: Optional[str] = Query(default= None, alias="The ID of the item to get",
                                             description="The id of the item to get",
                                             min_length=2,max_length=10 ,regex= '^[^0-9]*$' )):
    result = names_db
    if search:
        result = [name for name in names_db if search.lower() in name["name"].lower()]
    return JSONResponse(content=result,status_code=status.HTTP_200_OK)


@app.put("/names/{item_id}", response_model=PersonUpdateSchema)
def names_update(item_id: int = Path(), per: PersonRequestSchema= None):
    for n in names_db:
        if n["id"] == item_id:
            n["name"] = per.name
            return JSONResponse(content={"message": f"Name with ID {item_id} updated successfully"}, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")

@app.get("/list_names")
def get_list():
    result = names_db
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

'''
@app.post("/names")
def names_create(name: str = Body(embed=True, title="User Name", description="The name of the user", min_length=3, max_length=20)):
    new_name = {"id": random.randint(1,1000), "name": name}
    names_db.append(new_name)
    return JSONResponse(content=new_name, status_code=status.HTTP_201_CREATED)



@app.post("/upload/")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    return {"filename": file.filename,"content_type": file.content_type, "file_size": len(content)}

@app.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile]):
    return [
        {"filename": file.filename, "content_type": file.content_type}
        for file in files
    ]
    
@app.get("/names/{item_id}")
def names_detail(item_id: int):
    for name in names_db:
        if name["id"] == item_id:
            return JSONResponse(content=name, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")



@app.put("/names/{item_id}")
def names_update(item_id: int, name: str):
    for n in names_db:
        if n["id"] == item_id:
            n["name"] = name
            return JSONResponse(content={"message": f"Name with ID {item_id} updated successfully"}, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")

@app.delete("/names/{item_id}")
def names_delete(item_id: int):
    for i, n in enumerate(names_db):
        if n["id"] == item_id:
            del names_db[i]
            return JSONResponse(content={"message": f"Name with ID {item_id} deleted successfully"}, status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")
'''


'''
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


@app.delete("/items/{item_id}")
async def delete_names(item_id : int):
    for name in names_db:
        if name["id"] == item_id:
            names_db.remove(name)
            return JSONResponse(content={"details": "item is delete successfully"}, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")



@app.get("/names")
def names_list():
    return names_db



@app.get("/get_names")
def get_name(search : Optional[str] = None):
    result = names_db
    if search:
        result = [name for name in names_db if name["name"].lower() == search.lower() ]
        if len(result) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")
        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")


@app.get("/get_names")
def get_name(q : str | None = None):
    if q:
        return [name for name in names_db if name["name"] == q ]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}'''


