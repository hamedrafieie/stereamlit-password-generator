import random
import string
from abc import ABC, abstractmethod
from typing import Optional, List

import nltk
from nltk.corpus import words

nltk.download('words')


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate a password.
        """
        pass


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate a numeric PIN code.
    """
    def __init__(self, length: int = 8):
        """
        Initialize the PinCodeGenerator.

        Args:
            length (int): Length of the generated PIN code (default is 8).
        """
        self.length = length

    def generate(self) -> str:
        """
        Generate a numeric PIN code.

        Returns:
            str: Randomly generated PIN code.
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, include_capitalization: bool = False, include_numbers: bool = False, include_symbols: bool = False, length: int = 8):
        """
        Initialize the RandomPasswordGenerator.

        Args:
            include_capitalization (bool): Include uppercase letters.
            include_numbers (bool): Include digits (0-9).
            include_symbols (bool): Include special symbols.
            length (int): Length of the generated password (default is 8).
        """
        self.length: int = length
        self.include_numbers: bool = include_numbers
        self.include_symbols: bool = include_symbols
        self.include_capitalization: bool = include_capitalization
        self.source = string.ascii_lowercase
        if include_capitalization:
            self.source += string.ascii_letters
        if include_numbers:
            self.source += string.digits
        if include_symbols:
            self.source += string.punctuation

    def generate(self) -> str:
        """
        Generate a random password based on specified criteria.

        Returns:
            str: Randomly generated password.
        """
        return ''.join(random.choice(self.source) for _ in range(self.length))
        


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
        self,
        no_of_words: int = 5,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()  # edit this to any vocabulary list you want

        self.no_of_words: int = no_of_words
        self.separator: str = separator
        self.capitalization: bool = capitalization
        self.vocabulary: List[str] = vocabulary

    def generate(self) -> str:
        """
        Generate a password from a list of vocabulary words.
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.no_of_words)]
        if self.capitalization:
            password_words = [word.upper() for word in password_words]
        return self.separator.join(password_words)


# Example usage
if __name__ == "__main__":
    password_generator = MemorablePasswordGenerator(length=12)
    random_password = password_generator.generate()
    print(random_password)
