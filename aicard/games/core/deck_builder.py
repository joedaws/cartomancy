from aicard.games.core.deck import Deck
from importlib import import_module
from aicard.games.core.card_builder import CardBuilder


class DeckBuilder:
    def __init__(self, game_module):
        self.card_builder = CardBuilder(game_module)
        self.game_info = import_module(game_module)
        self.card_generator = getattr(self.game_info, 'card_generator')

    def build_cards(self):
        """Build instances of cards based using the deck generator."""
        cards = [self.card_builder.build_card(fields)
                 for fields in self.card_generator()]
        return cards

    def build_deck(self):
        deck = Deck()
        deck.cards = self.build_cards()
        return deck
