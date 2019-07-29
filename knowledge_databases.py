from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	new_article = Knowledge(
		name = name,
		topic = topic,
		rating = rating)
	session.add(new_article)
	session.commit()

def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge

def query_article_by_topic():
	article = session.query(Knowledge).filter_by(
		name=name).first()
	return article

def delete_article_by_topic():
	article = session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()

def delete_all_articles():
	article = session.query(Knowledge).filter_by(
		name=name).delete()
	session.commit()


def edit_article_rating():
	pass

add_article("Hedgehog", "Cute things", 10)