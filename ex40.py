# Learn Python the Hard Way - Exercise No. 40
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

daisy = ["Daisy",
	"Daisy",
	"Give me your answer do",
	"I'm half crazy over the love of you"]

daisy = Song(daisy)

daisy.sing_me_a_song()