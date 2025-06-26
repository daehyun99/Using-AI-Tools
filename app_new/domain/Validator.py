# ======================================================= #
### import ###
from abc import ABC, abstractmethod
import re

# Domain
from app_new.domain.User import User

# ======================================================= #

class Validator(ABC):
    """
    주어진 객체의 속성값을 검증하는 최상위 추상 클래스.

    하위 클래스로 UserValidator와 DataObjectValidator를 가진다.
    하위 클래스는 `validate` 메서드를 오버라이드하여 검증 로직을 구현한다.

    ## Methods:
        validate() -> bool:
            주어진 객체의 속성값이 유효한지 검증한다.
            검증 결과를 bool 형태로 반환한다.
    """
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, object: any) -> bool:
        """
        주어진 객체의 속성값이 유효한지 검증한다.
        검증 결과를 bool 형태로 반환한다.

        ## Parameters:
            object -> any

        ## Return:
             result -> bool

        ## Raise:
            Unknown Error(001)
            Invalid Data(003)
            Authentication Failed(005)
            Unsupported Format(007)
            Rate Limit Exceeded(008)
        """
        pass

# ======================================================= #

class UserValidator(Validator):
    """
    User 객체 검증에 책임을 가지는 클래스

    ## 특징:

    ## Methods:
        validate() -> bool:
            User 객체의 속성값이 유효한지 검증한다.
            검증 결과를 bool 형태로 반환한다.
    """
    def validate(self, object: str):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return True if re.match(pattern, object) else False

class DataObjectValidator(Validator):
    """
    DataObject 객체 검증에 책임을 가지는 클래스
    
    ## 특징:

    ## Methods:
        validate() -> bool:
            DataObject 객체의 속성값이 유효한지 검증한다.
            검증 결과를 bool 형태로 반환한다.
    
    """
    def validate(self, object):
        return super().validate(object)