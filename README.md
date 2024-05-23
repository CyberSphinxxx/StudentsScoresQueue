# Student Exam Score Queue Manager

This Python script manages a queue of student exam scores, allowing the user to input student names and their corresponding scores. The script employs the `queue.Queue` class from the Python standard library to handle up to 20 students. It provides the following functionalities:

1. **Input Collection**: Continuously prompts the user to enter student names and their scores until the queue is full or the user types 'done'.
2. **Error Handling**: Ensures that the score entered is a valid integer, prompting the user again in case of invalid input.
3. **Queue Status**: Displays whether the queue is empty or not after the input collection phase.
4. **Score Display**: Prints all entered scores and separately lists perfect scores (scores of 100).

## Code

```python
import queue

def main():
    exam_queue = queue.Queue(maxsize=20)

    while not exam_queue.full():
        name = input("Enter the student's name (or type 'done' to finish): ")
        if name == 'done':
            break
        try:
            score = int(input(f"Enter {name}'s score: "))
            exam_queue.put((name, score))
        except ValueError:
            print("Invalid score. Please enter a number.")

    print("\nThe queue is empty." if exam_queue.empty() else "\nThe queue is not empty.")

    print("\nScores:")
    print_scores(exam_queue, perfect=False)

    print("\nPerfect Scores:")
    print_scores(exam_queue, perfect=True)

def print_scores(q, perfect):
    for _ in range(q.qsize()):
        name, score = q.get()
        if (perfect and score == 100) or (not perfect and score != 100):
            print(f"{name} = {score}")
        q.put((name, score))

if __name__ == "__main__":
    main()
