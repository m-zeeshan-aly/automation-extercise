from src.utils.generatedata.GenerateDataUtils import GenerateData


def print_formatted_data(full_name, first_name, last_name, email, phone,title,country,month,day,year,company,address,city,state,zip_code,checkboxes:list):
    print("\n" + "="*40)
    print("      GENERATED TEST DATA")
    print("="*40)
    print(f"Full Name   : {full_name}")
    print(f"First Name  : {first_name}")
    print(f"Last Name   : {last_name}")
    print(f"Email       : {email}")
    print(f"Phone       : {phone}")
    print(f"Title       : {title}")
    print(f"Country     : {country}")
    print(f"Day         : {day}")
    print(f"Month       : {month}")
    print(f"Year        : {year}")
    print(f"Company     : {company}")
    print(f"Address     : {address}")
    print(f"City        : {city}")
    print(f"State       : {state}")
    print(f"Zip Code    : {zip_code}")
    print(f"Checkboxes  : {checkboxes}")
    print("="*40 + "\n")



def signup_data():
    new_data = GenerateData()

    return {
        "full_name": new_data.fullName(),
        "first_name": new_data.firstName(),
        "last_name": new_data.lastName(),
        "email": new_data.email(),
        "phone": new_data.phone(),
        "title": new_data.title(),
        "country": new_data.country(),
        "day": new_data.day(),
        "month": new_data.month(),
        "year": new_data.year(),
        "company": new_data.company(),
        "address": new_data.address(),
        "city": new_data.city(),
        "state": new_data.state(),
        "zip_code": new_data.zip_code(),
        "checkboxes": new_data.checkboxes()
    }