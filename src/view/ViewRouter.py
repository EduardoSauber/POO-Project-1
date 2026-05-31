from src.controller.appController import AppManager
from view.authView import AuthView
from view.userView import UserView
from view.adminView import AdminView
from view.storeView import StoreView

class ViewRouter:
    def __init__(self,file_path):
        self._app = AppManager(file_path)

        self.running = True

        self._auth_view = AuthView(self._app)
        self._store_view = StoreView(self._app)

        self._user_view = UserView(self._app,self._store_view)
        self._admin_view = AdminView(self._app)

    def start(self):
        while self.running:
            if not self._app.personal_session_id:
                case = self._auth_view.main_menu()
                if case == "STOP":
                    self.stop()
            else:
                admin = self._app.is_user_admin
                view = self._user_view if not admin else self._admin_view
                case = view.main_menu()
                if case == "STOP":
                    self.stop()
                elif case == "LOGOUT":
                    self._app.logout()

    def stop(self):
        print("Saindo do sistema...")
        self.running = False

# testbench
def testbench():
    print("Rodando modo teste:")
    app = ViewRouter("../controller/data")
    app.start()
if __name__ == '__main__':
    testbench()