from abc import ABC, abstractmethod

class Messaging(ABC):
    """
    메시지 전송 방식의 공통 인터페이스를 정의하는 최상위 추상 클래스.

    이 클래스는 Email, KakaoAPI 등 다양한 메시징 수단에 공통되는 속성과 
    인터페이스를 제공하며, 서브클래스에서 실제 전송 로직을 구현하도록 강제합니다.

    Attributes:
        channel (str): 메시지 전송 방식 (예: "email", "kakao").

    Methods:
        info() -> str:
            메시지 상태를 반환하는 추상 메서드입니다.

        send() -> None:
            메시지를 전송하는 추상 메서드입니다.
    """
    def __init__(self):
        self._channel = None
    
    def info(self) -> str:
        """
        메시지 상태를 반환하는 추상 메서드입니다.

        ## Paramters:

        ## Return:

        ## Raise:

        """
        return None
    
    def send(self) -> None:
        """
        메시지를 전송하는 추상 메서드입니다.
        
        ## Paramters:

        ## Return:
            None

        ## Raise:

        """
        return None

# ======================================================= #

class Email(Messaging):
    """
    이메일 기반 메시지 전송을 담당하는 Messaging의 하위 클래스.

    SMTP 등을 통해 이메일 메시지를 전송하며, `channel` 속성은 "email"로 설정됩니다.
    이 클래스는 메시지의 상태 확인(info) 및 실제 전송(send) 메서드를 구현합니다.

    ## Attributes:
        channel (str): 전송 채널. "email"로 고정.

    ## Methods:
        info() -> str:
            이메일 메시지 전송 상태를 반환합니다.

        send() -> None:
            이메일 메시지를 전송합니다.
    """
    pass


class KakaoAPI(Messaging):
    """
    (추후 개발)
    카카오톡 API를 활용한 메시지 전송을 담당하는 Messaging의 하위 클래스.

    Kakao Developers API 등을 사용해 사용자에게 메시지를 전달하며,
    `channel` 속성은 "kakao"로 설정됩니다.

    ## Attributes:
        channel (str): 전송 채널. "kakao"로 고정.

    ## Methods:
        info() -> str:
            카카오톡 메시지 전송 상태를 반환합니다.

        send() -> None:
            카카오톡 메시지를 전송합니다.
    """
    pass