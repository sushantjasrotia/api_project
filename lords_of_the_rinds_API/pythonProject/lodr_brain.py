class LodrBrain:
    def __init__(self, quote_list):
        self.quote_number = 0
        self.quote_list = quote_list
        self.current_quote = None

    def remaining_quote(self):
        return self.quote_number<len(self.quote_list)

    def next_quote(self):
        self.current_quote = self.quote_list[self.quote_number]
        self.quote_number += 1
        return f"Dialog.{self.quote_number}:{self.current_quote}"
        # lodr_quote = input(f"Dialog.{self.quote_number}:{self.current_quote}")
        # print(lodr_quote)
