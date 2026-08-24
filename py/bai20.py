class Nguoi:

    def getGender(self):
        pass


class Nam(Nguoi):

    def getGender(self):
        print("Nam")


class Nu(Nguoi):

    def getGender(self):
        print("Nữ")


nam = Nam()
nu = Nu()

nam.getGender()
nu.getGender()