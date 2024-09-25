import pytest
from tkinter import Tk
from Tic_Tac_Toe_Game import TicTacToe  # Assuming your game code is in a file called Tic_Tac_Toe_Game.py

@pytest.fixture
def tictactoe_app():
    """Create the Tic Tac Toe app for testing."""
    root = Tk()
    app = TicTacToe(root)
    return app

def test_initial_state(tictactoe_app):
    """Test the initial state of the game."""
    app = tictactoe_app
    # Check if all buttons are empty at the start
    for button in app.buttons:
        assert button['text'] == ' '
    
    # Check that the first player is X
    assert app.current_player == 'X'
    # Check the label displays Player 1's turn
    assert app.player_turn_label['text'].strip() == "Player 1 turn!"

def test_player_move(tictactoe_app):
    """Test player moves and switch between players."""
    app = tictactoe_app
    # Simulate Player 1 clicking on the first button
    app.button_click(0)
    assert app.buttons[0]['text'] == 'X'
    assert app.current_player == 'O'
    assert app.player_turn_label['text'].strip() == "Player 2 turn!"

    # Simulate Player 2 clicking on the second button
    app.button_click(1)
    assert app.buttons[1]['text'] == 'O'
    assert app.current_player == 'X'
    assert app.player_turn_label['text'].strip() == "Player 1 turn!"

def test_win_condition(tictactoe_app):
    """Test if the game detects the win condition correctly."""
    app = tictactoe_app
    # Simulate a winning move (Player X on row 1)
    app.button_click(0)  # X
    app.button_click(3)  # O
    app.button_click(1)  # X
    app.button_click(4)  # O
    app.button_click(2)  # X
    
    # Player X should be the winner
    assert app.check_winner() == True

def test_draw_condition(tictactoe_app):
    """Test the draw condition when no players win."""
    app = tictactoe_app
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]  # A set of moves leading to a draw
    players = ['X', 'O'] * 5

    for i, move in enumerate(moves):
        app.current_player = players[i % 2]
        app.button_click(move)

    # Ensure there is no winner and game ends in a draw
    assert app.check_winner() == False
    assert app.moves_count == 9
    assert all('disabled' in button.state() for button in app.buttons)  # Check if buttons are disabled
    
def test_restart_game(tictactoe_app):
    """Test if the game can be restarted correctly."""
    app = tictactoe_app

    # Make some moves
    app.button_click(0)  # Player X
    app.button_click(1)  # Player O

    # Restart the game
    app.restart_game()

    # Ensure all buttons are reset and player turn is reset
    for button in app.buttons:
        assert button['text'] == ' '  # Check if text is reset
        assert 'disabled' not in button.state()  # Check if buttons are enabled
    assert app.current_player == 'X'  # Ensure current player is reset
    assert app.moves_count == 0  # Ensure move count is reset


def test_all_win_conditions(tictactoe_app):
    """Test all possible win conditions for the game."""
    app = tictactoe_app

    winning_combinations = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal \
        (2, 4, 6),  # Diagonal /
    ]

    for combo in winning_combinations:
        app.restart_game()  # Reset the game for each test
        # Simulate Player X winning
        app.button_click(combo[0])  # Player X
        app.button_click(8)  # Player O (not blocking X)
        app.button_click(combo[1])  # Player X
        app.button_click(7)  # Player O (not blocking X)
        app.button_click(combo[2])  # Player X (Winning move)

    # Check if Player X wins after all combinations have been tested
    assert app.check_winner() == True