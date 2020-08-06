class UserError(Exception):
    "Any Error User Caused"

class BaseError(BaseException):
    " "
    
class PayloadConfigError(UserError):
    "Raised When A Wrong variable is in zkit.yml for user payload"
      

class BackToMainMenu(BaseError):
    "Not An Exception But Having This Helps . zkit_error_handler redirects user to Main Menu"

class IntegerError(BaseError):
    "Raised When ZKit Is Expecting An Integer But Gets Other Data Type (Usually String)"


