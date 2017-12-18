from selenium import webdriver
import smtplib, datetime

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        cur_datetime = datetime.datetime.now().strftime("%m%d%Y-%H%M")
        testrprt = 'TestReport-' + str(cur_datetime) + '.txt'
        WriteReport = open(testrprt, "w")

        """
        element variables
        """
        elementById = driver.find_element_by_id("name")
        elementById1 = driver.find_element_by_id("multiple-select-example")
        # elementById2 = driver.find_element_by_id("multiple-select-example2")
        elementByName = driver.find_element_by_name("show-hide")
        elementByClassName = driver.find_elements_by_class_name("block large-show-spacer")
        elementBySubID = driver.find_element_by_id("bmwradio")

        if elementById is not None:
            id = "Test Passed: We found an element by Id"
            print(id)
        else:
            id = "Test Failed : No element for Id has found"
            print(id)

        if elementById1 is not None:
            id1 = "Test Passed: We found an element by Id1"
            print(id1)
        else:
            id1 = "Test Failed : No element for Id1 has found"
            print(id1)

        # if elementById2 is not None:
        #     print("Test Passed: We found an element by Id2")
        # else:
        #     print("Test Failed : No element for Id2 has found")

        if elementByName is not None:
            byname = "Test Passed: We found an element by Name"
            print(byname)
        else:
            byname = "Test Failed : No element for Name has found"
            print(byname)

        if elementByClassName is not None:
            print("Test Passed: We found an element by Class Name")
        else:
            print("Test Failed : No element for Class Name has found")

        # class FindBySubIdName(FindByIdName):

        # def test2(self):

        if elementBySubID is not None:
            print("Test Passed: We found an element 'bmwradio'")
        else:
            print("Test Failed : No bmwradio")

        #print(id + "\n" + id1 + "\n" + byname)

        ebody2 = (id + "\n" + id1 + "\n" + byname)



        esender = 'monstermon1972@gmail.com'
        ereceiver = 'ramongreyes@icloud.com','monstermon72@gmail.com'
        ebody = 'Subject : Ewan\n\nDear Pogi, \n\n' + ebody2 +'\n\n - MonPogi'
        epwd = 'Eskimo72'

        conn = smtplib.SMTP('smtp.gmail.com', 587)
        type(conn)
        #conn
        conn.ehlo()
        conn.starttls()
        conn.login(esender, epwd)
        conn.sendmail(esender, ereceiver, ebody)
        #{}
        conn.quit()

        driver.close()

        WriteReport.write(ebody2)
        WriteReport.close()

ff = FindByIdName()
ff.test()

# ff2 = FindBySubIdName
# ff2.test2()
