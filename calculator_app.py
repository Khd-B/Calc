import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    # Dropdown menu for operations
    operation = st.selectbox("Select an operation:", ['+', '-', '*', '/'])

    # Calculate the result based on the selected operation
    if st.button("Calculate"):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."

        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
