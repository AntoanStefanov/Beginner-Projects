
import random


def get_word():
    words = ['python', 'javascript', 'monday', 'work', 'django',
             'google', 'facebook', 'slack', 'github', 'developer', 'hangman']
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = ['-'] * len(word)
    max_wrong_chars = 8
    wrong_chars = 0
    is_solved = False

    print("Let's Play Hangman!")
    print(' '.join(word_completion))
    print("Tries:", max_wrong_chars)

    while wrong_chars < max_wrong_chars:

        char = input('Please enter a letter: ').upper()
        if not char.isalpha():
            continue
        if char in word:
            print('Correct letter')
            for index, letter in enumerate(word):
                if char == letter:
                    word_completion[index] = letter
                    if '-' not in word_completion:
                        is_solved = True
                        break
            print(' '.join(word_completion))
        else:
            wrong_chars += 1
            print(' '.join(word_completion))
            print(f'Left tries: {max_wrong_chars - wrong_chars}')
        if is_solved:
            break

    if is_solved:
        print('Solved!')
    else:
        print('Game Over.')


def main():
    word = get_word()
    play(word)
    while input('Play Again ? (Y/N) ').upper() == 'Y':
        word = get_word()
        play(word)


main()
