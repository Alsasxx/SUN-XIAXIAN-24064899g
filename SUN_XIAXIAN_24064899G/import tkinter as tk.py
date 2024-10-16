import tkinter as tk
import random

class BallApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Click to Create Balls")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.create_ball)

    def create_ball(self, event):
        # 生成随机位置和大小的小球
        x = event.x
        y = event.y
        size = random.randint(10, 30)  # 随机大小
        self.draw_ball(x, y, size)

    def draw_ball(self, x, y, size):
        # 在画布上绘制小球
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = BallApp(root)
    root.mainloop()
