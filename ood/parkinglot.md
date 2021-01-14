
First we implement people in the system, which are admin, consumer and attendant.

```python
from enum import ENUM
class AccountsStatus(ENUM):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1,2,3,4,5,6

class Account(object):
    def __init__(self, user_name, password, person, status=AccountsStatus.Active):
        self.__user_name = user_name,
        self.__password = password,
        self.__perso = person,
        self.__status = status
        
   def reset_password(self):
    	None
        
class Admin(Account):

```



