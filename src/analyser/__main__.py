import uvicorn


def start() -> None:
    uvicorn.run("analyser.controller:app", reload=True)


if __name__ == "__main__":
    start()

