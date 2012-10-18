from pyjon.reports import ReportTemplate
from pyjon.reports import ReportFactory

import sys

testdata = [range(10)] * 100

def render_template(factory, template, title):
    
    factory.render_template(template_file=template,
                            title=title,
                            data=testdata,
                            truc="bidule")

if __name__ == '__main__':
    factory = ReportFactory()
    args = sys.argv
    if len(sys.argv)>1:
        render_template(factory, sys.argv[1], sys.argv[2])
        factory.render_document(sys.argv[2])
    else:    
        render_template(factory, 'test1.xml', "doc 1")
        print "doc 1 done"
        render_template(factory, 'test1.xml', "doc 2")
        print "doc 2 done"
        render_template(factory, 'test1.xml', "doc 3")
        print "doc 3 done"
        factory.render_document("test.pdf")
        print "file done"
