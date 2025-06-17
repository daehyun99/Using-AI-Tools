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
    def __init__(self):
        self._id = None
        self._pw = None
        self._email = None
        self._service_enabled = None
    pass

# ======================================================= #

class GuestUser(User):
    """
    (추후 개발)
    비회원 또는 임시 사용자에 해당하는 사용자 클래스.

    로그인 없이 서비스를 체험하거나 제한된 기능만 사용하는 사용자에 대한 
    최소한의 정보와 권한을 정의한다. 일반적으로 영속성이 없고, 식별자는 임시로 부여된다.

    특징:
        - 서비스 이용 제한 있음
        - 읽기 전용 권한
    """
    pass

class StandardUser(User):
    """
    일반 사용자 계층을 나타내는 클래스.

    정상적인 가입 절차를 통해 생성된 사용자로, 번역 서비스 기능을 이용할 수 있으며,
    인증 정보와 함께 서비스 상태를 관리한다. 대다수의 사용자 유형에 해당한다.

    특징:
        - 이메일을 통한 ID, PW 발급 가능
        - ID, PW를 통해 인증 가능
        - 서비스 이용 상태 변경 가능
    """
    pass

class AdminUser(User):
    """
    (추후 개발)
    시스템 관리자 역할을 수행하는 사용자 클래스.

    사용자 계정, 데이터, 서비스 설정 등에 대한 접근 권한을 가지며,
    시스템 전반을 관리하거나 운영 도구에 접근할 수 있는 권한을 포함한다.

    특징:
        - 사용자 목록 조회 및 수정 권한
        - 운영 데이터 접근 권한
        - 권한 기반 접근 제어(RBAC) 상 상위 등급
    """
    pass

