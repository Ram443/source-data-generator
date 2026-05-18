from DataGenerator import DataGenerator

gen = DataGenerator()

customer = gen.generate_customers(5)
accounts = gen.generate_accounts(customer,5)

print(customer.sample())