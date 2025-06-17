class Messaging:
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
    ...