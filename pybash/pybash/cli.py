from pybash.executor import Executor
from pybash.custom_exceptions import UserExitException, ParsingFailureException


class CLI:
    def __init__(self):
        self._executor = Executor()

    def run(self) -> None:
        while True:
            user_input = input("$ ")

            try:
                self._executor.call(user_input)
            except UserExitException:
                break
            except ParsingFailureException:
                print("Syntax error")


if __name__ == "__main__":
    CLI().run()