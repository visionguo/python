# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

class Config(object):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://noc:nocpasswd@10.16.208.178/noc?charset=utf8"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config.from_object(Config)
db = SQLAlchemy(app)


class Permission:
    WRITE = 1
    ADMIN = 2



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.WRITE, True],
            'Administrator': [Permission.WRITE | Permission.ADMIN, False],
        }
        for r in roles:
            try:
                role = Role.query.filter_by(name=r).first()
                #role = db.session.query(Role).filter_by(name=r).first()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()

            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            try:
                db.session.add(role)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()

    def __repr__(self):
        return '<Role %r>' % self.name



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r,Role id %r>' %(self.name, self.role_id)



def Administrator(user_id):
    try:
        admin = User.query.filter(User.user_id == user_id).first()
        #admin = db.session.query(User).filter(User.user_id == user_id).first()
        if admin.role.name == "Administrator":
            return True
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    return False



def user_id_exists(user_id):
    try:
        re = User.query.filter(User.user_id == user_id).first()
        #re = db.session.query(User).filter(User.user_id == user_id).first()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if re is None:
        return False
    return True


class NocNoc(db.Model):
    __tablename__ = 'noc'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(100))
    priority_id = db.Column(db.Integer)
    status = db.Column(db.String(100))
    responsible_dept = db.Column(db.Integer)
    responsible_team = db.Column(db.Integer)
    noc_reason = db.Column(db.Integer)
    direct_reason_id = db.Column(db.Integer)
    desc = db.Column(db.String(2048))
    detail = db.Column(db.Text())
    analysis = db.Column(db.Text())
    found_time = db.Column(db.DateTime())
    start_time = db.Column(db.DateTime())
    fixed_time = db.Column(db.DateTime())
    noc_time = db.Column(db.DateTime(), default=datetime.datetime.now)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class NocAffected(db.Model):
    __tablename__ = 'noc_affected_team'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nid = db.Column(db.Integer, nullable=False)
    affected_dept = db.Column(db.Integer, nullable=False)
    affected_team = db.Column(db.Integer, nullable=False)
    affected_customer_type = db.Column(db.Integer, nullable=False)
    affected_scope = db.Column(db.String(100), nullable=False)
    affected_money = db.Column(db.String(100), nullable=False)
    detail = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class NocImprovement(db.Model):
    __tablename__ = 'noc_improvement'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    improve_dept = db.Column(db.String(100), nullable=False)
    improve_team = db.Column(db.String(100), nullable=False)
    assignee = db.Column(db.String(100), nullable=False)
    completion_time = db.Column(db.DateTime(), default=datetime.datetime.now)
    jira_link = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class NocPriority(db.Model):
    __tablename__ = 'noc_priority'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    upgrade_interval = db.Column(db.Integer)
    notify_interval = db.Column(db.Integer)

class NocReasons(db.Model):
    __tablename__ = 'noc_reasons'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    treecode = db.Column(db.String(10), nullable=False)
    parent_id = db.Column(db.Integer, nullable=False, default=0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}




