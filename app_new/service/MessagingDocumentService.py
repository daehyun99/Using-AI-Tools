# ======================================================= #
### import ###

# Domain
from app_new.domain.Messaging import Messaging
from app_new.domain.DataObject import Document

# ======================================================= #

class MessagingDocumentService:
    """
    번역본 파일을 외부로 전송하는 애플리케이션 서비스.

    이 클래스는 도메인 객체인 `Document`와 `Messaging`을 활용하여,
    사용자 정보를 이메일, 카카오톡 등의 메시징 채널로 전송하는 로직을 담당한다.

    애플리케이션 계층에서 유즈케이스 단위로 활용된다.

    ## Attributes:
    
    ## Methods:
        notify_document(document: Document, messaging: Messaging) -> None:
            주어진 메시징 채널을 통해 번역본 파일을 전송한다.

    """
    def __init__(self):
        pass

    def notify_document(self, document: Document, messaging: Messaging) -> None:
        """
        주어진 메시징 채널을 통해 번역본 파일을 전송한다.

        ## Parameters:
            document -> Document
            messaging -> Messaging

        ## Return:
            None

        ## Raise:
            Unknown Error(001)
            Invalid Data(003)
            Rate Limit Exceeded(008): 일일 전송한도 초과.
            Internal System Error(009)
        """
        pass