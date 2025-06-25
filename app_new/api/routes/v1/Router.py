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
from app_new.domain.User import StandardUser
from app_new.domain.Translater import PDFMathTranslater
from app_new.domain.Register import StandardRegister
from app_new.domain.Validator import DataObjectValidator, UserValidator



# Infrastructure

# ======================================================= #

router = APIRouter(prefix="/v1")

@router.post("/Message/Document/")
async def MessaggingDocument(file: UploadFile, backgroundtasks: BackgroundTasks):
    """
    사용자 입력을 검증합니다.
    논문을 번역합니다.
    번역된 논문을 전송합니다.
    (+) 로깅

    ## Parameters:
        file -> UploadFile
        backgroundtasks -> BackgroundTasks

    ## Return:

    """
    # Domain 객체 선언
    document = Document()
    messaging = Email()
    translater = PDFMathTranslater()
    validator = DataObjectValidator()

    # Service 객체 선언
    translatedocument = TranslateDocumentService()
    messagingdocument = MessagingDocumentService()
    
    # 라우터 로직
    document.create_file(file)

    messagingdocument.notify_document(document, messaging)    

    return ...

@router.post("/Message/User/")
async def MessaggingUser(backgroundtasks: BackgroundTasks):
    """
    사용자 입력을 검증합니다.
    사용자 정보를 등록합니다.
    발급한 사용자 정보를 전송합니다.

    ## Parameters:
        backgroundtasks -> BackgroundTasks

    ## Return:

    """
    # Domain 객체 선언
    user = StandardUser()
    messaging = Email()
    register = StandardRegister()
    validator = UserValidator()

    # Service 객체 선언
    userregister = UserRegisterService()
    messaginguser = MessagingUserService()

    # 라우터 로직
    validator.validate(user)
    

    userregister.register_user(user)    
    messaginguser.notify_user(user= user, messaging= messaging)

    return ...

# ======================================================= #