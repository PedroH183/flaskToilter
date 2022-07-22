from app import db

class User(db.Model): # todas as classes são heranças de DB.MODEL
    __tablename__ = "users" # parametro especial para denominar a tabela

    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        

    def __repr__(self):
        return "<User %r>" % self.username # %r == converte em string, mas é usada para representar um objeto em python 

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.Text)

    owner = db.relationship('User', foreign_keys = user_id) # criando um relacionamento com a tabela User 

    def __init__(self,content, user_id):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id') )
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id') )
    
    user = db.relationship('User', foreign_keys = user_id)
    follower = db.relationship('User', foreign_keys = follower_id)
