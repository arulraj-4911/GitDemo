from itertools import count

from playwright.sync_api import Page , expect

#def test_radio(page: Page):
        #page.goto("https://testautomationpractice.blogspot.com/")
       # day = page.get_by_role("checkbox",name="sunday")
       # day.click()
       # page.wait_for_timeout(4000)
#to check all the checkboxes
def test_list(page: Page):
        page.goto("https://testautomationpractice.blogspot.com/")
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        checkbox = []
        for day in days:
            checkbox.append(page.get_by_label(day))

        print(len(checkbox))
        for checkboxes in checkbox:
            checkboxes.check()
            expect(checkboxes).to_be_checked()



        #to uncheck the last 3 boxs
        for checkboxes in checkbox[-3:]:
            checkboxes.uncheck()
            expect(checkboxes).not_to_be_checked()

        #toggle the checkboxes
        for checkboxes in checkbox:
            if checkboxes.is_checked():
                checkboxes.uncheck()
                expect(checkboxes).not_to_be_checked()
            else:
                checkboxes.check()
                expect(checkboxes).to_be_checked()


        #randomly check check boxes
        indexes = [1,3,6]
        for index in indexes:
            checkbox[index].check()
            expect(checkbox[index]).to_be_checked()



        #by passing label to select checkboxes
        weekday = "Sunday"
        for day in days:
            if day == weekday:
                na = page.get_by_label(day)
                na.check()
                expect(na).to_be_checked()
                page.wait_for_timeout(4000)


