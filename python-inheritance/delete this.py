class Flacko:
    def check_integer(self, num):
        if not isinstance(num, int):
            raise ValueError("a must be an integer")
        else:
            pass


flacko_instance = Flacko()



try:
    flacko_instance.check_integer(5)
except ValueError as e:
    print("[ {} ] {}".format(e.__class__.__name__, e))

