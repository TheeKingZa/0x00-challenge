#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid

class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    def __init__(self):
        """
        Initialize a new user:
        - assigned an unique uid=10223(u0_a223) gid=10223(u0_a223) groups=10223(u0_a223),3003(inet),9997(everybody),20223(u0_a223_cache),50223(all_a223)
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.__password = None  # Initialize the password attribute as None

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password  # Return the private password attribute

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        -  if /data/data/com.termux/files/home/alxAug/0x00-challenge is 
        -  if /data/data/com.termux/files/home/alxAug/0x00-challenge is not a string
        - Hash /data/data/com.termux/files/home/alxAug/0x00-challenge in MD5 before assigning to 
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None  # Set password to None if pwd is None or not a string
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()  # Hash and store the password as MD5

    def is_valid_password(self, pwd):
        """
        Valid password:
        -  if /data/data/com.termux/files/home/alxAug/0x00-challenge is 
        -  if /data/data/com.termux/files/home/alxAug/0x00-challenge is not a string
        -  if  is 
        - Compare  and the MD5 value of /data/data/com.termux/files/home/alxAug/0x00-challenge
        """
        if pwd is None or type(pwd) is not str:
            return False  # Return False if pwd is None or not a string
        if self.__password is None:
            return False  # Return False if the stored password is None
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password  # Compare MD5 hashes and return the result

if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")  # Check if a new user has an ID

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")  # Verify that user IDs are unique

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password != u_pwd:
        print("User.password should be hashed")  # Confirm that the password is correctly hashed

    if user_2.password is not None:
        print("User.password should be None by default")  # Ensure that password is None by default

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if set to None")  # Test setting the password to None

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if set to an integer")  # Test setting the password to an integer

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")  # Verify the is_valid_password method

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")  # Check is_valid_password with a wrong password

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compared with None")  # Check is_valid_password with None

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compared with an integer")  # Check is_valid_password with an integer

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")  # Check is_valid_password when no password is set
