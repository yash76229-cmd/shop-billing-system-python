print("====== WELCOME TO PYTHON SHOP BILLING SYSTEM ======")

items = []
total_amount = 0

while True:
    name = input("\nEnter product name: ")
    price = float(input("Enter product price: ₹"))
    qty = int(input("Enter quantity: "))

    item_total = price * qty
    total_amount += item_total

    items.append((name, price, qty, item_total))

    more = input("Do you want to add another item? (yes/no): ").lower()
    if more != 'yes':
        break

# GST Calculation (18%)
gst = total_amount * 0.18

# Discount Logic
discount = 0
if total_amount > 5000:
    discount = total_amount * 0.10   # 10% discount
elif total_amount > 2000:
    discount = total_amount * 0.05   # 5% discount

final_amount = total_amount + gst - discount

# Display Bill
print("\n\n============= FINAL BILL =============")
print("{:<15} {:<10} {:<10} {:<10}".format("Product", "Price", "Qty", "Total"))

for item in items:
    print("{:<15} {:<10} {:<10} {:<10}".format(item[0], item[1], item[2], item[3]))

print("--------------------------------------")
print(f"Subtotal: ₹{total_amount:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Discount: -₹{discount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
print("======================================")

# Save Bill to File
with open("bill.txt", "w") as file:
    file.write("=========== SHOP BILL ===========\n")
    file.write("{:<15} {:<10} {:<10} {:<10}\n".format("Product", "Price", "Qty", "Total"))
    
    for item in items:
        file.write("{:<15} {:<10} {:<10} {:<10}\n".format(item[0], item[1], item[2], item[3]))
    
    file.write("---------------------------------\n")
    file.write(f"Subtotal: ₹{total_amount:.2f}\n")
    file.write(f"GST (18%): ₹{gst:.2f}\n")
    file.write(f"Discount: -₹{discount:.2f}\n")
    file.write(f"Final Amount: ₹{final_amount:.2f}\n")

print("\nBill saved successfully to 'bill.txt'")
print("Thank you for shopping with us! 🛍️")