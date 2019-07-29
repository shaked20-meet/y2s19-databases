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

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		topic=topic).first()
	return article
# def query_article_by_rating(threshold):
# 	global rating
# 	article = session.query(Knowledge).filter_by(
# 		rating = rating).first()
# 	if article.rating < threshold:
# 		return article
# 	return None
def delete_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()

def delete_all_articles():
	article = session.query(Knowledge).delete()
	session.commit()


def edit_article_rating(updated_rating, name):
	article = session.query(
		Knowledge).filter_by(
		name=name).first()
	article.rating = updated_rating
	session.commit()	

#add_article("Hedgehog", "Cute things", 10)
#add_article("Macaroons", "Tasty things", 9)
#add_article("Flute", "Music", 7)
#delete_all_articles()
#edit_article_rating(10, "Flute")
print(query_all_articles())