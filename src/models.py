import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()




class User(Base):
                __tablename__ = 'user'
                id = Column(Integer, primary_key=True)
                username = Column(String(250), nullable=False)
                first_name = Column(String(250), nullable=False)
                last_name = Column(String(250), nullable=False)
                description = Column(String(250), nullable=True)
                email = Column(String(250), nullable=False)
                password = Column(String(250), nullable=False)
                profile_pic = Column(String(250), nullable=True)
                posts = relationship("Post", back_populates="user")
                followers = relationship("Followers", back_populates="user")
                following = relationship("Following", back_populates="user")
                stories = relationship("Story", back_populates="user")
                highlights = relationship("Highlight", back_populates="user")
                saved_posts = relationship("SavedPost", back_populates="user")
                locations = relationship("Location", back_populates="user")
                facebook_account = relationship("FacebookAccount", back_populates="user")
                direct_messages = relationship("DirectMessage", back_populates="user")
                blocked_users = relationship("BlockedUser", back_populates="user")
                account_type = relationship("AccountType", back_populates="user")

class Story (Base):
                __tablename__ = 'story'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                image = Column(String(250), nullable=False)
                views = relationship("View", back_populates="story")

class Post (Base):
                __tablename__ = 'post'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                caption = Column(String(250), nullable=False)
                image = Column(String(250), nullable=False)
                likes = relationship("Like", back_populates="post")
                comments = relationship("Comment", back_populates="post")

class Feed (Base):
                __tablename__ = 'feed'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)
                story_id = Column(Integer, ForeignKey('story.id'))
                story = relationship(Story)



class Like (Base):
                __tablename__ = 'like'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)

class Comment (Base):
                __tablename__ = 'comment'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)
                comment = Column(String(250), nullable=False)

class Followers (Base):
                __tablename__ = 'followers'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                follower_id = Column(Integer, ForeignKey('user.id'))
                follower = relationship(User)
                
class Following (Base):
                __tablename__ = 'following'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                following_id = Column(Integer, ForeignKey('user.id'))
                following = relationship(User)



class View (Base):
                __tablename__ = 'view'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_id = Column(Integer, ForeignKey('story.id'))
                story = relationship(Story)
        
class BlockedUser (Base):
                __tablename__ = 'blocked_user'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                blocked_user_id = Column(Integer, ForeignKey('user.id'))
                blocked_user = relationship(User)
        
class AccountType (Base):
                __tablename__ = 'account_type'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                type = Column(String(250), nullable=False)
        
class DirectMessage (Base):
                __tablename__ = 'direct_message'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                message = Column(String(250), nullable=False)
                image = Column(String(250), nullable=False)
                video = Column(String(250), nullable=False)
                audio = Column(String(250), nullable=False)
                recipient_id = Column(Integer, ForeignKey('user.id'))
                recipient = relationship(User)

class Recipient(Base):
                __tablename__ = 'recipient'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                direct_message_id = Column(Integer, ForeignKey('direct_message.id'))
                direct_message = relationship(DirectMessage)
    
class Hashtag(Base):
                __tablename__ = 'hashtag'
                id = Column(Integer, primary_key=True)
                name = Column(String(250), nullable=False)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)

class Location(Base):
                __tablename__ = 'location'
                id = Column(Integer, primary_key=True)
                name = Column(String(250), nullable=False)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)

class Mention(Base):
                __tablename__ = 'mention'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)

class SavedPost(Base):
                __tablename__ = 'saved_post'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                post_id = Column(Integer, ForeignKey('post.id'))
                post = relationship(Post)

class SavedStory(Base):
                __tablename__ = 'saved_story'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_id = Column(Integer, ForeignKey('story.id'))
                story = relationship(Story)

class Highlight(Base):
                __tablename__ = 'highlight'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                name = Column(String(250), nullable=False)
                stories = relationship("Story", back_populates="highlight")

class SavedHighlight(Base):
                __tablename__ = 'saved_highlight'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                highlight_id = Column(Integer, ForeignKey('highlight.id'))
                highlight = relationship(Highlight)



class StoryView(Base):
                __tablename__ = 'story_view'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_id = Column(Integer, ForeignKey('story.id'))
                story = relationship(Story)

class StoryReply(Base):
                __tablename__ = 'story_reply'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_id = Column(Integer, ForeignKey('story.id'))
                story = relationship(Story)
                reply = Column(String(250), nullable=False)

class StoryReplyView(Base):
                __tablename__ = 'story_reply_view'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_reply_id = Column(Integer, ForeignKey('story_reply.id'))
                story_reply = relationship(StoryReply)

class StoryReplyLike(Base):
                __tablename__ = 'story_reply_like'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_reply_id = Column(Integer, ForeignKey('story_reply.id'))
                story_reply = relationship(StoryReply)
    
class StoryReplyReply(Base):
                __tablename__ = 'story_reply_reply'
                id = Column(Integer, primary_key=True)
                user_id = Column(Integer, ForeignKey('user.id'))
                user = relationship(User)
                story_reply_id = Column(Integer, ForeignKey('story_reply.id'))
                story_reply = relationship(StoryReply)
                reply = Column(String(250), nullable=False)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
