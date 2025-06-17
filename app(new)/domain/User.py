class User:
    """
    사용자 정보를 관리하는 도메인 계층의 최상위 객체.

    이 클래스는 메모리 상의 사용자 상태를 로드하고 변경하는 데 사용되며,
    사용자 식별 정보, 인증 정보, 이메일, 서비스 사용 여부 등의 속성을 갖는다.
    실제 사용자는 GuestUser, StandardUser, AdminUser로 세분화되어 확장된다.

    Attributes:
        id (str): 사용자 ID.
        pw (str): 비밀번호.
        email (str): 사용자 이메일 주소.
        service_enabled (bool): 서비스 이용 가능 여부 상태.

    Methods:
        is_service_enabled() -> bool:
            현재 서비스 이용 가능 여부를 반환한다.

        update_email(new_email: str) -> None:
            사용자의 이메일 주소를 변경한다.

        update_pw(new_pw: str) -> None:
            사용자 비밀번호를 변경한다.

        update_service_enabled(new_service_state: bool) -> None:
            서비스 활성화 상태를 변경한다.
    """
    ...