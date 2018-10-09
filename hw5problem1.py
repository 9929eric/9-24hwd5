romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his life… over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life forever.", ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])
header = "Here are my favorite romance movies:"
print(header)
print(" ")
romantic_movie_list = [romantic_movie1,romantic_movie2, romantic_movie3]
for movie in romantic_movie_list:
   print(movie[0],sep = " ", end = '')
   print(' (' ,movie[1],")",sep = '', end = ': ')
   print(movie[3])
   print(" ")
