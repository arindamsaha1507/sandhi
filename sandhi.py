"""Module for sandhi rules."""

from typing import Protocol

from akshara import varnakaarya as vk


class Sandhi(Protocol):
    """Interface for sandhi rules."""

    def sandhi(self, word1: str, word2: str) -> str:
        """Returns the word after sandhi."""


class StringOperations:
    """Class for string operations."""

    @staticmethod
    def get_last_letter(word: str) -> str:
        """Returns the last letter of the word."""
        return vk.get_vinyaasa(word)[-1]

    @staticmethod
    def get_first_letter(word: str) -> str:
        """Returns the first letter of the word."""
        return vk.get_vinyaasa(word)[0]

    @staticmethod
    def get_second_last_letter(word: str) -> str:
        """Returns the second last letter of the word."""
        return vk.get_vinyaasa(word)[-2]

    @staticmethod
    def get_second_letter(word: str) -> str:
        """Returns the second letter of the word."""
        return vk.get_vinyaasa(word)[1]

    @staticmethod
    def check_one_space(word: str) -> bool:
        """Returns True if there is only one space in the word."""
        return word.count(" ") == 1

    @staticmethod
    def split_at_space(word: str) -> list[str]:
        """Returns the word split at space."""

        if not StringOperations.check_one_space(word):
            raise ValueError("Word must have only one space.")

        return word.split(" ")


class VarnaSandhi:
    """Class for varna sandhi."""

    def __init__(self) -> None:
        """Initializes the class."""

        self.swara = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ऌ", "ए", "ऐ", "ओ", "औ"]

        self.rules = {}

        with open("rules_modified.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                self.rules[f"{line[0]} {line[1]}"] = {
                    "result": line[2],
                    "type": int(line[3]),
                }

    def sandhi(self, word1: str, word2: str) -> str:
        """Returns the word after sandhi."""

        last_letter = StringOperations.get_last_letter(word1)
        first_letter = StringOperations.get_first_letter(word2)

        if f"{last_letter} {first_letter}" in self.rules:
            result = self.rules[f"{last_letter} {first_letter}"]["result"]
            type_ = self.rules[f"{last_letter} {first_letter}"]["type"]

            if result == "ं":
                result = result + " "

            if type_ == 1:
                if StringOperations.get_second_letter(
                    word2
                ) in self.swara or StringOperations.get_second_letter(word2) in [
                    "ङ्",
                    "ञ्",
                    "ण्",
                    "न्",
                    "म्",
                    "य्",
                    "र्",
                    "ल्",
                    "व्",
                    "ह्",
                ]:
                    pass
                else:
                    result = vk.get_vinyaasa(word1)[-1]

            if type_ == 2:
                if StringOperations.get_second_last_letter(word1) in ["अ", "इ", "उ"]:
                    full_result = vk.get_shabda(
                        vk.get_vinyaasa(word1)
                        + vk.get_vinyaasa(result)
                        + vk.get_vinyaasa(word2)
                    )
                    return full_result

                else:
                    result = vk.get_vinyaasa(word1)[-1]

            if type_ == 3:
                full_result = vk.get_shabda(
                    vk.get_vinyaasa(word1)[:-1]
                    + vk.get_vinyaasa(result)
                    + vk.get_vinyaasa(word2)[1:]
                )
                return full_result

            if type_ in [0, 1, 2]:
                full_result = vk.get_shabda(
                    vk.get_vinyaasa(word1)[:-1]
                    + vk.get_vinyaasa(result)
                    + vk.get_vinyaasa(word2)
                )
                return full_result

        return f"{word1} {word2}"


class VisargaSandhi:
    """Class for visarga sandhi."""

    def __init__(self) -> None:
        self.karkasha = [
            "क्",
            "ख्",
            "च्",
            "छ्",
            "ट्",
            "ठ्",
            "त्",
            "थ्",
            "प्",
            "फ्",
            "श्",
            "ष्",
            "स्",
        ]

    def sandhi(self, word1: str, word2: str) -> str:
        """Returns the word after sandhi."""

        last_letter = StringOperations.get_second_last_letter(word1)
        first_letter = StringOperations.get_first_letter(word2)

        if first_letter in self.karkasha:
            if first_letter in ["क्", "ख्", "प्", "फ्"]:
                return f"{word1} {word2}"

            elif first_letter in ["च्", "छ्"]:
                full_result = vk.get_shabda(
                    vk.get_vinyaasa(word1)[:-1]
                    + vk.get_vinyaasa("श्")
                    + vk.get_vinyaasa(word2)
                )
                return full_result

            elif first_letter in ["ट्", "ठ्"]:
                full_result = vk.get_shabda(
                    vk.get_vinyaasa(word1)[:-1]
                    + vk.get_vinyaasa("ष्")
                    + vk.get_vinyaasa(word2)
                )
                return full_result

            elif first_letter in ["त्", "थ्"]:
                full_result = vk.get_shabda(
                    vk.get_vinyaasa(word1)[:-1]
                    + vk.get_vinyaasa("स्")
                    + vk.get_vinyaasa(word2)
                )
                return full_result

            else:
                return f"{word1} {word2}"

        elif last_letter not in ["अ", "आ"]:
            full_result = vk.get_shabda(
                vk.get_vinyaasa(word1)[:-1]
                + vk.get_vinyaasa("र्")
                + vk.get_vinyaasa(word2)
            )
            return full_result

        elif last_letter == "आ":
            full_result = vk.get_shabda(
                vk.get_vinyaasa(word1)[:-1]
                + vk.get_vinyaasa(" ")
                + vk.get_vinyaasa(word2)
            )
            return full_result

        if first_letter == "अ":
            full_result = vk.get_shabda(
                vk.get_vinyaasa(word1)[:-2]
                + vk.get_vinyaasa("ओऽ")
                + vk.get_vinyaasa(word2)[1:]
            )
            return full_result

        elif first_letter in [
            "आ",
            "इ",
            "ई",
            "उ",
            "ऊ",
            "ऋ",
            "ॠ",
            "ऌ",
            "ए",
            "ऐ",
            "ओ",
            "औ",
        ]:
            full_result = vk.get_shabda(
                vk.get_vinyaasa(word1)[:-1]
                + vk.get_vinyaasa(" ")
                + vk.get_vinyaasa(word2)
            )
            return full_result

        full_result = vk.get_shabda(
            vk.get_vinyaasa(word1)[:-2] + vk.get_vinyaasa("ओ ") + vk.get_vinyaasa(word2)
        )
        return full_result


if __name__ == "__main__":
    varna_sandhi = VarnaSandhi()
    print(varna_sandhi.sandhi("तस्मात्", "इन्द्र"))
    print(varna_sandhi.sandhi("रामम्", "गच्छ"))
    print(varna_sandhi.sandhi("बालान्", "तिष्ठति"))
    print(varna_sandhi.sandhi("बालान्", "त्रायते"))
    print(varna_sandhi.sandhi("सन्", "त्सरुः"))
