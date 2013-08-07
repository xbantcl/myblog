#coding=utf8

#flask-admin

from flask.ext.admin import Admin,expose
from flask.ext import admin, login, wtf
from flask.ext.admin.contrib import sqlamodel
from flask.ext.admin.contrib.sqlamodel import ModelView
from myapp import app
from data import (db, Category, Tag, Article, Comment, User,\
                    Link, BlackList, Subscriber)

#add  flask-superadmin
#from flask.ext import wtf
#from flask.ext.superadmin import Admin, model
#from flask.ext.superadmin.contrib.sqlamodel import ModelView
#add by 
# 参考
# https://flask-admin.readthedocs.org/en/latest/quickstart/#authentication
#add 添加登录界面
#Define login  forms (for flask-login)
class LoginForm(wtf.Form):
    login = wtf.TextField(validators=[wtf.required()])
    password = wtf.PasswordField(validators=[wtf.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise wtf.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


#####
# 
#def init_login(self):
#	login_manager = login.LoginManager()
 #   login_manager.set_up(app)
     # Create user loader function
  #  @login_manager.user_loader
   # def load_user(id):
    #    	return db.session.query(User).get(id)
# is_accessible 返回 False 
# 即可防止外人登录

#add by wang



class MyModelView(ModelView):#ModelView
   #add
   # @expose('/index/')
    #def index(self):
     #   return self.render('index.html')
	def is_accessible(self):
		    #init_login()
		    #return login.current_user.is_authenticated)
            return True
    # add 


admin = Admin(app, url='/blog/admin_daniel')
# add by wang


admin.add_view(MyModelView(Category, db.session))
admin.add_view(MyModelView(Tag, db.session))
admin.add_view(MyModelView(Article, db.session))
admin.add_view(MyModelView(Comment, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Link, db.session))
admin.add_view(MyModelView(BlackList, db.session))
admin.add_view(MyModelView(Subscriber, db.session))
