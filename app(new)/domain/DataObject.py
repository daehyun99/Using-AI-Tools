class DatObject:
    """
    프로그램 내부 파일 관리의 최상위 객체.

    이 클래스는 모든 파일 객체의 공통 기반으로 사용되며, 
    파일의 메타데이터(경로, 생성 시각 등)를 관리하고 
    다양한 파일 유형에 공통적으로 필요한 인터페이스를 제공합니다.

    서브클래스로는 MediaFile (Video, Audio) 및 Document (Pdf) 등이 존재하며,
    이들을 통해 다형적 파일 관리가 가능하도록 설계되었습니다.

    Attributes:
        file_path (str): 파일의 경로.
        create_at (datetime): 파일의 생성 시간 정보.
    
    Method:
        get_file_type() -> bool:
            파일의 유형을 문자열로 반환합니다.

        get_file_path(new_path: str) -> str:
            파일의 경로를 반환합니다.

        create_file(path: str) -> None:
            새로운 파일을 생성합니다.

        update_file(path: str) -> None:
            기존의 파일을 수정합니다.
            
        delete_file(path: str) -> None:
            파일을 삭제합니다.
    """
    ...
