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
