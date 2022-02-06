import os

from src.app import app


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=os.getenv("PORT"),
        debug=True if os.getenv("STAGE") == "dev" else False,
    )
