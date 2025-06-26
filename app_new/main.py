# ======================================================= #
### import ###
# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Router
from app_new.api.routes.v1 import Router

# ======================================================= #

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()

    # 미들웨어 정의
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 개발용
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Router
    app.include_router(Router.router, tags=["v1"])

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app_new", host="0.0.0.0", port=7999, reload=True)