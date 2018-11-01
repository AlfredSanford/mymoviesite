import web
urls = (
    '/', 'Index',
    '/movie/(\d+)', 'Movie',
)
db = web.database(dbn='sqlite', db='MovieSite.db')
#movies = [{'title': 'Forrest Gump', 'year': 1994, }, {'title': 'Titanic', 'year': 1997, }, ]
render = web.template.render('templates/')
class Index:
	def GET(self):
		movies = db.select('movie')
#		page = ''
#		for m in movies:
#			page += '%s (%d)\n' % (m['title'], m['year'])
		return render.index(movies)

class Movie:
	def GET(self, movie_id):
		movie_id = int(movie_id)
#		condition = 'id=' + movie_id
#		movie = db.select('movie', where=condition, vars=locals())[0]
		movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
		return render.movie(movie)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
