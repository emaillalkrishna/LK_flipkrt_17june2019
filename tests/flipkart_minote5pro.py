from selenium import webdriver
import time
# # #  ----------------------------------- Launch browser------------------------------------

def launch_browser():
    global driver
    driver = webdriver.Chrome(
        executable_path="C:/Users/LAL KRISHNA/PycharmProjects/flipkrt_17june2019/drivers/chromedriver.exe")
    driver.get(url="https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(5)

# # #  ----------------------------------- Login page - Login to the flipkart --------------------------------------
def login_flipkart():
    driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys("7899091518")
    driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("Qspiderflipkart@123")
    driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
    time.sleep(5)


# # # ---------------------------------- Home page - Search for the product ----------------------------------------
def search_product():
    driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("mi note 5 pro")
    driver.find_element_by_xpath("//button[@class='vh79eN']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'Price -- Low to High')]").click()
    time.sleep(5)


    driver.find_element_by_xpath(
        "//body/div[@id='container']/div/div[@class='t-0M7P _2doH3V']/div[@class='_3e7xtJ']/div[@class='_1HmYoV hCUpcT']/div[@class='_1HmYoV _35HD7C']/div[2]/div[1]/div[1]/div[1]").click()

    my_current_window_id = driver.current_window_handle
    print(my_current_window_id)
    id_list_of_all_windows = driver.window_handles
    print(id_list_of_all_windows)
    driver.switch_to.window(id_list_of_all_windows[1])
    driver.refresh()
    # # # Click on any one
    driver.find_element_by_xpath("//button[@class='_2AkmmA _2Npkh4 _2MWPVK']").click()              # 1. Click on the "ADD TO CART button
    # driver.find_element_by_xpath("//button[@class='_2AkmmA _2Npkh4 _2kuvG8 _7UHT_c']").click()  # 2. Click on the "BUY NOW" button

    driver.find_element_by_xpath("//button[@class='_2AkmmA _14O7kc mrmU5i']").click()           # "ADD TO CART" --> continue shopping button
    # driver.find_element_by_xpath("//button[@class='_2AkmmA _14O7kc _7UHT_c']").click()      # "ADD TO CART" --> Place Order button


# # # ---------------------------------- Home page - Logout ----------------------------------------
launch_browser()
login_flipkart()
search_product()