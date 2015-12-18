import unittest
import webtest

class WikiAppTests(unittest.TestCase):
    def setUp(self):
        import sqlalchemy as sa
        from . import make_app, init_db, DBSession

        DBSession.remove()
        engine = sa.create_engine('sqlite:///')
        init_db(engine)
        app = make_app()
        self.app = webtest.TestApp(app)
        self.session = DBSession

    def tearDown(self):
        self.session.rollback()

    def test_page(self):
        from . import Page

        test_page = Page(page_name='TestPage', contents='this-is-test')
        self.session.add(test_page)
        res = self.app.get('/TestPage')
        self.assertIn('this-is-test', res)

    def test_no_page(self):
        res = self.app.get('/TestNoPage')
        self.assertEqual(res.status_int, 302)
        self.assertEqual(res.location, 'http://localhost:80/TestNoPage/edit')

    def test_new_page(self):
        from . import Page

        res = self.app.get('/TestNewPage/edit')
        res.form['contents'] = 'create new page'
        res.form.submit()

        page = self.session.query(Page).filter(Page.page_name=='TestNewPage').one()
        self.assertEqual(page.contents, 'create new page')

    def test_update_page(self):
        from . import Page

        test_page = Page(page_name='TestUpdatePage', contents='old contents')
        self.session.add(test_page)

        res = self.app.get('/TestUpdatePage/edit')
        res.form['contents'] = 'updated contents'
        res.form.submit()

        page = self.session.query(Page).filter(Page.page_name=='TestUpdatePage').one()
        self.assertEqual(page.contents, 'updated contents')
