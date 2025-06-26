# ======================================================= #
### import ###
# Domain
from app_new.domain.User import User, StandardUser

# Common
from app_new.common.Generator import Generator

# Infrastructure
from app_new.infrastructure.UserRepository import UserRepository

# ======================================================= #

class UserRegisterService:
    """
    사용자 등록을 수행하는 애플리케이션 서비스.

    이 서비스는 도메인 객체인 `User`와 `Register`를 조합하여
    사용자 입력을 처리하고, 적절한 사용자 유형(Guest, Standard, Admin)에 따라
    시스템에 등록하는 로직을 담당한다.

    도메인 계층의 상태 변경은 이 계층에서 트리거되며, 트랜잭션/로깅/검증 등도
    이 계층에서 조정될 수 있다.

    ## Attributes:

    ## Methods:
        register_user(user_input: dict) -> User:
            사용자 입력 데이터를 받아 등록 절차를 수행하고,
            등록된 User 객체를 반환한다.
    """
    def __init__(self):
        pass

    def register_user(self, email) -> User:
        """
        사용자 입력 데이터를 받아 등록 절차를 수행하고,
        등록된 User 객체를 반환한다.
        
        ## Parameters:
            user_input -> dict

        ## Return:
            user -> User

        ## Raise:
            Unknown Error(001)
            Invalid Data(003)

        """
        ### 객체 선언 ###
        # Domain 객체 선언
        user = StandardUser()

        # Common 객체 선언
        generator = Generator()

        # Infrastructure 객체 선언
        userrepository = UserRepository()

        ### 서비스 로직 ###
        # 중복 검증
        if userrepository.read_user():
            return ...

        # User 정보 생성
        user.update_id(generator.generate_id())
        user.update_pw(generator.generate_pw())
        user.update_email(email)
        user.update_service_enabled(True)

        # User 정보 저장(DB)
        userrepository.save_user(user)

        return user
