import time
from decimal import Decimal
from wallets import Wallets
from reports import Reports


class GameEngine():
    _instance = None
    _start_time: int = 0
    _clock: int = 0
    _entries: list[tuple[str, Decimal]] = []
    _game_open = True

    def _new__(cls):
        if cls._instance is None:
            cls._instance = GameEngine()
            cls._start_time = int(time.time())
            cls._clock = 60
        return cls._instance

    @classmethod
    def get_game_state(cls) -> dict:
        """Get a snapshot of the current game state"""
        now = int(time.time())
        time_remaining = cls._start_time - now + cls._clock
        if time_remaining < 0:
            cls._game_open = False
        return {
            "clock": time_remaining,
            "game_open": cls._game_open,
            "entries": cls._entries
        }

    @classmethod
    def submit_entry(cls, user_id: str, entry: Decimal) -> bool:
        """Submit a new entry to the user in the game"""
        now = int(time.time())
        time_remaining = cls._start_time - now + cls._clock
        if time_remaining < 0:
            if Wallets.get_balance(user_id) > Decimal('1'):
                if Wallets.adjust_balance(user_id, Decimal('-1')):
                    cls._entries.append((user_id, entry))
                    Reports.log_event(f"New entry submitted by {user_id} for {entry}")
                    return True
                Reports.log_event(f"Insufficient funds for {user_id} to submit entry")
                return False
            Reports.log_event(f"Insufficient funds for {user_id} to submit entry")
            return False
        Reports.log_event(f"Game closed")
        return False

    

    