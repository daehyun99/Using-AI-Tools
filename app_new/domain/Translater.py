from abc import ABC, abstractmethod
from app_new.domain.DataObject import Document


class Translater(ABC):
    """
    파일 번역 기능을 위한 최상위 추상 클래스.

    다양한 번역 전략(PDF 수식 번역, 기타 라이브러리 기반 번역 등)을 유연하게 확장할 수 있도록
    설계된 기반 클래스이며, 실제 번역 로직은 하위 클래스에서 구현된다.

    이 클래스를 상속받는 모든 클래스는 `translate()` 메서드를 반드시 구현해야 한다.

    ## Methods:
        translate(document: Document) -> str:
            주어진 파일 경로에 해당하는 파일을 번역하여 번역본 파일 경로를 반환한다.
    """

    @abstractmethod
    def translate(self, document : Document) -> str:
        """
        주어진 파일 경로에 해당하는 파일을 번역하여 번역본 파일 경로를 반환한다.

        ## Parameters:
            document -> Document

        ## Return:
            file_path -> str

        ## Raise:
            Unknown Error(001)
            Unsupported Format(007)

        """
        pass        

    pass

# ======================================================= #

class PDFMathTranslate(Translater):
    """
    `PDFMathTranslate` 라이브러리를 이용해 PDF 파일을 번역하는 Translate 하위 클래스.

    이 클래스는 외부 라이브러리인 `PDFMathTranslate`를 래핑하여,
    PDF 내 텍스트를 번역하는 기능을 시스템 내부 Translate 인터페이스에 통합한다.

    내부적으로 라이브러리의 API를 호출하고, 결과를 후처리하여 반환한다.
    라이브러리의 업데이트에 따라 번역 품질이나 형식이 달라질 수 있다.

    ## 특징:
        - `PDFMathTranslate`의 기능을 추상화 계층에 연결
        - 시스템 내 일관된 번역 인터페이스 제공
        - 테스트 및 대체 구현이 용이한 구조로 유지

    ## Methods:
        translate(document : Document) -> str:
            주어진 파일 경로에 해당하는 파일을 번역하여 번역본 파일 경로를 반환한다.
    """
    pass
