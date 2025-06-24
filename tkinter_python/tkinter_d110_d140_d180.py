import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

D140_D180 = {}

def upload_files(frame, file_list, prepare_btn):
    """Upload and display selected files."""
    files = filedialog.askopenfilenames(filetypes=[("XML files", "*.xml"), ("All Files", "*.*")])
    
    for file in files:
        if file not in file_list:  # Avoid duplicates
            file_list.append(file)
    
    display_files(frame, file_list, prepare_btn)

def remove_file(file, frame, file_list, prepare_btn):
    """Remove a file and update the display."""
    file_list.remove(file)
    display_files(frame, file_list, prepare_btn)
    prepare_btn.config(state="disabled")

def display_files(frame, file_list, prepare_btn):
    """Update displayed file list with remove buttons."""
    for widget in frame.winfo_children():
        widget.destroy()

    for file in file_list:
        file_frame = tk.Frame(frame)
        file_frame.pack(fill="x", pady=2)

        file_label = tk.Label(file_frame, text=os.path.basename(file), anchor="w", width=30)
        file_label.pack(side="left", padx=5)

        remove_btn = tk.Button(file_frame, text="✖", fg="red", width=3, 
                               command=lambda f=file: remove_file(f, frame, file_list, prepare_btn))
        remove_btn.pack(side="right", padx=5)

    if file_list:
        prepare_btn.config(state="normal")  # Enable "Prepare" button when files exist

def process_d110_xml_files(file_list, output_name):
    """Read multiple XML files, concatenate, and save as a single Excel file."""
    dfs = []
    for file in file_list:
        try:
            df = pd.read_xml(file,xpath="//G_TRX_NO")
            dfs.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")

    if dfs:
        final_df = pd.concat(dfs, ignore_index=True)
        output_file = os.path.join(os.path.dirname(file_list[0]), f"{output_name}.xlsx")
        final_df.to_excel(output_file, index=False)
        return output_file
    return None

def process_d140_xml_files(file_list, output_name):
    dfs = []
    for file in file_list:
        try:
            df = pd.read_xml(file,xpath="//G_TRX_CHAR_DATE")
            dfs.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")

    if dfs:
        global D140_D180
        final_df = pd.concat(dfs, ignore_index=True)
        D140_D180.update({"D140":final_df})
        output_file = os.path.join(os.path.dirname(file_list[0]), f"{output_name}.xlsx")
        final_df.to_excel(output_file, index=False)
        return output_file
    return None

def process_d180_xml_files(file_list, output_name):
    dfs = []
    for file in file_list:
        try:
            df = pd.read_xml(file,xpath="//G_TRX_CHAR_DATE")
            dfs.append(df)
        except Exception as e:
            print(f"Error processing {file}: {e}")

    if dfs:
        global D140_D180
        final_df = pd.concat(dfs, ignore_index=True)
        D140_D180.update({"D180":final_df})
        output_file = os.path.join(os.path.dirname(file_list[0]), f"{output_name}.xlsx")
        final_df.to_excel(output_file, index=False)
        return output_file
    return None


def prepare_action(file_type, file_list):
    """Process selected files and show the saved location."""
    if not file_list:
        messagebox.showwarning("No Files", f"No {file_type} files selected.")
        return

    print(f"Processing {file_type} files...")
    if file_type == "D110":
        output_file = process_d110_xml_files(file_list, f"{file_type}_Processed")
    elif file_type == "D140":
        output_file = process_d140_xml_files(file_list, f"{file_type}_Processed")
    elif file_type == "D180":
        output_file = process_d180_xml_files(file_list, f"{file_type}_Processed")
    if output_file:
        messagebox.showinfo("File Saved", f"Processed file saved at:\n{output_file}")
    else:
        messagebox.showerror("Error", f"Failed to process {file_type} files.")

def create_file_section(root, file_type):
    """Create a section for each file type."""
    frame = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
    frame.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

    tk.Label(frame, text=f"{file_type} Processing", font=("Arial", 10, "bold")).pack()

    file_list = []
    file_display_frame = tk.Frame(frame)
    file_display_frame.pack(pady=5)

    prepare_btn = tk.Button(frame, text="Prepare & Show File Location", bg="#FFD580", width=30, state="disabled",
                            command=lambda: prepare_action(file_type, file_list))
    prepare_btn.pack(pady=5)

    upload_btn = tk.Button(frame, text="📂 Upload Files",
                           command=lambda: upload_files(file_display_frame, file_list, prepare_btn))
    upload_btn.pack(pady=5)


def reconcile_button():
    global D140_D180
    if "D140" in D140_D180 and "D180" in D140_D180:
        print(D140_D180)
    else:
        messagebox.showerror("Error", f"Upload Both D140 & D180 files.")

# Create main window
root = tk.Tk()
reconcile_btn = tk.Button(root, text="Reconcile Files", bg="#FFD580", width=30,
                            command=lambda: reconcile_button())
reconcile_btn.pack(pady=10)
root.title("File Processing")
root.geometry("900x300")
# Create sections for each file type
for file_type in ["D110", "D140", "D180"]:
    create_file_section(root, file_type)
print(D140_D180,"%"*100)
root.mainloop()