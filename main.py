import keychain
import os

class InstallIdPersistence:
    def __init__(self):
        self.keychain = keychain.Keychain()

    def get_install_id(self):
        return self.keychain.get_password('com.example.app', 'install_id')

    def set_install_id(self, install_id):
        self.keychain.set_password('com.example.app', 'install_id', install_id)

    def delete_install_id(self):
        self.keychain.delete_password('com.example.app', 'install_id')

def main():
    persistence = InstallIdPersistence()

    # Install ID mavjudligini tekshirish
    if persistence.get_install_id():
        print("Install ID mavjud")
    else:
        print("Install ID yo'q")

    # Install ID qo'shish
    install_id = "1234567890"
    persistence.set_install_id(install_id)
    print(f"Install ID qo'shildi: {install_id}")

    # Install ID o'chirish
    persistence.delete_install_id()
    print("Install ID o'chirildi")

if __name__ == "__main__":
    main()
