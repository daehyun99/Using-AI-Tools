from app_new.domain.Messaging import Messaging
from app_new.domain.User import User

class MessagingUserService:
    """
    사용자 정보를 외부로 전송하는 애플리케이션 서비스.

    이 클래스는 도메인 객체인 `User`와 `Messaging`을 활용하여,
    사용자 정보를 이메일, 카카오톡 등의 메시징 채널로 전송하는 로직을 담당한다.

    애플리케이션 계층에서 유즈케이스 단위로 활용된다.

    ## Attributes:
    
    ## Methods:
        notify_user(user: User, messaging: Messaging) -> None:
            주어진 메시징 채널을 통해 사용자 정보를 전송한다.
    """
    def __init__(self):
        pass

    def notify_user(self, user: User, messaging: Messaging) -> None:
        """
        주어진 메시징 채널을 통해 사용자 정보를 전송한다.

        ## Parameters:
            user -> User
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