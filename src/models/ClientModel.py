from . import db
import datetime
from marshmallow import fields, Schema

class ClientModel(db.Model):
  """
  Client Model
  """

  __tablename__ = 'clients'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  fone = db.Column(db.Integer, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.name = data.get('name')
    self.fone = data.get('fone')
    self.owner_id = data.get('owner_id')
    self.created_at = datetime.datetime.now()
    self.modified_at = datetime.datetime.now()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_blogposts():
    return ClientModel.query.all()
  
  @staticmethod
  def get_one_blogpost(id):
    return ClientModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class ClientSchema(Schema):
  """
  Client Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  fone = fields.Str(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)