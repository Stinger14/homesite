from decimal import Decimal
from reports import Reports


class Wallets():
    """A Singleton Dictionary of User Wallets"""
    _wallets: dict[str, Decimal] = {}

    def __new__(cls):
        return cls

    @classmethod
    def create_wallet(cls, user_id: str) -> bool:
        """A method to create a new wallet for a user"""
        if user_id not in cls._wallets:
            cls._wallets[user_id] = Decimal(0)
            Reports.log_event(f"Wallet created for user {user_id} with 0 balance")
            return True
        return False

    @classmethod
    def get_balance(cls, user_id: str) -> Decimal:
        """A method to retrieve the balance of a user's wallet"""
        Reports.log_event(f"Balance check for user {user_id} = {cls._wallets.get(user_id, Decimal(0))}")
        return cls._wallets.get(user_id, Decimal(0))

    @classmethod
    def adjust_balance(cls, user_id: str, amount: Decimal) -> Decimal:
        cls._wallets[user_id] += Decimal(amount)
        Reports.log_event(f"Balance adjusted for user {user_id} by {amount}."
                        f" New balance = {cls._wallets[user_id]}")
        return cls._wallets[user_id]
