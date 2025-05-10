#include <iostream>
using namespace std;

char board[3][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
char currentPlayer = 'X';
bool gameRunning = true;

void drawBoard() {
    cout << " " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
    cout << "---|---|---" << endl;
    cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
    cout << "---|---|---" << endl;
    cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl;
}

bool makeMove(int choice) {
    int row = (choice - 1) / 3;
    int col = (choice - 1) % 3;
    if (choice < 1 || choice > 9 || board[row][col] == 'X' || board[row][col] == 'O') {
        return false;
    }
    board[row][col] = currentPlayer;
    return true;
}

bool checkWin() {
    // Rows
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return true;
    }
    // Columns
    for (int i = 0; i < 3; i++) {
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return true;
    }
    // Diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return true;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return true;
    return false;
}

bool checkDraw() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] != 'X' && board[i][j] != 'O') return false;
        }
    }
    return true;
}

void switchPlayer() {
    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
}

int main() {
    cout << "Tic-Tac-Toe: Player 1 (X), Player 2 (O)" << endl;
    cout << "Enter a number (1-9) to make a move." << endl;

    while (gameRunning) {
        drawBoard();
        cout << "Player " << currentPlayer << "'s turn. Enter a number: ";
        int choice;
        cin >> choice;

        if (!makeMove(choice)) {
            cout << "Invalid move! Try again." << endl;
            continue;
        }

        if (checkWin()) {
            drawBoard();
            cout << "Player " << currentPlayer << " wins!" << endl;
            gameRunning = false;
        } else if (checkDraw()) {
            drawBoard();
            cout << "It's a draw!" << endl;
            gameRunning = false;
        } else {
            switchPlayer();
        }
    }

    cout << "Game Over!" << endl;
    return 0;
}
