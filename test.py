# import time
# from selenium.webdriver.chrome.options import Options
# from seleniumwire import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import gzip
# import io
#
# def decompress_gzip(data):
#     with gzip.GzipFile(fileobj=io.BytesIO(data)) as f:
#         return f.read()
#
# # Khởi tạo ChromeDriver
# #service = Service(executable_path= r"D:\ChromeDriver\chromedriver-win64\chromedriver.exe")
#
# # Set up Chrome options
# chrome_options = Options()
# chrome_options.debugger_address = "localhost:9222"
# driver = webdriver.Chrome()
#
# # Mở một trang web
# driver.get("https://crm.mindx.edu.vn/leads")
# time.sleep(10)
# # Tìm kiếm một phần tử bằng ID
# username_field = driver.find_element(By.XPATH, '//*[@id="usernameOrEmail"]')
# username_field.send_keys('ducnt@mindx.edu.vn')
#
# password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
# password_field.send_keys('MindX@6969')
#
# button_login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/form/div/div/div[3]/button/span[1]')
# button_login.click()
# #driver.get("https://crm.mindx.edu.vn/leads")
#
# '''
# list_sales_person = [
#     'Tấn Hùng CSL 18+': 'jsZdJWsAVjQ3D1GzPb2lQP3OuWM2',
#     'STL Nguyen Thi Thuong': '8eUWoFJwzfeEzuIMRlDahAsWhnB2',
#     'Sale Vu Thi Uyen': 'xLb05PzmT9N1fEwgcdoxfaUAyJ22',
#     'Sale Trang': 'KtlAEKx9lANyo17C0Nrd8fOUOD53',
#     'Sale Tran Thi Kim Anh',
#     'STL Nguyen Thao My',
#     'Sale Van Thanh Minh Thu',
#     'Sale Phung Thi Hong Nhung',
#     'Sale Pham Thi Ngoc Nhi',
#     'Sale Nguyen Diem Quynh',
#     'Sale Huynh Thi Thuy Trang',
#     'Sale Cao Thu Thao',
#     'Lê Tấn Đạt',
#     'CS 18+ Châu Pha',
#     'STL Lai Trung Khuong',
#     'Sale Truong Nguyen Khoi Nguyen',
#     'Sale Truong Huyen Trinh',
#     'Sale Nguyen Thi Nhu Thuy',
#     'Nguyễn Thị Quỳnh Trang CXO',
#     'Sales Truong Thanh Tung',
#     'Sale Tran Thi Kim Anh',
#     'Bui Thuy An',
#     'STL LVV 18+ Le Thi Ngoc Mai',
#     'Sale Le Thi Kim Xuyen',
#     'Sale Cao Thi My Huong',
#     'STL Nguyen Thi Doi',
#     'Sale Trang',
#     'Sale Pham Thao Van',
#     'Sale Khuat Duy Trung'
# ] '''
#
# #search_sales = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/section/section/main/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[6]/div/div/div/div[1]')
# #search_sales.send_keys()
#
# time.sleep(15)
# # Refresh the current page
# driver.refresh()
#
# # Optional: wait for some time to let the page reload and requests be made again
# time.sleep(30)
#
# # Capture and print the responses of the specific endpoint
# for request in driver.requests:
#     #print(f"URL: {request.url}")
#     if request.response and "https://crm.mindx.edu.vn/api/leads:fetch" in request.url:
#         print(f"URL: {request.url}")
#         print(f"Response status: {request.response.status_code}")
#         response_body = decompress_gzip(request.response.body)
#         print(f"Response body: {response_body.decode('utf-8')}")
# # Đóng trình duyệt
# driver.quit()


from math import comb

MOD = 1000000007


def main():
    n = int(input())
    mp = {}
    for _ in range(n):
        x = int(input())
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1

    ans = 0
    for key, value in mp.items():
        if value != 1:
            ans = (ans + comb(value, 2)) % MOD

    print(ans)


if __name__ == "__main__":
    main()
