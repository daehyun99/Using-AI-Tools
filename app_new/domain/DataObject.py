from datetime import datetime
import os

class DataObject:
    """
    프로그램 내부 파일 관리의 최상위 객체.

    이 클래스는 모든 파일 객체의 공통 기반으로 사용되며, 
    파일의 메타데이터(경로, 생성 시각 등)를 관리하고 
    다양한 파일 유형에 공통적으로 필요한 인터페이스를 제공합니다.

    서브클래스로는 MediaFile (Video, Audio) 및 Document (Pdf) 등이 존재하며,
    이들을 통해 다형적 파일 관리가 가능하도록 설계되었습니다.

    ## Attributes:
        file_path (str): 파일의 경로.
        created_at (datetime): 파일의 생성 시간 정보.
    
    ## Method:
        get_file_type() -> str:
            파일의 유형을 문자열로 반환합니다.

        get_file_path() -> str:
            파일의 경로를 반환합니다.

        create_file() -> None:
            새로운 파일을 생성합니다.

        update_file() -> None:
            기존의 파일을 수정합니다.
            
        delete_file() -> None:
            파일을 삭제합니다.
    """
    def __init__(self):
        self._file_path = None
        self._created_at = None

    def get_file_type(self) -> str:
        """
        파일의 유형을 문자열로 반환합니다.
        예: 'mp4', 'mp3', 'pdf' 등

        ## Paramters:
            None

        ## Return:
            file_type -> str

        ## Raise:

        """
        return self._file_path.split('.')[-1].lower()
    
    def get_file_path(self) -> str:
        """
        파일의 경로를 반환합니다.

        ## Paramters:
            None

        ## Return:
            file_path -> str

        ## Raise:

        """
        return self._file_path
    
    def create_file(self) -> None:
        """
        새로운 파일을 생성합니다.

        ## Paramters:
            None

        ## Return:
            None

        ## Raise:
        
        """
        pass

    def update_file(self) -> None:
        """
        기존의 파일을 수정합니다.

        ## Paramters:
            None

        ## Return:
            None

        ## Raise:
        
        """
        pass

    def delete_file(self) -> None:
        """
        파일을 삭제합니다.

        ## Paramters:
            None

        ## Return:
            None

        ## Raise:
        
        """
        os.remove(f"{self._file_path}")
        return None

# ======================================================= #

class MediaFile(DataObject):
    """
    (추후 개발)
    멀티미디어 파일을 나타내는 추상 클래스.

    이 클래스는 오디오 및 비디오와 같은 미디어 유형 파일의 공통 속성과
    동작을 정의하며, 하위 클래스인 `Audio` 및 `Video`를 통해 구체화된다.

    ## 특징:
        - 스트리밍 또는 디코딩이 필요한 파일 유형
        - 파일 메타데이터(길이, 비트레이트 등)가 존재할 수 있음

    ## Attributes:
        file_path (str): 파일의 경로
        created_at (datetime): 파일 생성 시각
    """
    pass


class Document(DataObject):
    """
    문서 파일을 나타내는 추상 클래스.

    이 클래스는 텍스트 기반 또는 포맷 기반의 문서 파일에 대한 공통 기능을 정의하며,
    `PDF` 등의 하위 클래스를 통해 구체 포맷별로 확장된다.
    DataObject 클래스의 메서드를 상속 받는다.

    ## 특징:
        - 구조적 데이터 표현 가능 (텍스트, 수식, 표 등)
        - 주로 읽기/편집/변환 기능과 연계

    ## Attributes:
        file_path (str): 문서 파일의 경로
        created_at (datetime): 문서 객체 생성 시각
    """
    pass