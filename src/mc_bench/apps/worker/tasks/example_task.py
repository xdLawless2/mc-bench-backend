from ..app import app


@app.task(name="example_task")
def example_task():
    return {"ok": True}
