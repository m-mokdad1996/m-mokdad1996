def countDigits(num):
  
  if (num == 0):
    return 0
  return 1 + countDigits(num//10) 
def findMax():
  list = []
  elements = int(input("how many elements you want to add on list: "))
  for i in range(elements):
    integers = int(input("enter an integer:"))
    list.append(integers)
  def find_max_recursive(s):
     if (len(s) == 1):
       return s[0]
     else:
       return max(s[0],find_max_recursive(s[1:]))

  return find_max_recursive(list)
  
def countTags(html,tag):
  if '<' + tag + '>' in html or '</' + tag + '>' in html:
        if '<' + tag + '>' in html:
            html = html.replace('<' + tag + '>', '', 1)
        if '</' + tag + '>' in html:
            html = html.replace('</' + tag + '>', '', 1)
        return 1 + countTags(html, tag)
  else:
        return 0

def main():
  html_code ="""
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""
  while True:
    print("1. Count Digits") 
    print("2. Find Max")
    print("3. Count Tags") 
    print("4. Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
      number = int(input("enter an integer: "))
      print(countDigits(number))
    elif choice == 2:
      print(findMax())
    elif choice == 3:
      tag_name = input("enter a tag name: ")
      print("Number of occurences of the tags:", countTags(html_code, tag_name))
    elif choice == 4:
      break
    else:
      print("error, please try again another choice")
   
if __name__ == "__main__":
  main()
         

  

