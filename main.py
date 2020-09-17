# Author: Andrew Wang aqw5628@psu.edu
# Collaborator: Chris Belt cob5463@psu.edu
# Collaborator: Eric Beardslee eab6024@psu.edu
# Collaborator: Devanshi Mittal dfm5688@psu.edu
# Section: 005R
# Breakout: 7

def sum_n(n):
  if (n>0):
    return n + sum_n(n-1);
  else:
    return 0;

def print_n(s, n):
  if (n>0):
    print (f"{s}");
    print_n(s, n-1);

def run():
  init_num = int(input("Enter an int: "));
  fin_num = sum_n(init_num);
  print(f"sum is {fin_num}.");
  init_string = str(input("Enter a string: "));
  print_n(init_string, init_num);

if __name__ == "__main__":
  run();