import os
from webob.dec import wsgify
from webob.static import DirectoryApp
from webob.exc import HTTPFound
from webdispatch import URLDispatcher,MethodDispatcher
from wsgiref.simple_server import make_server

from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from docutils.core import publish_parts
from jinja2 import Environment
from jinja2.loaders import PackageLoader

here = os.path.dirname(__file__)
env = Environment(loader=PackageLoader(__name__, 'templates'))

DBSession = orm.scoped_session(orm.sessionmaker())

Base = declarative_base()

def init_db(engine):
    DBSession.configure(bind=engine)
    Base.metadata.create_all(bind=DBSession.bind)
    try:
       front_page = Page(page_name='FrontPage', contents="""\
FrontPage
====================""")
       DBSession.add(front_page)
       DBSession.commit()
    except IntegrityError:
       DBSession.remove()



class Page(Base):
    __tablename__ = 'pages'
    id = sa.Column(sa.Integer, primary_key=True)
    page_name = sa.Column(sa.Unicode(255), unique=True)
    contents = sa.Column(sa.UnicodeText)
    created = sa.Column(sa.DateTime, default=datetime.now)
    edited = sa.Column(sa.DateTime, onupdate=datetime.now)

    @property
    def html_contents(self):
        parts = publish_parts(source=self.contents, writer_name="html")
        return parts['html_body']

@wsgify.middleware
def sqla_transaction(req, app):
    try:
       res = req.get_response(app)
       DBSession.commit()
       return res
    finally:
       DBSession.remove()

@wsgify
def page_view(request):
    page_name = request.urlvars['page_name']
    edit_url = request.environ['webdispatch.urlgenerator'].generate('page_edit', page_name=page_name)
    try:
        page = DBSession.query(Page).filter(Page.page_name==page_name).one()
        tmpl = env.get_template('page.html')
        return tmpl.render(page=page, edit_url=edit_url)
    except NoResultFound:
        return HTTPFound(location=edit_url)

@wsgify
def page_edit_form(request):
    page_name = request.urlvars['page_name']
    try:
        page = DBSession.query(Page).filter(Page.page_name==page_name).one()
    except NoResultFound:
        page = Page(page_name=page_name, contents="")

    tmpl = env.get_template('page_edit.html')
    return tmpl.render(page=page)

@wsgify
def page_update(request):
    page_name = request.urlvars['page_name']
    try:
        page = DBSession.query(Page).filter(Page.page_name==page_name).one()
    except NoResultFound:
        page = Page(page_name=page_name, contents="")
        DBSession.add(page)

    page.contents = request.params['contents']
    location = request.environ['webdispatch.urlgenerator'].generate('page', page_name=page_name)
    return HTTPFound(location=location)

page_edit = MethodDispatcher()
page_edit.register_app('get', page_edit_form)
page_edit.register_app('post', page_update)

def make_app():
    application = URLDispatcher()
    js_app = DirectoryApp(os.path.join(here, 'static/js'))
    css_app = DirectoryApp(os.path.join(here, 'static/css'))
    img_app = DirectoryApp(os.path.join(here, 'static/img'))

    application.add_url('js', '/js/*', js_app)
    application.add_url('css', '/css/*', css_app)
    application.add_url('img', '/img/*', img_app)
    application.add_url('page', '/{page_name}', page_view)
    application.add_url('page_edit', '/{page_name}/edit', page_edit)
    application.add_url('top', '/', HTTPFound(location='FrontPage'))
    return application

def main():
    engine = sa.create_engine('sqlite:///{dir}/wiki.db'.format(dir=os.getcwd()))
    engine.echo = True
    init_db(engine)
    application = make_app()

    application = sqla_transaction(application)
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
