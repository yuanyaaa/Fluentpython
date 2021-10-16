def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ' '.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ' '

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# name = 'p', content = (), cls = None, attrs = {}
str_ = tag('br')
print(str_)

# name = 'p', content = {tuple:1}('hello'), cls = None, attrs = {}
str_ = tag('p', 'hello')
print(str_)

# name = 'p', content = {tuple:2}('hello', 'world'), cls = None, attrs = {}
str_ = tag('p', 'hello', 'world')
print(str_)

# name = 'p', content = {tuple:1}('hello'), cls = None, attrs = {dict:1}{'id':33}
str_ = tag('p', 'hello', id=33)
print(str_)

# name = 'p', content = {tuple:2}('hello', 'world'), cls = 'sidebar', attrs = {}
str_ = tag('p', 'hello', 'world', cls='sidebar')
print(str_)

# name = 'img', content = (), cls = None, attrs = {'content': 'testing'}
str_ = tag(content='testing', name="img")
print(str_)

# name = 'img', content = (), cls = 'framed', attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
str_ = tag(**my_tag)
print(str_)
