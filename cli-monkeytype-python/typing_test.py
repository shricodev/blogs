import curses
import random
import time


class TypingTest:
    """
    A class representing a type test application that measures words per minute (WPM) and accuracy.

    Attributes:
      stdscr (curses._CursesWindow): The curses window object for the application.
      to_type_text (str): The line of text for the user to type.
      user_typed_text (list): List of characters typed by the user.
      wpm (int): The calculated words per minute.
      start_time (float): The timestamp when the test began.
    """

    def __init__(self, stdscr):
        """Initialize the TypingTest instance with a curses window object."""
        self.stdscr = stdscr
        self.to_type_text = self.get_line_to_type()
        self.user_typed_text = []
        self.wpm = 0
        self.start_time = time.time()

    def get_line_to_type(self):
        """Select a random line of text from the 'typing_texts.txt' file to be typed by the user."""

        with open("typing_texts.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        return random.choice(lines).strip()

    def display_wpm(self):
        """Update the display with the current words per minute (WPM) score."""

        self.stdscr.addstr(1, 0, f"WPM: {self.wpm}", curses.color_pair(3))

    def display_accuracy(self):
        """Update the display with the current typing accuracy percentage."""
        self.stdscr.addstr(
            2,
            0,
            f"Accuracy: {self.test_accuracy()}%",
            curses.color_pair(3),
        )

    def display_typed_chars(self):
        """Highlight the typed characters according to their correctness to the original text."""
        for i, char in enumerate(self.user_typed_text):
            correct_character = self.to_type_text[i]
            color = 1 if char == correct_character else 2
            self.stdscr.addstr(0, i, char, curses.color_pair(color))

    def display_details(self):
        """Display the text to be typed along with the WPM and accuracy scores."""
        self.stdscr.addstr(self.to_type_text)
        self.display_wpm()
        self.display_accuracy()
        self.display_typed_chars()

    def test_accuracy(self):
        """Calculate and return the typing accuracy as a percentage."""
        total_characters = min(len(self.user_typed_text), len(self.to_type_text))

        if total_characters == 0:
            return 0.0

        matching_characters = 0

        for current_char, target_char in zip(self.user_typed_text, self.to_type_text):
            if current_char == target_char:
                matching_characters += 1

        matching_percentage = (matching_characters / total_characters) * 100
        return matching_percentage

    def test_wpm(self):
        """Run the typing test, calculating WPM and updating the display in real-time."""
        self.stdscr.nodelay(True)

        while True:
            time_elapsed = max(time.time() - self.start_time, 1)

            # Considering the average word length in English is 5 characters
            self.wpm = round((len(self.user_typed_text) / (time_elapsed / 60)) / 5)
            self.stdscr.clear()
            self.display_details()
            self.stdscr.refresh()

            if "".join(self.user_typed_text) == self.to_type_text or len(
                self.user_typed_text
            ) == len(self.to_type_text):
                self.stdscr.nodelay(False)
                break

            try:
                key = self.stdscr.getkey()
            except Exception:
                continue

            # Check if the key is a single character before using ord()
            if isinstance(key, str) and len(key) == 1:
                if ord(key) == 27:  # ASCII value for ESC
                    break

            # If the user has not typed anything reset to 0
            if not self.user_typed_text:
                self.start_time = time.time()

            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if len(self.user_typed_text) > 0:
                    self.user_typed_text.pop()

            elif len(self.user_typed_text) < len(self.to_type_text):
                self.user_typed_text.append(key)
