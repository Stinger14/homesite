from decimal import Decimal
import re
from reports import Reports
from wallets import Wallets


class Users():
    """ A Singleton dictionary of User objects """
    _users: dict[str, dict[str, str]] = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_user(cls, new_user: dict[str, str]) -> str:
        """Register a new user"""
        if new_user.get("user_id") not in cls._users:
            # using existing user_name as the id for simplicity
            user_id = new_user.get("user_name", "NA")
            cls._users[user_id] = new_user
            Reports.log_event(f"New user {user_id} registered")
            # create a wallet for the new user
            Wallets.create_wallet(user_id)
            # give user a sign up bonus
            Reports.log_event(f"User {user_id} received a sign up bonus of 10")
            Wallets.adjust_balance(user_id, Decimal(10))
            return user_id
        return ""
    
    @classmethod
    def edit_user(cls, user_id: str, updated_user: dict):
        """do nothing"""
        print(user_id)
        print(updated_user)
        return False

    @classmethod
    def change_pwd(cls, user_id: str, password: str):
        """do nothing"""
        print(user_id)
        print(password)
        return False

    