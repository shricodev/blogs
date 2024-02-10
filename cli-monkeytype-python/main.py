import curses
from curses import wrapper

from typing_test import TypingTest


def main(stdscr):
    """
    Initialize the curses colors and run the TypingTest. Display the typing test interface
    and handle user input until the test is completed or the user exits by pressing ESC.

    Args:
        stdscr (curses._CursesWindow): The curses window object passed to the main function.

    Note:
        The function uses a loop to repeatedly call the TypingTest's test_wpm method until the
        user completes the test or exits via the ESC key. After completion, a congratulatory
        message is displayed, and the user is prompted to press any key to continue or exit.
    """
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr("Welcome to the speed type test")
    stdscr.addstr("\nPress any key to continue playing the game!")

    while True:
        typing_test = TypingTest(stdscr)
        stdscr.getkey()
        typing_test.test_wpm()
        stdscr.addstr(
            3,
            0,
            "Congratulations! You have completed the test! Press any key to continue...",
        )
        key = stdscr.getkey()

        # Check if the key is a single character before using ord()
        if isinstance(key, str) and len(key) == 1:
            if ord(key) == 27:  # ASCII value for ESC
                break


if __name__ == "__main__":
    wrapper(main)
