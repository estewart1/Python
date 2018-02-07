def shut_down(s):
  if s == "yes":
    print("Shutting down")
  elif s == "no":
    print("Shutdown aborted")
  else:
    print("Sorry")
shut_down(raw_input("Do you want to shudown? "))

# Practice Using if/elif/else