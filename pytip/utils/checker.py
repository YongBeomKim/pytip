import os
import datetime


# Cache file Check 함수
def check_folder_file(file:str=None, folder:str=None):
    r"""파일과 폴더 존재여부 확인 (폴더가 없으면 해당 폴더를 생성)
    file (str) : 파일이름
    folder (str) : 폴더명
    :: return :: Boolean, file_path"""
    assert folder is not None, "확인할 folder 를 지정하지 않았습니다."
    str_folder = os.path.abspath(os.path.join(folder, ''))

    # Check Folder 
    if not os.path.exists(str_folder):
        os.makedirs(str_folder)

    # Check File (생성 날짜가 동일한지 확인)
    file_name = os.path.abspath(os.path.join(folder, file))
    if os.path.exists(file_name) == True:
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getatime(file_name)).date()
        if file_creation_date == datetime.datetime.today().date():
            return True, file_name
    
    return False, file_name

