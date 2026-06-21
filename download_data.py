import os

os.environ['KAGGLE_USERNAME'] = 'felix1way'
os.environ['KAGGLE_KEY'] = 'KGAT_79f03df6879de65354d42ebff5ddb38d'

import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data_via_kaggle_token():
    api = KaggleApi()
    try:
        print("🔑 Đang gửi chuỗi định danh Token tới hệ thống Kaggle...")
        api.authenticate()
        print("✅ Xác thực quyền API thành công!")
    except Exception as e:
        print(f"❌ Lỗi xác thực hệ thống: {e}")
        return

    os.makedirs('data/raw', exist_ok=True)
    
    datasets = [
        "jeanpooljinezsorroza/data-for-forecast-the-fifa-worldcup-2026",
        "bibas69/world-cup-2026-prediction"
    ]
    
    for dataset in datasets:
        print(f"🔄 API đang kết nối và kéo gói dữ liệu: {dataset}...")
        api.dataset_download_files(dataset, path='data/raw', unzip=False)
        
    print("\n📦 Đang giải nén các tệp dữ liệu thô (.zip)...")
    for file in os.listdir('data/raw'):
        if file.endswith('.zip'):
            zip_path = os.path.join('data/raw', file)
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall('data/raw')
                os.remove(zip_path)
                print(f"✔️ Đã giải nén hoàn tất: {file}")
            except zipfile.BadZipFile:
                print(f"❌ Tệp tin {file} bị lỗi cấu trúc dữ liệu nén.")
                
    print("\n✨ XỬ LÝ HOÀN TẤT! Toàn bộ file dữ liệu thật đã nằm gọn trong thư mục 'data/raw/'.")

if __name__ == "__main__":
    download_data_via_kaggle_token()