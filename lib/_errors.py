class UserError(Exception):
    "Any Error User Caused"
    pass

class BaseError(BaseException):
    pass
    
class InteractError(BaseError):
    pass
class PayloadConfigError(UserError):
    "Raised When A Wrong variable is in zkit.yml for user payload"
    pass

class BackToMainMenu(BaseError):
    "Not An Exception But Having This Helps . crash_handler redirects user to Main Menu"
    pass


