from game.rockpaperscissor import rps_main


class Jesus:

    def __init__(self):

        self.x = None
        self.attempts = 0

    def functions(self, who_first):
        self.x = rps_main.some_instance.for_imports()

        if who_first is True:
            self.potato()
        elif who_first is False:
            self.banana()

        if self.x is True:
            self.potato()
        elif self.x is False:
            self.banana()

    def potato(self):
        print("Potato goes first.")
        self.attempts += 1
        rps_main.some_instance.for_imports()
        self.functions(None)

    def banana(self):
        print("Banana goes first.")
        self.attempts += 1
        rps_main.some_instance.for_imports()
        self.functions(None)


uwu = Jesus()
uwu.functions(None)