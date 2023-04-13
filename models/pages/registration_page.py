import os

from selene import be, have
from selene.support.shared import browser
from selene import command

import tests
from tests import resources

class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
        return self

    def add_block_to_page(self):
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=2).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

        # var2:
        # browser.element('footer').execute_script('element.remove()')

        return self


    def type_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def type_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def type_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def choose_gender(self, value):
        browser.element('[for="gender-radio-2"]').should(have.text(value)).click()  # female
        # or
        # browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
        return self

    def type_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def type_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def type_subjects(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        # or
        # browser.element('#subjectsInput').type('Computer Science').press_enter()
        return self

    def choose_hobbies(self, value):
        browser.element('[for="hobbies-checkbox-2"]').should(have.text(value)).click()  # Reading
        # or
        # browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click() #best practice
        # or
        # browser.element('[for=hobbies-checkbox-2]').click() #Reading
        return self

    def picture_path(self, file_name):
        return str(
            browser.element('#uploadPicture').send_keys(os.getcwd() + file_name)  # only if the photo is in the same folder as the test
            # or
            # browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'resources/' + file_name))) # Photo from /resources
        )

    def type_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def choose_state_and_city(self, state, city):
        browser.execute_script("window.scrollBy(0, 500)")  # check scrolling
        browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()
        browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()

        '''
        or
        browser.element('#state').perform(command.js.scroll_into_view) #!
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Delhi')).click()
        '''
        return self

    def should_registered_user_with(self,
                                    full_name,
                                    email,
                                    gender,
                                    number,
                                    date_of_birth,
                                    subjects,
                                    hobbies,
                                    photo,
                                    address,
                                    state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(full_name,
                             email,
                             gender,
                             number,
                             date_of_birth,
                             subjects,
                             hobbies,
                             photo,
                             address,
                             state_and_city))
        return self
