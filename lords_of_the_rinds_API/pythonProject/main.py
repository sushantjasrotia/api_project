
from data import quote_in_dict
from lodr_brain import LodrBrain
from ui import LodrInterface

dialog_bank = []
for quote in quote_in_dict:
    dialog = quote["dialog"]
    dialog_bank.append(dialog)

DIALOG = LodrBrain(dialog_bank)
app = LodrInterface(DIALOG)

# while DIALOG.remaining_quote():
#     DIALOG.next_quote()
