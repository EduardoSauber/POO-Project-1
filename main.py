from src.controller.appController import AppManager

def main():
    file_path = "./src/controller/data"
    app = AppManager(file_path=file_path)

    app.start()

if __name__ == '__main__':
    main()