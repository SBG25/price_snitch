import yaml
from MailSender import MailSender
import importlib
import pkgutil


class PriceWarner():

    def __init__(self, config_file):
        self.config_file = config_file
        self.mail_sender = self.initialize_mail_sender()
        self.scrappers = self.initialize_scrappers()
        self.warning_list = []
        self.error_list = []

    def initialize_mail_sender(self):
        with open(self.config_file, 'r') as f:
            mail_config = yaml.safe_load(f)['mailsender']
            return MailSender(mail_config['sender'], mail_config['password'], mail_config['receiver'])

    def initialize_scrappers(self):
        scrappers_names_list = [name for _, name, _ in pkgutil.iter_modules(['scrappers'])]
        scrappers_list = dict()
        for scrapper in scrappers_names_list:
            module = importlib.import_module("scrappers." + scrapper)
            class_ = getattr(module, scrapper)
            instance = class_()
            scrappers_list[instance.url] = instance
        return scrappers_list

    def process_row(self, item):
        try:
            scrapper = self.get_scrapper(item.url)
            scrapper.url_to_item(item)

            if item.is_below_threshold():
                self.warning_list.append(item)
        except KeyError:
            self.error_list.append(item)
            print("Error in " + str(item))

    def process_warning_list(self):
        email_body = ""
        for item in self.warning_list:
            email_body += str(item) + "\n\n"

        if self.error_list:
            email_body += "\n\n------------------------\nERRORS\n------------------------\n"
            for item in self.error_list:
                email_body += str(item) + "\n\n"

        self.mail_sender.send_mail(email_body)

    def get_scrapper(self, url):
        try:
            main_url = url.split("/")[2]
            return self.scrappers[main_url]
        except KeyError:
            raise KeyError
