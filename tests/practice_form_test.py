from selene.support.shared import browser
from selene import command
from models.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()  # OPEN PAGE
    registration_page.add_block_to_page()  # AdBlockers

    # WHEN
    registration_page.type_first_name('Olga')
    registration_page.type_last_name('Kos')
    registration_page.type_email('kos@example.com')
    registration_page.choose_gender('Female')
    registration_page.type_number('0123456789')
    registration_page.type_date_of_birth('April', '1995', '23')  # Calendar
    registration_page.type_subjects('Computer Science')  # Subjects
    registration_page.choose_hobbies('Reading')  # Hobbies
    # registration_page.picture_path('/foto.jpg')  # Photo from tests folder
    registration_page.picture_path('/resources/foto_r.jpg')  # Photo from /resources
    registration_page.type_address('Moscowskaya Street 16')  # Current Address
    registration_page.choose_state_and_city('NCR', 'Delhi')  # State and City
    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Olga Kos',
        'kos@example.com',
        'Female',
        '0123456789',
        '23 April,1995',
        'Computer Science',
        'Reading',
        'foto_r.jpg',
        'Moscowskaya Street 16',
        'NCR Delhi',
    )

    browser.element('#closeLargeModal').click()