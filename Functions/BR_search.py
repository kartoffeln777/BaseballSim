def BR_search(query):

  url = "http://www.baseball-reference.com/pl/player_search.cgi?search="
  query = query.split()
  for i in query:
    url += i
    url += "+"
  url = url[0:(len(url)-1)]

  return url
