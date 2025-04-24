import re


the_input = input()

start = the_input.find("<title>") + len("<title>")
end = the_input.find("</title>")

title = the_input[start:end]

start_body =the_input.find("<body>") + len("<body>")
end_body = the_input.find("</body>")

body = the_input[start_body:end_body]



clean = re.sub(r"<.*?>", "", body).strip()

clean = clean.replace('\\n','')



print(f"Title: {title}")
print(f"Content: {clean}")