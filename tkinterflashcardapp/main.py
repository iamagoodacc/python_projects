from tkinter import *

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")

        self.flashcards = []

        self.question_label = Label(root, text="Question:")
        self.question_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.answer_label = Label(root, text="Answer:")
        self.answer_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.question_entry = Entry(root, width=50)
        self.question_entry.grid(row=0, column=0, padx=85, pady=5, sticky=W)

        self.answer_entry = Entry(root, width=50)
        self.answer_entry.grid(row=1, column=0, padx=85, pady=5, sticky=W)


        self.add_button = Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.grid(row=2, column=0, padx=80, pady=5, sticky=W)

        self.delete_button = Button(root, text="Delete Flashcard", command=self.delete_flashcard)
        self.delete_button.grid(row=2, column=0, padx=200, pady=5, sticky=W)

        self.review_button = Button(root, text="Review Flashcards", command=self.review_flashcards)
        self.review_button.grid(row=3, column=0, padx=75, pady=5, sticky=W)

        self.browse_button = Button(root, text="Browse Flashcards", command=self.browse_flashcards)
        self.browse_button.grid(row=3, column=0, padx=200, pady=5, sticky=W)

        self.load_flashcards()

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append((question, answer))
            self.clear_entries()
        self.save_flashcards() #auto saving

    def delete_flashcard(self):
        if self.flashcards:
            self.flashcards.pop()
            self.save_flashcards()

    def clear_entries(self):
        self.question_entry.delete(0, END)
        self.answer_entry.delete(0, END)

    def load_flashcards(self):
        try:
            with open("D:\Visual Studio\Python\FLASHCARDAPP\cards.txt", "r") as file:
                for line in file:
                    question, answer = line.strip().split(":")
                    self.flashcards.append((question, answer))
        except FileNotFoundError:
            pass

    def save_flashcards(self):
        with open("D:\Visual Studio\Python\FLASHCARDAPP\cards.txt", "w") as file:
            for flashcard in self.flashcards:
                file.write(f"{flashcard[0]}:{flashcard[1]}\n")

    def review_flashcards(self):
        review_window = Toplevel(self.root)
        review_window.title("Flashcard Review")

        review_window.geometry("200x100")

        self.current_index = 0

        self.question_label_review = Label(review_window, text="", wraplength=400)
        self.question_label_review.grid(row=0, column=0, padx=85, pady=5, sticky=W)

        self.show_answer_button = Button(review_window, text="Show Answer", command=self.show_answer)
        self.show_answer_button.grid(row=1, column=0, padx=65, pady=5, sticky=W)

        self.next_button = Button(review_window, text="Next", command=self.show_next_flashcard)
        self.next_button.grid(row=2, column=0, padx=85, pady=5, sticky=W)

        self.show_flashcard()

    def show_flashcard(self):
        if self.flashcards:
            question, _ = self.flashcards[self.current_index]
            self.question_label_review.config(text=question)
        else:
            self.question_label_review.config(text="No flashcards to review.")

    def show_answer(self):
        if self.flashcards:
            _, answer = self.flashcards[self.current_index]
            self.question_label_review.config(text=answer)

    def show_next_flashcard(self):
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.show_flashcard()
        else:
            self.question_label_review.config(text="End of flashcards.")


    def browse_flashcards(self):
        browse_window = Toplevel(self.root)
        browse_window.title("Browse Flashcards")

        browse_listbox = Listbox(browse_window, width=50)
        browse_listbox.pack(padx=5, pady=5, fill=BOTH, expand=True)

        for index, (question, answer) in enumerate(self.flashcards):
            browse_listbox.insert(END, f"Q: [{question}]\n A: [{answer}]\n")

if __name__ == "__main__":
    root = Tk()
    app = FlashcardApp(root)
    root.mainloop()
