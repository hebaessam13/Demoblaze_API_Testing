from utils import data_generator

SIGNUP_TEST_DATA = [('keirahahe', '123', 400, 'This user already exist.'),
                    ('', '123', 400, 'username is mandatory'),
                    ('keirahahe', '', 400, 'password is mandatory'),
                    ('15namestartwithnum', '123', 400, 'invalid username'),
                    ('randomusername', '1', 400, 'password length should be >1 '),
                    ('username with space', '12345', 400, 'username cant have spaces'),
                    (data_generator.generate_string(10), data_generator.generate_string(10), 200, '')]

LOGIN_TEST_DATA = [('keirahahe', '123', 200, ''),
                   ('keirahahe', 'xyz', 401, 'Wrong user name or password'),
                   ('keira', '123', 401, 'wrong username or password'),
                   ('thisauserthatdoesntexist', '12345', 401, 'wrong username or password'),
                   ('', '12345', 400, 'username cant be empty'),
                   ('thisauserthatdoesntexist', '', 400, 'password cant be empty')]

INVALID_API_METHODS = ['PUT', 'PATCH']
