
from Utilities.readProperties import ReadConfig
from pageObjects import LoginPage

from pageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from testCases.conftest import driver


class Test_001_Login:
    base_url = ReadConfig.getApplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_homepage(self, setup):
        self.logger.info("************* Test_001_Login ********* ")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            print("ftfjcnecbej")
            self.logger.info("title matched")
            self.driver.close()
        else:
            self.driver.save_screenshot("/Users/vamshi/PycharmProjects/nocommereceApp/Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("home page failed")
            assert False, "title not matched"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True, "title matches"
        else:
            assert False, "title not matched"
