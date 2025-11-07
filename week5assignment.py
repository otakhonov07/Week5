def add_new_orders(orders, new_orders):
    """
    Adds each order from new_orders to the end of orders.
    Modifies the orders list in-place.
    """
    for new_order in new_orders:       
        orders.append(new_order)       



def process_orders(orders, num_to_process):
    """
    Removes the first num_to_process orders from the list and returns them.
    If num_to_process > len(orders), process all remaining orders.
    """
    processed = []                    

   
    for i in range(num_to_process):
        if len(orders) == 0:          
            break
        processed_order = orders.pop(0)  
        processed.append(processed_order)
    
    return processed



def cancel_order(orders, order_id):
    """
    Searches for order_id in the orders list and removes its first occurrence.
    Returns True if found and removed, False otherwise.
    """
    if order_id in orders:             
        orders.remove(order_id)       
        return True
    else:
        return False


def manage_orders(initial_orders, new_orders_to_add, orders_to_process, order_to_cancel):
    """
    Manages the full workflow: add, cancel, and process orders.
    Returns final orders list and processed orders list.
    """
    
    current_orders = initial_orders[:]     

 
    add_new_orders(current_orders, new_orders_to_add)

    cancel_order(current_orders, order_to_cancel)

    processed_orders = process_orders(current_orders, orders_to_process)

    return current_orders, processed_orders


initial = [101, 102, 103, 104]
new = [105, 106]
process_count = 3
cancel_id = 103

final_state, processed = manage_orders(initial, new, process_count, cancel_id)

print("Test Case 1 Results:")
print("final_state:", final_state)
print("processed:", processed)
print("Original initial list (should be unchanged):", initial)
