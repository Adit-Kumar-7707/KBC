# KBC (Kaun Banega Crorepati) Python Project

This Python project simulates a basic version of the popular TV quiz show "Kaun Banega Crorepati" (KBC). The script presents a series of questions to the user, who must choose the correct answer from four options. The project includes features such as leveling up based on correct answers and handling prize money.

## Features

- **Quiz Questions:** A series of predefined questions with four options each.
- **Answer Validation:** Checks if the user's answer is correct and updates the level and prize money accordingly.
- **Prize Money:** Displays the prize money based on the level achieved.
- **Quit Option:** Allows the user to quit the game at any point.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/kbc-python-project.git
    cd kbc-python-project
    ```

2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the script:
    ```sh
    python kbc.py
    ```

2. The program will display questions one by one.
3. Enter the number corresponding to your answer (1, 2, 3, or 4) or type "9" to quit.
4. The program will validate your answer, update your level, and display your prize money.

## Questions and Answers

The following is a list of questions included in the project:

1. What is the color of orange?
    - 1) Orange
    - 2) Red
    - 3) Yellow
    - 4) Green

2. What is the color of Red Rose?
    - 1) Orange
    - 2) Red
    - 3) Yellow
    - 4) Green

3. What is the color of Lemon?
    - 1) Orange
    - 2) Red
    - 3) Yellow
    - 4) Green

4. What is the color of Grapes?
    - 1) Orange
    - 2) Red
    - 3) Yellow
    - 4) Green

5. Who is the Iron Man?
    - 1) Tony Stark
    - 2) Loki
    - 3) Thor
    - 4) Shield

6. Who can Teleport?
    - 1) Tony Stark
    - 2) Loki
    - 3) Thor
    - 4) Shield

7. Who has Mijoneer?
    - 1) Tony Stark
    - 2) Loki
    - 3) Thor
    - 4) Shield

8. What Captian Amearica has?
    - 1) Tony Stark
    - 2) Loki
    - 3) Thor
    - 4) Shield

## Prize Levels

The prize money awarded at each level is as follows:

- Level 0: "Bhaag yaha se"
- Level 1: ₹10,000
- Level 2: ₹25,000
- Level 3: ₹50,000
- Level 4: ₹1,00,000
- Level 5: ₹5,00,000
- Level 6: ₹50,00,000
- Level 7: ₹1,00,00,000
- Level 8: ₹7,00,00,000

## How It Works

1. The script iterates through a list of questions.
2. The user is prompted to input their answer or choose to quit.
3. If the answer is correct, the user moves to the next level and the corresponding prize money is updated.
4. If the answer is incorrect, the user falls to a lower level (if applicable) and the prize money is updated accordingly.
5. The game ends if the user chooses to quit or provides an incorrect answer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

