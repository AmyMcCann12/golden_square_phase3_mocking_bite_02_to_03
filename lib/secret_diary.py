class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True
        pass

    def read(self):
        if self.locked:
            raise Exception("Go away!")
        else:
            return self.diary.read()
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False