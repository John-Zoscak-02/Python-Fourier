from collections import deque
from future.moves import tkinter


class FourierWindow:

    def __init__(self):
        self.time = 0
        self.vectors = []
        self.top = tkinter.Tk()
        self.top.mainloop()
        print("hello world")

    def draw_vectors(self, vectors):
        self.vectors = vectors
        vector_dequeue = deque(vectors)
        while vector_dequeue:
            self.draw_vector(vector_dequeue[0])
            vector_dequeue.popleft()

    # @staticmethod
    # def draw_vector():


    def main():
        import tkinter
        top = tkinter.Tk()
        canvas = tkinter.Canvas(master=top, height=700, width=1000)
        canvas.pack()

        top.mainloop()

    if __name__ == "__main__":
        main()


