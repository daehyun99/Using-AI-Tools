class UserRegisterService:
    """
    사용자 등록을 수행하는 애플리케이션 서비스.

    이 서비스는 도메인 객체인 `User`와 `Register`를 조합하여
    사용자 입력을 처리하고, 적절한 사용자 유형(Guest, Standard, Admin)에 따라
    시스템에 등록하는 로직을 담당한다.

    도메인 계층의 상태 변경은 이 계층에서 트리거되며, 트랜잭션/로깅/검증 등도
    이 계층에서 조정될 수 있다.

    Methods:
        register_user(user_input: dict) -> User:
            사용자 입력 데이터를 받아 등록 절차를 수행하고,
            등록된 User 객체를 반환한다.
    """
    pass