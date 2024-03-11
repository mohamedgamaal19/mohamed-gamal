//author:mohamed gamal zainhom ali
//Id:20230326
//game: 1 Each player will take turns to enter a number between 1 and 10.\nThe first player to get more than 100 will be the winner of the game.
#include <iostream>

int main() {
    std::cout << "Each player will take turns to enter a number between 1 and 10.\nThe first player to get more than 100 will be the winner of the game.\n";

    int start = 0;

    while (start < 100) {
        int number;

        // Player one's turn
        while (true) {
            std::cout << "Please player one, enter a number from 1 to 10: ";
            std::cin >> number;

            if (number >= 1 && number <= 10) {
                break;
            }
            else {
                std::cout << "Invalid input! Please enter a number between 1 and 10.\n";
            }
        }

        start += number;
        std::cout << "The sum is: " << start << std::endl;

        if (start >= 100) {
            std::cout << "Congratulations player one, you are the winner :)\n";
            break;
        }

        // Player two's turn
        while (true) {
            std::cout << "Please player two, enter a number from 1 to 10: ";
            std::cin >> number;

            if (number >= 1 && number <= 10) {
                break;
            }
            else {
                std::cout << "Invalid input! Please enter a number between 1 and 10.\n";
            }
        }

        start += number;
        std::cout << "The sum is: " << start << std::endl;

        if (start >= 100) {
            std::cout << "Congratulations player two, you are the winner :)\n";
            break;
        }
    }

    return 0;
}
#include <iostream>

int main () {
    std::cout << "Each player will take turns to enter a number between 1 and 10.\nThe first player to get more than 100 will be the winner of the game.\n";

    int start = 0;

    while (start < 100) {
        int number;

        // Player one's turn
        while (true) {
            std::cout << "Please player one, enter a number from 1 to 10: ";
            std::cin >> number;

            if (number >= 1 && number <= 10) {
                break;
            }
            else {
                std::cout << "Invalid input! Please enter a number between 1 and 10.\n";
            }
        }

        start += number;
        std::cout << "The sum is: " << start << std::endl;

        if (start >= 100) {
            std::cout << "Congratulations player one, you are the winner :)\n";
            break;
        }

        // Player two's turn
    while (true) {
            std::cout << "Please player two, enter a number from 1 to 10: ";
            std::cin >> number;

            if (number >= 1 && number <= 10) {
                break;
            }
            else {
                std::cout << "Invalid input! Please enter a number between 1 and 10.\n";
            }
        }

        start += number;
    std::cout << "The sum is: " << start << std::endl;

         if (start >= 100) {
            std::cout << "Congratulations player two, you are the winner :)\n";
            break;
        }
    }

    return 0;
}
