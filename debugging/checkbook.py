class Checkbook:
    """
    Esta clase representa una chequera que permite realizar operaciones básicas como
    depósitos, retiros y consultar el balance actual.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de Checkbook con un balance de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Realiza un depósito en la cuenta y actualiza el balance.

        Args:
            amount (float): El monto a depositar en la cuenta.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Realiza un retiro de la cuenta si hay suficientes fondos y actualiza el balance.

        Args:
            amount (float): El monto a retirar de la cuenta.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Imprime el balance actual de la cuenta.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Función principal que permite al usuario interactuar con la chequera.
    Ofrece opciones para depositar, retirar, consultar el balance o salir.

    Args:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
