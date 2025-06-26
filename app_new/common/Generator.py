# ======================================================= #
### import ###
from uuid import uuid4

# ======================================================= #

class Generator:
    def __init__(self):
        pass
    def generate_id():
        id = None
        while not id:
            id_candidate = f"{str(uuid4())[:8]}{str(uuid4())[:8]}"
            id_check = True # DB에서 id 중복여부를 확인하는 코드로 수정 필요
            if id_check:
                id = id_candidate
        return id

    def generate_pw():
        pw = None
        while not pw:
            pw_candidate = f"{str(uuid4())[:8]}{str(uuid4())[:8]}"
            pw_check = True # DB에서 pw 중복여부를 확인하는 코드로 수정 필요
            if pw_check:
                pw = pw_candidate
        return pw