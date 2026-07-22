import time
from src.load import load_data

def run_pipeline():
    while True:
        try:
            load_data()
            
            time.sleep(3600)
        except Exception as e:
            print('Loading failed with error:')
            print(f'{e}')


if __name__ == '__main__':
    run_pipeline()

