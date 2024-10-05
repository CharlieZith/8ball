import uvicorn

def main() -> None:
    uvicorn.run("src.app:app", host="localhost", port=6969, reload=True)

if __name__ == "__main__":
    main()