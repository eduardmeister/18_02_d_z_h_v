from model.movie import Movie


class MovieDAO:
    def __int__(self, session):
        self.session = session
        self.model = Movie

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, mid):
        return self.session.query(self.model).get(mid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        mid = data.pop('id')
        movie = self.get_by_id(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)

            self.session.add(movie)
            self.session.commit()

    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
