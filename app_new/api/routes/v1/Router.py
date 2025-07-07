# ======================================================= #
### import ###
# FastAPI
from fastapi import APIRouter 
from fastapi import UploadFile, BackgroundTasks

# Service
from app_new.service.MessagingDocumentService import MessagingDocumentService
from app_new.service.MessagingUserService import MessagingUserService
from app_new.service.UserRegisterService import UserRegisterService
from app_new.service.TranslateDocumentService import TranslateDocumentService

# Domain
from app_new.domain.DataObject import Document
from app_new.domain.Messaging import Email
from app_new.domain.Translater import PDFMathTranslater
from app_new.domain.Validator import DataObjectValidator

# 의존성
from app_new.api.deps import MessaggingDocumentRequest, MessaggingUserRequest

# ======================================================= #

router = APIRouter(prefix="/v1")

@router.post("/Message/Document/")
async def MessaggingDocument(
    file: UploadFile,
    request: MessaggingDocumentRequest,
    backgroundtasks: BackgroundTasks):
    """
    `입력 검증`, `에러 처리`, `의존성 주입` <br>
    사용자 입력을 검증합니다. <br>
    논문을 번역합니다. <br>
    번역된 논문을 전송합니다. <br>
    (+) 로깅

    ## Parameters:
        file -> UploadFile
        backgroundtasks -> BackgroundTasks

    ## Return:

    ## Raise:

    """
    try:
        ### 객체 선언 ###
        # Domain 객체 선언
        document = Document()
        messaging = Email()
        translater = PDFMathTranslater()
        validator = DataObjectValidator()

        # Service 객체 선언
        translatedocument = TranslateDocumentService()
        messagingdocument = MessagingDocumentService()
        
        # 문서 생성 도메인 로직 실행
        document.create_file(file)

        ### 프리젠테이션 로직 ###
        # 문서 번역 서비스 로직 실행
        ...

        # 문서 전송 서비스 로직 실행
        messagingdocument.notify_document(document, messaging)    

        return ...
    except Exception as e:
        return ...

@router.post("/Message/User/")
async def MessaggingUser(
    request: MessaggingUserRequest,
    backgroundtasks: BackgroundTasks):
    """
    `입력 검증`, `에러 처리`, `의존성 주입` <br>
    사용자 입력을 검증합니다. <br>
    User 등록 서비스 로직을 실행합니다. <br>
    User 정보 전송 서비스 로직을 실행합니다. <br>
    발급한 사용자 정보를 전송합니다. <br>

    ## Parameters:
        email -> UserRegisterRequest
        backgroundtasks -> BackgroundTasks

    ## Return:

    ## Raise:

    """
    try:
        ### 객체 선언 ###
        # Domain 객체 선언
        messaging = Email()

        # Service 객체 선언
        userregister = UserRegisterService()
        messaginguser = MessagingUserService()

        ### 프리젠테이션 로직 ###
        # User 등록 서비스 로직 실행
        user = userregister.register_user(request.email)    

        # User 정보 전송 서비스 로직 실행
        messaginguser.notify_user(user= user, messaging= messaging)

        return ...
    except Exception as e:
        return ...

# ======================================================= #