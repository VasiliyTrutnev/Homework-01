class Tag(object):
    def get_html(self):
        pass


class Image(Tag):
    def get_html(self):
        print('<img>')


class Input(Tag):
    def get_html(self):
        print('<input></input>')


class Text(Tag):
    def get_html(self):
        print('<p></p>')

class Link(Tag):
    def get_html(self):
        print('<a></a>')


class TF(object):
    def create_tag(self, name):
        pass

class TagFactory(TF):
    def create_tag(self, name):
        if name == 'Image':
            return Image()
        if name == 'Input':
            return Input()
        if name == 'Text':
            return Text()
        if name == 'Link':
            return Link()



if __name__ == '__main__':
    factory = TagFactory()
    elements = ['Image', 'Input', 'Text', 'Link']
    for el in elements:
        print(factory.create_tag(el).get_html())

