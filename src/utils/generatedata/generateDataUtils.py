import random
import string
import uuid
from datetime import datetime
from src.utils.constants.constantsUtils import COUNTRIES, MONTHS, TITLES, CHECKBOXS, CONTACT_SUBJECTS, CONTACT_MESSAGES

class GenerateData:
    def __init__(self):
        self.first_name = self._generate_name(6)
        self.last_name = self._generate_name(6)

    def _generate_name(self, length):
        return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()

    def firstName(self):
        return self.first_name

    def lastName(self):
        return self.last_name

    def fullName(self):
        return f"{self.firstName()} {self.lastName()}"

    def email(self):
        return f"user_{uuid.uuid4().hex[:8]}@test.com"

    def phone(self):
        return "03" + ''.join(random.choices(string.digits, k=9))
    
    def card_number(self):
        return ''.join(random.choices(string.digits, k=13))
    
    def day(self):
        return str(random.randint(1, 31))
    
    def month(self):
        return random.choice(MONTHS)
    
    def year(self):
        current_year = datetime.now().year
        return str(random.randint(current_year - 100, current_year))
    
    def country(self):
        return random.choice(COUNTRIES)
    
    def title(self):
        return random.choice(TITLES)
    
    def zip_code(self):
        return ''.join(random.choices(string.digits, k=random.randint(5, 8)))
    
    def cvc_expiry(self):
        return ''.join(random.choices(string.digits, k=3))
   
    def checkboxes(self):
        return random.sample(CHECKBOXS, k=random.randint(0, len(CHECKBOXS)))
        
    def address(self):
        street = self._generate_name(8)
        landmark = self._generate_name(12)
        address = self._generate_name(15)
        return f"{street}, {landmark}, {address}"

    
    def city(self):
        name_len = random.randint(1,3)
        if name_len==1:
            c3 = ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
            return f"{c3}"
        elif name_len==2:
            c2 = ''.join(random.choices(string.ascii_letters, k=4)).capitalize()
            c3 = ''.join(random.choices(string.ascii_letters, k=6)).capitalize()
            return f"{c2} {c3}"
        else:
            c1 = ''.join(random.choices(string.ascii_letters, k=2)).capitalize()
            c2 = ''.join(random.choices(string.ascii_letters, k=5)).capitalize()
            c3 = ''.join(random.choices(string.ascii_letters, k=7)).capitalize()

            return f"{c1}, {c2}, {c3}"
        
    def state(self):
        name_len = random.randint(1,2)
        if name_len==1:
            c3 = ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
            return f"{c3}"
        else:
            c2 = ''.join(random.choices(string.ascii_letters, k=4)).capitalize()
            c3 = ''.join(random.choices(string.ascii_letters, k=6)).capitalize()
            return f"{c2} {c3}"
    
    def company(self):
        name_len = random.randint(1,2)
        if name_len==1:
            c3 = ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
            return f"{c3}"
        else:
            c2 = ''.join(random.choices(string.ascii_letters, k=4)).capitalize()
            c3 = ''.join(random.choices(string.ascii_letters, k=6)).capitalize()
            return f"{c2} {c3}"
        
    def get_payment_data(self):
        mm = self.month()
        cvc = self.cvc_expiry()
        year = self.year()
        card_number = self.card_number()
        name = self.fullName()

        return {
            "mm":mm,
            "cvc":cvc,
            "year":year,
            "card_number":card_number,
            "name": name
        }
    

        
    
