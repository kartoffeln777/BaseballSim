def generalize_player_name(name):
	
  playerName = name.lower()
  playerName = name.strip()
  playerName = name.replace(" ", "_")
  print "\n" + playerName + "\n"

  return playerName
