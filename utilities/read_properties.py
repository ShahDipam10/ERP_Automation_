import configparser

# Initialize ConfigParser to read configuration file
config = configparser.RawConfigParser()
config.read('./configurations/config.ini')  # Load the config file

class ReadConfig:
    """Class to read configuration values from config.ini file"""

    @staticmethod
    def get_google_url():
        return config.get('common info', 'google_URL')

    @staticmethod
    def get_google_email():
        return config.get('common info', 'google_email')

    @staticmethod
    def get_google_pass():
        return config.get('common info', 'google_password')

    @staticmethod
    def get_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_user_email():
        return config.get('common info', 'user_email')

    @staticmethod
    def get_email_prefix():
        return config.get('common info', 'email_prefix')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')

    @staticmethod
    def get_search_text():
        return config.get('common info', 'search_keyword')

    @staticmethod
    def get_firstname():
        return config.get('common info', 'first_name')

    @staticmethod
    def get_lastname():
        return config.get('common info', 'last_name')

    @staticmethod
    def get_wrong_email():
        return config.get('common info', 'user_wrong_email')

    @staticmethod
    def get_wrong_password():
        return config.get('common info', 'user_wrong_password')

    @staticmethod
    def get_company_name():
        return config.get('common info', 'company_name')

    @staticmethod
    def get_company_city():
        return config.get('common info', 'company_city')

    @staticmethod
    def get_company_phone_no():
        return config.get('common info', 'company_phone_no')
