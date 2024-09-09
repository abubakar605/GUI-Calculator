import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("830x670+250+10")
        self.root.configure(bg='#000000')

        self.expression = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Display widget
        self.display = tk.Entry(self.root, font=('Segoe UI', 30), bg='#1E1E1E', fg='white', bd=0, relief=tk.FLAT, justify='right')
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Heading for history display
        history_heading = tk.Label(self.root, text="HISTORY", font=('Segoe UI', 16, 'bold'), bg='#000000', fg='#FFFFFF')
        history_heading.grid(row=1, column=0, columnspan=5, pady=10)

        # Calculation history display
        self.history_display = tk.Text(self.root, font=('Segoe UI', 14), bg='#333333', fg='#FFFFFF', bd=0, relief=tk.FLAT, height=5)  # Adjusted height here
        self.history_display.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'CLR',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', 'sqrt',
            'sin', 'cos', 'tan', 'pow', 'DEL',
            'BMI', 'Clear History', 'Currency'
        ]

        row_val = 3
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.button_press(x)
            if button == 'BMI':
                tk.Button(self.root, text=button, width=10, height=3, command=self.open_bmi_window, font=('Arial', 10, 'bold'), bg='#191970', fg='white', bd=0, relief='flat', highlightbackground='#444444').grid(row=row_val, column=col_val, padx=2, pady=2)  # Adjusted padx and pady
                col_val += 1
            elif button == 'Clear History':
                tk.Button(self.root, text=button, width=10, height=3, command=self.clear_history, font=('Arial', 10, 'bold'), bg='#D32F2F', fg='#FFFFFF', bd=0, relief='flat', highlightbackground='#444444').grid(row=row_val, column=col_val, padx=2, pady=2)  # Adjusted padx and pady
                col_val += 1
            elif button == 'Currency':
                tk.Button(self.root, text=button, width=10, height=3, command=self.open_currency_converter, font=('Arial', 10, 'bold'), bg='#191970', fg='white', bd=0, relief='flat', highlightbackground='#444444').grid(row=row_val, column=col_val, padx=2, pady=2)  # Adjusted padx and pady
                col_val += 1
            else:
                tk.Button(self.root, text=button, width=10, height=3, command=action, font=('Arial', 10, 'bold'), bg='#333333', fg='white', bd=0, relief='flat', highlightbackground='#444444').grid(row=row_val, column=col_val, padx=2, pady=2)  # Adjusted padx and pady
                col_val += 1

            if col_val > 4:
                col_val = 0
                row_val += 1

    def button_press(self, key):
        if key == "=":
            self.calculate_expression()
        elif key == "CLR":
            self.clear_display()
        elif key == "DEL":
            self.delete_last_character()
        elif key in ['sqrt', 'sin', 'cos', 'tan', 'pow']:
            self.handle_functions(key)
        else:
            self.expression += str(key)
            self.update_display()

    def calculate_expression(self):
        try:
            # Ensure the expression is closed properly
            open_paren_count = self.expression.count('(')
            close_paren_count = self.expression.count(')')
            self.expression += ')' * (open_paren_count - close_paren_count)

            result = eval(self.expression, {"__builtins__": None}, {
                'sqrt': math.sqrt,
                'sin': lambda x: math.sin(math.radians(x)),
                'cos': lambda x: math.cos(math.radians(x)),
                'tan': lambda x: math.tan(math.radians(x)),
                'pow': pow  # Directly use pow here
            })
            history_entry = f"{self.expression} = {result}"
            self.expression = str(result)
            self.update_display()
            self.update_history(history_entry)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def handle_functions(self, func):
        if func == 'sqrt':
            self.expression += 'sqrt('
        elif func == 'sin':
            self.expression += 'sin('
        elif func == 'cos':
            self.expression += 'cos('
        elif func == 'tan':
            self.expression += 'tan('
        elif func == 'pow':
            self.expression += '**('  # Use ** instead of pow for the expression
        self.update_display()

    def delete_last_character(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def clear_display(self):
        self.expression = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def update_history(self, entry):
        self.history.append(entry)
        self.history_display.delete(1.0, tk.END)
        for entry in self.history:
            self.history_display.insert(tk.END, f"{entry}\n")

    def clear_history(self):
        self.history = []
        self.history_display.delete(1.0, tk.END)

    def open_bmi_window(self):
        bmi_window = tk.Toplevel(self.root)
        bmi_window.title("BMI Calculator")
        bmi_window.geometry("250x200")
        bmi_window.configure(bg='#000000')

        tk.Label(bmi_window, text="Height (feet):", bg='#000000', fg='white').grid(row=0, column=0, pady=5, padx=5)
        height_feet_entry = tk.Entry(bmi_window, bg='#000000', fg='white')
        height_feet_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(bmi_window, text="Height (inches):", bg='#000000', fg='white').grid(row=1, column=0, pady=5, padx=5)
        height_inches_entry = tk.Entry(bmi_window, bg='#000000', fg='white')
        height_inches_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(bmi_window, text="Weight (kg):", bg='#000000', fg='white').grid(row=2, column=0, pady=5, padx=5)
        weight_entry = tk.Entry(bmi_window, bg='#000000', fg='white')
        weight_entry.grid(row=2, column=1, pady=5, padx=5)

        def calculate_bmi():
            try:
                height_feet = float(height_feet_entry.get())
                height_inches = float(height_inches_entry.get())
                weight_kg = float(weight_entry.get())
                
                total_height_inches = height_feet * 12 + height_inches
                height_meters = total_height_inches * 0.0254
                bmi = weight_kg / (height_meters ** 2)
                bmi_result = f"BMI: {bmi:.2f}"

                history_entry = f"Height: {height_feet} feet {height_inches} inches, Weight: {weight_kg} kg, {bmi_result}"
                self.update_history(history_entry)

                result_label.config(text=bmi_result)
            except ValueError:
                messagebox.showerror("Input error", "Please enter valid numbers for height and weight")

        tk.Button(bmi_window, text="Calculate BMI", command=calculate_bmi, bg='#000000', fg='white').grid(row=3, columnspan=2, pady=10)
        result_label = tk.Label(bmi_window, text="", bg='#000000', fg='white')
        result_label.grid(row=4, columnspan=2, pady=5)

    def open_currency_converter(self):
        currency_window = tk.Toplevel(self.root)
        currency_window.title("Currency Converter")
        currency_window.geometry("250x200")
        currency_window.configure(bg='#000000')

        currencies = ['PKR', 'YEN', 'USD', 'Dirham']

        tk.Label(currency_window, text="Amount:", bg='#000000', fg='white').grid(row=0, column=0, pady=5, padx=5)
        amount_entry = tk.Entry(currency_window, bg='#000000', fg='white')
        amount_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(currency_window, text="From:", bg='#000000', fg='white').grid(row=1, column=0, pady=5, padx=5)
        from_currency = tk.StringVar(currency_window)
        from_currency.set(currencies[0])
        from_currency_menu = tk.OptionMenu(currency_window, from_currency, *currencies)
        from_currency_menu.config(bg='#000000', fg='white')
        from_currency_menu.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(currency_window, text="To:", bg='#000000', fg='white').grid(row=2, column=0, pady=5, padx=5)
        to_currency = tk.StringVar(currency_window)
        to_currency.set(currencies[1])
        to_currency_menu = tk.OptionMenu(currency_window, to_currency, *currencies)
        to_currency_menu.config(bg='#000000', fg='white')
        to_currency_menu.grid(row=2, column=1, pady=5, padx=5)

        def convert_currency():
            try:
                amount = float(amount_entry.get())
                from_curr = from_currency.get()
                to_curr = to_currency.get()

                rates = {
                    'PKR': {'USD': 0.0057, 'YEN': 0.62, 'Dirham': 0.021},
                    'USD': {'PKR': 175.68, 'YEN': 109.62, 'Dirham': 3.67},
                    'YEN': {'PKR': 1.61, 'USD': 0.0091, 'Dirham': 0.033},
                    'Dirham': {'PKR': 47.96, 'USD': 0.27, 'YEN': 30.12}
                }

                conversion_rate = rates[from_curr][to_curr]
                converted_amount = amount * conversion_rate
                conversion_result = f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}"

                history_entry = f"Converted {amount} {from_curr} to {to_curr}: {converted_amount:.2f} {to_curr}"
                self.update_history(history_entry)

                result_label.config(text=conversion_result)
            except ValueError:
                messagebox.showerror("Input error", "Please enter a valid amount")
            except KeyError:
                messagebox.showerror("Conversion error", "Unsupported currency conversion")

        tk.Button(currency_window, text="Convert", command=convert_currency, bg='#333333', fg='white').grid(row=3, columnspan=2, pady=10)
        result_label = tk.Label(currency_window, text="", bg='#000000', fg='white')
        result_label.grid(row=4, columnspan=2, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()