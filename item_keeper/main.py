from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    items = ["item1", "item2", "item3"]
    if item_id < len(items):
        return {"item": items[item_id]}
    return {"error": "Item not found"}
