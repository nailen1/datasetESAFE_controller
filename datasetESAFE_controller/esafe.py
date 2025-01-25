from .file_name_utils import *
from .esafe_consts import ESAFE_RAW_DATASET_PREFIX
from .excel_utils import open_excel_as_df
from tqdm import tqdm
from shining_pebbles import scan_files_including_regex



class EsafeDatasetController:
    def __init__(self, file_name, account_code=ACCOUNT_CODE_TOTAL):
        self.file_name = file_name
        self.file_path = get_file_path(file_name)
        self.df = open_excel_as_df(self.file_path)
        self.date_ref = get_date_ref_from_df(self.df)
        self.date_save = get_date_save_from_file_name(self.file_name)
        self.file_name = get_file_name_format(self.file_name)

    
class EsafeDatasetScanner:
    def __init__(self, folder_path=BASE_PATH):
        self.folder_path = folder_path
        self.file_names_raw = scan_files_including_regex(self.folder_path, ESAFE_RAW_DATASET_PREFIX)
        self.file_names_canonical = [EsafeDatasetController(file_name).file_name for file_name in tqdm(self.file_names_raw)]

    def rename_all(self):
        for old, new in tqdm(zip(self.file_names_raw, self.file_names_canonical)):

            rename_file(old, new)
        return None
