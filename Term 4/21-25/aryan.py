    def create(self):
        name = self.name_c.get()
        year = self.year_c.get()
        director = self.director_c.get()
        rate = self.rate_c.get()

        movie = Movie(name, year, director, rate)
        self.session.add(movie)
        self.session.commit()

        self.name_c.set('')
        self.year_c.set(2021)
        self.director_c.set('')
        self.rate_c.set(1)