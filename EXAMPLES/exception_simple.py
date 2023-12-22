
try:  # Execute code that might have a problem
    x = 5
    open("i_do_not_exist.txt")
    y = "cheese"
    z = x + y
    print("Bottom of try")

except (TypeError, FileNotFoundError) as err:    # Catch the expected error; assign error object to err
    print("Naughty programmer! ", err)
except Exception as err:
#    pass
    print("Did not expect", err)



print("After try-except")  # Get here whether or not exception occurred
