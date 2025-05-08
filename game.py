import streamlit as st
import random

def check_winner(board):
    # Rows, columns, diagonals
    for row in board:
        if row.count(row[0]) == 3 and row[0] != '':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def computer_move(board):
    empty = get_empty_cells(board)
    if empty:
        return random.choice(empty)
    return None

def reset_game():
    st.session_state.board = [[''] * 3 for _ in range(3)]
    st.session_state.winner = None
    st.session_state.turns = 0
    st.session_state.game_over = False

# Initialize game state
if 'board' not in st.session_state:
    reset_game()

st.title("Tic Tac Toe: Player vs Computer")
st.write("You are ❌ (Player). The computer is ⭕.")

if st.button("Reset Game"):
    reset_game()

# Game logic
def play_turn(i, j):
    if st.session_state.board[i][j] == '' and not st.session_state.game_over:
        # Player move
        st.session_state.board[i][j] = 'X'
        st.session_state.turns += 1
        winner = check_winner(st.session_state.board)
        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
            return

        # Computer move
        if st.session_state.turns < 9:
            move = computer_move(st.session_state.board)
            if move:
                x, y = move
                st.session_state.board[x][y] = 'O'
                st.session_state.turns += 1
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True

# UI
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        label = st.session_state.board[i][j] or " "
        if cols[j].button(label, key=f"{i}-{j}") and not st.session_state.game_over:
            play_turn(i, j)

# Game status
if st.session_state.winner:
    if st.session_state.winner == 'X':
        st.success("🎉 You win!")
    else:
        st.error("💻 Computer wins!")
elif st.session_state.turns == 9:
    st.info("It's a tie!")
