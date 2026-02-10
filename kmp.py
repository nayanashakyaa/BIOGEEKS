import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

#  DNA Validation Logic
def is_valid_dna(seq):
    """Check if the sequence contains only A, T, G, and C."""
    valid_bases = {'A', 'T', 'G', 'C'}
    return all(char in valid_bases for char in seq)

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

# Animation function 
def draw_state(text, pattern, start, info=""):
    plt.clf()
    plt.title("KMP DNA Motif Visualization")
    for i, ch in enumerate(text):
        plt.text(i, 1, ch, fontsize=14, ha='center')
    for i, ch in enumerate(pattern):
        plt.text(start + i, 0, ch, fontsize=14, ha='center', color='blue')
    plt.text(len(text) / 2, -0.6, info, fontsize=12, ha='center', color='green')
    plt.xlim(-1, len(text))
    plt.ylim(-1, 2)
    plt.axis("off")
    plt.pause(0.5)

#  Add Frequency Graph
def plot_frequency(positions):
    """Generates a bar chart showing where motifs appear in the DNA."""
    if not positions:
        messagebox.showinfo("Result", "No matches found to plot.")
        return

    match_numbers = list(range(1, len(positions) + 1))
    plt.figure(figsize=(8, 5))
    plt.bar(match_numbers, positions, color='skyblue', edgecolor='navy')
    plt.xlabel("Match Occurence (1st, 2nd, 3rd...)")
    plt.ylabel("Index Position in DNA Sequence")
    plt.title("Distribution of DNA Motif")
    plt.xticks(match_numbers)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Save Results to File
def save_results(text, pattern, positions):
    """Saves findings to a text file for biological records."""
    filename = "kmp_dna_results.txt"
    with open(filename, "w") as file:
        file.write("DNA Pattern Finder using KMP Algorithm\n")
        file.write("=" * 40 + "\n")
        file.write(f"DNA Length: {len(text)}\n")
        file.write(f"Pattern Searched: {pattern}\n")
        file.write(f"Total Matches Found: {len(positions)}\n")
        file.write(f"Positions (0-indexed): {positions}\n")
    print(f"Results saved to {filename}")

def kmp_visual(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    
    # Store match positions
    positions = []

    plt.figure(figsize=(11, 3))
    while i < len(text):
        draw_state(text, pattern, i - j)
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            pos = i - j
            positions.append(pos) # Storing the match
            draw_state(text, pattern, pos, f"Motif FOUND at position {pos}")
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    plt.close() # Close animation before showing graph
    
    # Execution of additional requirements
    save_results(text, pattern, positions)
    plot_frequency(positions)

def start():
    # Convert to uppercase for DNA consistency
    text = text_entry.get().upper().strip()
    pattern = pattern_entry.get().upper().strip()

    if not text or not pattern:
        messagebox.showerror("Error", "Enter both DNA sequence and pattern")
        return

    #  DNA Validation Check
    if not is_valid_dna(text) or not is_valid_dna(pattern):
        messagebox.showerror(
            "Invalid DNA Sequence",
            "DNA sequence must contain only A, T, G, and C."
        )
        return

    kmp_visual(text, pattern)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("KMP DNA Motif Finder")

tk.Label(root, text="DNA Sequence (A, T, G, C):", font=('Arial', 10, 'bold')).pack(pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.pack(padx=20)

tk.Label(root, text="Target Motif (Pattern):", font=('Arial', 10, 'bold')).pack(pady=5)
pattern_entry = tk.Entry(root, width=50)
pattern_entry.pack(padx=20)

tk.Button(root, text="Run Bioinformatics Analysis", command=start, 
          bg="green", fg="white", font=('Arial', 10, 'bold')).pack(pady=20)

root.mainloop()