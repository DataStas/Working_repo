"""It is just a function that can take all the 
same parameters that a path operation function can take:"""
import uvicorn
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# CommonsDep = Annotated[dict, Depends(common_parameters)]

# @app.get("/items/")
# async def read_items(commons: Annotated[dict, CommonsDep]):
#     return commons


# @app.get("/users/")
# async def read_users(commons: Annotated[dict, CommonsDep]):
#     return commons

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
# CommonClassDep = Annotated[CommonQueryParams, Depends(CommonQueryParams)]
# @app.get("/items/")
# async def read_items(commons: CommonClassDep):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response


"""
Add dependencies to the path operation decorator

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
"""

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)