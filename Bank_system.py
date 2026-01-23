# ================================
# Smart Bank System (Backend)
# Language : Python
# Concept  : OOP (Object Oriented Programming)
# ================================


class BankAccount:
    """
    This class represents a bank account.
    It stores customer details and provides
    methods for banking operations.
    """

    def __init__(self, name, account_no, balance=0):
        # Encapsulation: data stored inside object
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        """
        Adds money to the account
        """
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        """
        Withdraws money if balance is sufficient
        """
        if amount <= self.balance:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully."
        else:
            return "Insufficient balance."

    def get_balance(self):
        """
        Returns current balance
        """
        return self.balance

    def account_summary(self):
        """
        Returns customer details
        """
        return {
            "Name": self.name,
            "Account No": self.account_no,
            "Balance": self.balance
        }


# ================================
# Child Class (Inheritance)
# ================================
class PremiumAccount(BankAccount):
    """
    Premium account inherits BankAccount
    Demonstrates inheritance
    """

    def __init__(self, name, account_no, balance, reward_points=0):
        super().__init__(name, account_no, balance)
        self.reward_points = reward_points

    def add_rewards(self, points):
        self.reward_points += points

    def premium_summary(self):
        data = self.account_summary()
        data["Reward Points"] = self.reward_points
        return data


# ================================
# DEMO (This simulates UI actions)
# ================================
if __name__ == "__main__":

    # Creating object (Object Creation)
    customer = PremiumAccount(
        name="Rajendra Mahapatra",
        account_no="1234567890",
        balance=69000
    )

    # Deposit operation
    print(customer.deposit(5000))

    # Withdraw operation
    print(customer.withdraw(1000))

    # Add reward points
    customer.add_rewards(50)

    # Display summary
    print("\n--- Account Summary ---")
    summary = customer.premium_summary()
    for key, value in summary.items():
        print(f"{key} : {value}")

