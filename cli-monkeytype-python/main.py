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
        stdscr.nodelay(False)
        key = stdscr.getkey()

        # Check if the key is a single character before using ord()
        if isinstance(key, str) and len(key) == 1:
            if ord(key) == 27:  # ASCII value for ESC
                break


if __name__ == "__main__":
    wrapper(main)
