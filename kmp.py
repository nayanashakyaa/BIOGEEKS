import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def draw_state(text, pattern, start, info=""):
    plt.clf()
    plt.title("KMP Motif Visualization")

    # Draw text sequence
    for i, ch in enumerate(text):
        plt.text(i, 1, ch, fontsize=14, ha='center')

    # Draw pattern (motif)
    for i, ch in enumerate(pattern):
        plt.text(start + i, 0, ch, fontsize=14, ha='center', color='blue')

    # Info text (motif found message)
    plt.text(len(text) / 2, -0.6, info,
             fontsize=12, ha='center', color='green')

    plt.xlim(-1, len(text))
    plt.ylim(-1, 2)
    plt.axis("off")
    plt.pause(0.7)


def kmp_visual(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    positions = []

    plt.figure(figsize=(11, 3))

    while i < len(text):
        draw_state(text, pattern, i - j)

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            pos = i - j
            positions.append(pos)

            # Show motif found message ON plot
            draw_state(
                text,
                pattern,
                pos,
                f"Motif FOUND at position {pos}"
            )

            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    # Final message stays on screen
    if positions:
        final_msg = f"Motif found at positions: {positions}"
    else:
        final_msg = "Motif NOT found"

    draw_state(text, pattern, -10, final_msg)
    plt.show()


def start():
    text = text_entry.get()
    pattern = pattern_entry.get()

    if not text or not pattern:
        messagebox.showerror("Error", "Enter both text and pattern")
        return

    kmp_visual(text, pattern)


# ---------- GUI ----------
root = tk.Tk()
root.title("KMP Motif Finder (Visual)")

tk.Label(root, text="Text (Sequence):").pack()
text_entry = tk.Entry(root, width=45)
text_entry.pack()

tk.Label(root, text="Pattern (Motif):").pack()
pattern_entry = tk.Entry(root, width=45)
pattern_entry.pack()

tk.Button(root, text="Start Visualization", command=start).pack(pady=10)

root.mainloop()