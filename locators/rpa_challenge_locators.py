from botcity.web import By


class RpaChallengeLocators():
    """The RpaChallengeLocators class defines all locators from rpa challenge. Each locator has to be a tuple
    """
    b_input_forms = ("//a[text() = 'Input Forms']", By.XPATH)
    b_download_excel = ("//a[text() = ' Download Excel ']", By.XPATH)
    b_start = ("//button[text()='Start']", By.XPATH)
    i_first_name = ("//label[text()='First Name']/../input", By.XPATH)
    i_last_name = ("//label[text()='Last Name']/../input", By.XPATH)
    i_company_name = ("//label[text()='Company Name']/../input", By.XPATH)
    i_role_in_company = (
        "//label[text()='Role in Company']/../input", By.XPATH)
    i_address = ("//label[text()='Address']/../input", By.XPATH)
    i_email = ("//label[text()='Email']/../input", By.XPATH)
    i_phone_number = ("//label[text()='Phone Number']/../input", By.XPATH)
    b_sumbit = ("//input[@type='submit']", By.XPATH)
