
def add_songs(*args):
    list_with_songs = {}
    for song_title,list_ in args:
        if song_title not in list_with_songs:
            list_with_songs[song_title] = []
        if not list_:
            continue
        if song_title in list_with_songs:
            if list_:
                for n in list_:
                    list_with_songs[song_title].append(n)

    result = []
    if list_with_songs:
        for song_name,lyrics in list_with_songs.items():
            if not lyrics:
                result.append(f'- {song_name}')

            else:
                result.append(f'- {song_name}')
                for t in lyrics:
                    result.append(f'{t}')




    return '\n'.join(result)



print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))