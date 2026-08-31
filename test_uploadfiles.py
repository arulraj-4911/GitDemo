from playwright.sync_api import Page , expect
import pytest
import os
@pytest.mark.skip
def test_files_upload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #uploading single file
    page.locator("input[id='singleFileInput']").set_input_files(r"C:\Users\arul\PycharmProjects\PythonSelenium\report.html")
    page.wait_for_timeout(7000)
    page.locator("button:has-text('Upload Single File')").click()
    message=page.locator("#singleFileStatus")
    expect(message).to_contain_text("report.html")
    print("Uploaded Single File",message)
    page.wait_for_timeout(3000)
@pytest.mark.skip
def test_multi_files_upload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #uploading multiple file
    files =[r"C:\Users\arul\PycharmProjects\PythonSelenium\report.html",r"C:\Users\arul\PycharmProjects\PythonSelenium\report.xml"]
    page.locator("input[id='multipleFilesInput']").set_input_files(files)
    page.wait_for_timeout(7000)
    page.locator("button:has-text('Upload Multiple File')").click()
    message=page.locator("#multipleFilesStatus")
    expect(message).to_contain_text("report.html")
    expect(message).to_contain_text("report.xml")
    page.wait_for_timeout(3000)

def test_download(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("hello")
    page.locator("#generateTxt").click()
    page.on("download", lambda download: download.save_as("downloads/testfile.txt"))#to specify where to download
    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(5000)
    if os.path.exists("downloads/testfile.txt"):
        print("Download file exists")
    else:
        print("Download file not exists")





