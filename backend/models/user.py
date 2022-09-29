from database.database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    article = relationship("ArticleModel", back_populates="author")
    news_article = relationship("NewsArticleModel", back_populates="author")
