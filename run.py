import uvicorn

from app.config.settings import settings


def main():
    uvicorn.run(
        "app.main:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
