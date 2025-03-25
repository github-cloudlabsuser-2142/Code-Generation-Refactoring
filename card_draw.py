from typing import List, Tuple
import itertools
import random

# Constants
RANKS = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King"
}
SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
CARDS_TO_DRAW = 5

def create_deck() -> List[Tuple[int, str]]:
    """Create a standard deck of 52 playing cards."""
    return list(itertools.product(range(1, 14), SUITS))

def shuffle_deck(deck: List[Tuple[int, str]]) -> None:
    """Shuffle the deck of cards in place."""
    random.shuffle(deck)

def format_card(card: Tuple[int, str]) -> str:
    """Format a card tuple into a readable string."""
    rank, suit = card
    rank_str = RANKS.get(rank, str(rank))
    return f"{rank_str} of {suit}"

def draw_cards(deck: List[Tuple[int, str]], count: int) -> List[Tuple[int, str]]:
    """Draw a specified number of cards from the deck."""
    if count > len(deck):
        raise ValueError(f"Cannot draw {count} cards from a deck of {len(deck)} cards")
    return deck[:count]

def main() -> None:
    """Main program execution."""
    try:
        # Create and shuffle the deck
        deck = create_deck()
        shuffle_deck(deck)

        # Draw and display cards
        print(f"\nDrawing {CARDS_TO_DRAW} cards:")
        drawn_cards = draw_cards(deck, CARDS_TO_DRAW)
        
        for i, card in enumerate(drawn_cards, 1):
            print(f"Card {i}: {format_card(card)}")

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
