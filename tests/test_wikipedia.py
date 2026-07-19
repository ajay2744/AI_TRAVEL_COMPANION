from app.clients.wikipedia import wiki

page = wiki.page("Mysore Palace")

print(page.exists())

print(page.title)

print(page.summary[:500])