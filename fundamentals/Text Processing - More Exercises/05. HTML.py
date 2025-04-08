title_article = input()
content = input()


def for_title(title):
    print(f'<h1>')
    print(f'    {title}')


    print(f'</h1>')

for_title(title_article)

def for_content(content):
    print(f'<article>')
    print(f'    {content}')


    print(f'</article>')

for_content(content)

def comment_(comment):
    print(f'<div>')
    print(f'    {comment}')


    print(f'</div>')






while True:
    commentt = input()
    if commentt == 'end of comments':
        break
    comment_(commentt)