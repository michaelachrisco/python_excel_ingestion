class Transaction:
    def __init__(self, transaction_date, amount, description, running_total):
        self.transaction_date = transaction_date
        self.amount = amount
        self.description = description
        self.running_total = running_total

    def get_transaction_date(self):
        return self.transaction_date

    def get_amount(self):
        return self.amount

    def get_description(self):
        return self.description

    def get_running_total(self):
        return self.running_total

    def save(self,conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO transactions (transaction_date, amount, description, running_total) VALUES (%s, %s, %s, %s)",
                    (self.transaction_date, self.amount * 1.00, self.description, self.running_total))
        conn.commit()
        cur.close()

    def __str__(self):
        return 'transaction_date: ' + self.transaction_date.strftime('%m/%d/%y') + " amount: " + str(self.amount) + " description: " + self.description + " running_total: " + str(self.running_total)

