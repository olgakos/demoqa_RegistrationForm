from models.pages.registration_page import RegistrationPage
from data.users import User

user = User('Olga', 'Kos',
            'kos@example.com',
            'Female',
            '0123456789',
            'April', '1995', '23',
            'Computer Science',
            'Reading',
            '/resources/foto_r.jpg',
            'Moscowskaya Street 16',
            'NCR', 'Delhi')


def test_registration_page():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.user_registration(user)
    registration_page.should_registered_user_with('Olga Kos',
                                                  'kos@example.com',
                                                  'Female',
                                                  '0123456789',
                                                  '23 April,1995',
                                                  'Computer Science',
                                                  'Reading',
                                                  'foto_r.jpg',
                                                  'Moscowskaya Street 16',
                                                  'NCR Delhi')