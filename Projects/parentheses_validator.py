string = "{(}"

def iterative_parentheses_validator(chars):
  new = []
  opened = ['(',  '[', '{']
  closed = [')', ']',  '}']
  char_dict = {'(':')', '[':']', '{':'}'}
  for char in chars:
    if char in opened:
      new.append(char)
    if char in closed:
      if len(new) == 0:
        return False
      elif char_dict[new.pop()] != char:
        return False
  return True

# print(iterative_parentheses_validator(string))

def recursive_parentheses_validator(chars):
  opened = ['(',  '[', '{']
  closed = [')', ']',  '}']
  char_dict = {'(':')', '[':']', '{':'}'}
  if len(chars) == 0:
    return True
  
  for i, char in enumerate(chars):
    if char in char_dict and char_dict[char] == chars[i+1]:
      return recursive_val(chars[:i] + chars[i+2:])
  
  return False
  
print(recursive_parentheses_validator(string))