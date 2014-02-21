# coding=utf-8
"""A custom Sphinx HTML Translator for *Twitter Bootstrap* layout

.. moduleauthor:: Torbjörn Klatt <opensource@torbjoern-klatt.de>
"""
import sys
import re

from docutils import nodes
from docutils.writers.html4css1 import HTMLTranslator
from sphinx import addnodes
from sphinx.locale import admonitionlabels, l_


# add this to support sphinx.ext.todo
admonitionlabels['todo'] = l_('Todo')
admonitionlabels['example'] = l_('Example')


#: Mapping of admonition classes to Bootstrap contextual classes
alert_classes = {
    'attention': 'primary',
    'caution':   'warning',
    'danger':    'danger',
    'error':     'danger',
    'hint':      'info',
    'important': 'primary',
    'note':      'info',
    'seealso':   'info',
    'tip':       'primary',
    'warning':   'warning',
    'todo':      'info',
    'example':   'info'
}


#: Mapping of object types to signature annotations
member_types = {
    'function': 'function ',
    'method': 'method ',
    'attribute': 'attribute ',
    'staticmethod': 'static ',
    'static': 'static '
}


split_parameter_types = re.compile('\sor\s|,\s')


class BootstrapTranslator(HTMLTranslator):
    """Custom HTML Translator for a Bootstrap-ifyied Sphinx layout

    This is a specialization of the default HTML Translator of the docutils
    package.
    Only a couple of functions have been overridden to produce valid HTML to be
    directly styled with *Twitter Bootstrap*.
    """

    # overridden
    doctype = '<!DOCTYPE html>\n'

    def __init__(self, builder, *args, **kwds):
        # mostly copied from sphinx.writer.HTMLTranslator
        HTMLTranslator.__init__(self, *args, **kwds)
        self.highlighter = builder.highlighter
        self.no_smarty = 0
        self.builder = builder
        self.highlightlang = builder.config.highlight_language
        self.highlightlinenothreshold = sys.maxsize
        self.protect_literal_text = 0
        self.permalink_text = builder.config.html_add_permalinks
        # support backwards-compatible setting to a bool
        if not isinstance(self.permalink_text, basestring):
            self.permalink_text = self.permalink_text and u'\u00B6' or ''
        self.permalink_text = self.encode(self.permalink_text)
        self.secnumber_suffix = builder.config.html_secnumber_suffix
        self.param_separator = ''
        self.optional_param_level = 0
        self._table_row_index = 0
        self.field_context = []
        self.collapse_context = []
        self.collapse_id_count = 0
        self.collapse_item_count = 0
        self.first_param = 0

    # overridden
    def visit_comment(self, node, sub=re.compile('-(?=-)').sub):
        """A comment. Printed but hidden by default.
        """
        self.body.append(self.starttag(node, 'div', '', CLASS='comment hidden'))

    def depart_comment(self, node):
        self.body.append('</div>')

    def visit_compact_paragraph(self, node):
        """Must be defined for use with Sphinx.

        We are not doing anything here.
        """
        pass

    def depart_compact_paragraph(self, node):
        pass

    # overridden
    def visit_attribution(self, node):
        """Attribution line (e.g. in block quotes)

        With *Twitter Bootstrap* we are able to style a special attribution
        paragraph (read "*footer*") at the end of block quotes with the ReST
        directive ``epigraph``.

        .. admonition:: Example

            The ReST directive::

                .. epigraph::

                    This is a block quote with a footer/attribution line.

                    -- this is the attribution

            renders to:

            .. epigraph::

                This is a block quote with a footer/attribution line.

                -- this is the attribution
        """
        if isinstance(node.parent, nodes.block_quote):
            self.body.append(self.starttag(node, 'footer'))
        else:
            prefix, suffix = self.attribution_formats[self.settings.attribution]
            self.context.append(suffix)
            self.body.append(
                self.starttag(node, 'p', prefix, CLASS='attribution'))

    # overridden
    def depart_attribution(self, node):
        if isinstance(node.parent, nodes.block_quote):
            self.body.append("</footer>\n")
        else:
            self.body.append(self.context.pop() + '</p>\n')

    # overridden
    def visit_admonition(self, node, name=''):
        """Admonition panel

        A admonition is a special section within a object description which is
        rendered as a panel.
        For a list of supported admonitions, see the keys of
        :py:attr:`.alert_classes` and :py:attr:`.admonitionLabels`.

        The following note is a usage example of an admonition.

        .. note::
            This method is usually called via one of the specialized wrappers:

            * :py:meth:`.visit_note`
            * :py:meth:`.visit_attention`
            * :py:meth:`.visit_warning`
            * :py:meth:`.visit_danger`
            * :py:meth:`.visit_error`
            * :py:meth:`.visit_seealso`
            * :py:meth:`.visit_example`
            * :py:meth:`.visit_todo_node`

        :param str name: type of the admonition as in the keys of
            :py:attr:`.alert_classes`.
        """
        if isinstance(node[0], nodes.title):
            if node[0].astext() in ['Example', 'Examples']:
                del node['classes']
                del node[0]
                self.context.append('example')
                name = 'example'
            elif node[0].astext() in ['Note', 'Notes']:
                del node['classes']
                del node[0]
                self.context.append('note')
                name = 'note'
        if name:
            self.body.append(
                self.starttag(node, 'div',
                              CLASS=('accordion-group panel '
                                     'panel-%s' % alert_classes[name])))
            self.section_level += 1
            self.body.append(
                '<div class="accordion-heading panel-heading">'
                '<h%d class="panel-title">%s</h%d></div>\n' %
                (self.section_level, admonitionlabels[name], self.section_level)
            )
            self.section_level -= 1
            self.body.append(self.starttag(node, 'div',
                                           CLASS='accordion-inner panel-body'))
        else:
            self.body.append(
                self.starttag(node, 'div',
                              CLASS='accordion-group panel panel-default'))

    # overridden
    def depart_admonition(self, node=None, name=''):
        if name:
            # closing off the additional div.panel-body
            self.body.append('</div>\n')
        elif self.context[-1] in alert_classes.keys():
            self.body.append('</div>\n')
            self.context.pop()
        self.body.append('</div>\n')

    def visit_note(self, node):
        self.visit_admonition(node, 'note')

    def depart_note(self, node):
        self.depart_admonition(node, 'note')

    def visit_attention(self, node):
        self.visit_admonition(node, 'attention')

    def depart_attention(self, node):
        self.depart_admonition(node, 'attention')

    def visit_warning(self, node):
        self.visit_admonition(node, 'warning')

    def depart_warning(self, node):
        self.depart_admonition(node, 'warning')

    def visit_danger(self, node):
        self.visit_admonition(node, 'danger')

    def depart_danger(self, node):
        self.depart_admonition(node, 'danger')

    def visit_error(self, node):
        self.visit_admonition(node, 'error')

    def depart_error(self, node):
        self.depart_admonition(node, 'error')

    def visit_seealso(self, node):
        self.visit_admonition(node, 'seealso')

    def depart_seealso(self, node):
        self.depart_admonition(node, 'seealso')

    def visit_example(self, node):
        self.visit_admonition(node, 'example')

    def depart_example(self, node):
        self.depart_admonition(node, 'example')

    def visit_todo_node(self, node):
        node.remove(node[0])  # remove additional 'Todo' title node
        self.visit_admonition(node, 'todo')

    def depart_todo_node(self, node):
        self.depart_admonition(node, 'todo')

    def visit_index(self, node):
        pass

    def depart_index(self, node):
        pass

    # overridden
    def visit_bullet_list(self, node):
        atts = {}
        old_compact_simple = self.compact_simple
        self.context.append((self.compact_simple, self.compact_p))
        self.compact_p = None
        self.compact_simple = self.is_compactable(node)
        if self.compact_simple and not old_compact_simple:
            atts['class'] = ' simple'
        self.body.append(self.starttag(node, 'ul', **atts))

    # overridden
    def visit_list_item(self, node):
        self.body.append(self.starttag(node, 'li', '',))
        if len(node):
            node[0]['classes'].append('first')

    # overridden
    def visit_definition_list(self, node):
        """Bootstrap-ified Definition List

        .. admonition:: Example

        The ReST definition list::

            Key One
                Is the first

            Second Key
                Is the second

        is rendered to:

        Key One
            Is the first

        Second Key
            Is the second
        """
        self.body.append(self.starttag(node, 'dl', CLASS='dl-horizontal'))

    # overridden
    def visit_field_list(self, node):
        self.body.append(
            self.starttag(node, 'div',
                          CLASS='accordion panel-group field-list'))

    # overridden
    def depart_field_list(self, node):
        self.body.append('</div>\n')

    def _fixup_return_type(self, node):
        if node[0].astext() == 'Returns':
            _this_index = node.parent.index(node)

            if len(node.parent.children) > _this_index + 1:
                if node.parent[_this_index + 1][0].astext() == 'Return type':
                    _rtype = node.parent[_this_index + 1]
                    _rtype_new = [nodes.Text(' (')]
                    if isinstance(_rtype[1][0], nodes.paragraph):
                        for elem in _rtype[1][0]:
                            _rtype_new.append(elem.deepcopy())
                    _rtype_new.append(nodes.Text(')'))
                    _strongs = node.traverse(condition=nodes.strong)

                    if len(_strongs) > 0:
                        _return_name = _strongs[0]
                        _return_para = _return_name.parent
                        _first_strong_id_in_its_parent = \
                            _return_para.index(_strongs[0])
                        _return_para.insert(_first_strong_id_in_its_parent + 1,
                                            _rtype_new)

                        if isinstance(_return_para, nodes.paragraph) \
                                and isinstance(_return_para.parent,
                                               nodes.paragraph):
                            _return_para_parent = _return_para.parent
                            if len(_return_para_parent) > 1 \
                                    and isinstance(_return_para_parent[1],
                                                   (nodes.bullet_list,
                                                    nodes.definition_list,
                                                    nodes.field_list)):
                                _para = []
                                for _p in _return_para_parent[0]:
                                    _para.append(_p.deepcopy())
                                _list = _return_para_parent[1].deepcopy()
                                _return_para_parent.clear()
                                _return_para_parent.extend(_para)
                                _return_para_parent.append(_list)

    # overridden
    def visit_field(self, node):
        if node[0][0].astext() == 'Return type':
            # return type should be handled by _fixup_return_type
            #  on 'Returns' nodes
            raise nodes.SkipNode

        _contextual_class = 'default'
        self._fixup_return_type(node)
        _field_name_title = node[0][0].astext()
        if _field_name_title == 'Raises':
            _contextual_class = 'warning'
        if node[0][0].astext() in ['Raises']:
            if node[0].__len__() == 3:
                node[1][0].insert(0, nodes.Text(' -- '))
                node[1][0].insert(0, nodes.strong(text=node[0][2].astext()))
                del node[0][2]
                del node[0][1]
        self.field_context.append(_field_name_title)
        self.body.append(
            self.starttag(node, 'div',
                          CLASS=('accordion-goup panel '
                                 'panel-%s field' % _contextual_class)))
        self.section_level += 1

    # overridden
    def depart_field(self, node):
        self.field_context.pop()
        self.section_level -= 1
        self.body.append('</div>')

    # overridden
    def visit_field_name(self, node):
        self.body.append(
            self.starttag(node, 'div', '',
                          CLASS='accordion-heading panel-heading field-name'))
        self.body.append('<h%d class="panel-title">' % self.section_level)

    # overridden
    def depart_field_name(self, node):
        self.body.append('</h%d></div>' % self.section_level)

    # overridden
    def visit_field_body(self, node):
        self.body.append(
            self.starttag(node, 'div', '',
                          CLASS='accordion-inner panel-body field-body'))
        if self.field_context[-1] in ['Parameters', 'Raises', 'Returns']:
            self._print_parameters(node)

    # overridden
    def depart_field_body(self, node):
        self.body.append('</div>')

    # overridden
    def visit_table(self, node):
        self.context.append(self.compact_p)
        self.compact_p = True
        classes = ' '.join(['table', self.settings.table_style]).strip()
        self.body.append(
            self.starttag(node, 'table', CLASS=classes))

    # overridden
    def depart_table(self, node):
        self.compact_p = self.context.pop()
        self.body.append('</table>\n')

    def visit_desc(self, node):
        if node['objtype'] in member_types.keys() \
                and node['objtype'] != 'staticmethod':
            node[0].insert(0,
                           addnodes
                           .desc_annotation(text=member_types[node['objtype']]))
        self.body.append(
            self.starttag(node, 'div',
                          CLASS=('accordion-group panel panel-default '
                                 '%s' % node['objtype'])))
        if node['objtype'] in ['class']:
            self.collapse_context.append([node['objtype'],
                                          '%s-id%d' % (node['objtype'],
                                                       self.collapse_id_count)])
            self.collapse_id_count += 1
        if len(self.collapse_context) > 0 \
                and node['objtype'] in member_types.keys():
            self.collapse_context[-1]\
                .append('%s-id%d' % (node['objtype'], self.collapse_item_count))
            self.collapse_item_count += 1
        self.section_level += 1

    def depart_desc(self, node):
        self.section_level -= 1
        if node['objtype'] in ['class']:
            self.collapse_context.pop()
        if len(self.collapse_context) > 0 \
                and node['objtype'] in member_types.keys():
            self.collapse_context[-1].pop()
        self.body.append('</div>')

    def visit_desc_signature(self, node):
        self.body.append(
            self.starttag(node, 'div',
                          CLASS=('accordion-heading panel-heading '
                                 'desc-signature')))
        self.body.append('<h%d class="panel-title">' % self.section_level)
        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 3:
            self.body.append(
                '<a data-toggle="collapse" '
                'data-parent="#%s" ' % self.collapse_context[-1][1] +
                'href="#%s">' % self.collapse_context[-1][2])

    def depart_desc_signature(self, node):
        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 3:
            self.body.append('</a>')
        self.body.append('</h%d></div>' % self.section_level)

    def visit_desc_name(self, node):
        self.body.append(self.starttag(node, 'tt', '', CLASS='desc-name'))

    def depart_desc_name(self, node):
        self.body.append('</tt>')

    def visit_desc_addname(self, node):
        self.body.append(
            self.starttag(node, 'tt', '', CLASS='desc-addname'))
        self.body.append('<span class="text-muted muted">')

    def depart_desc_addname(self, node):
        self.body.append('</span></tt>')

    def visit_desc_parameterlist(self, node):
        """The list of parameters in a method signature.
        Including the enclosing brackets.
        """
        self.body.append(
            self.starttag(node, 'tt', '', CLASS='desc-parameterlist'))
        self.body.append('<big>(</big>')
        self.first_param = 1
        self.optional_param_level = 0
        # How many required parameters are left.
        self.required_params_left = sum([isinstance(c, addnodes.desc_parameter)
                                         for c in node.children])
        self.param_separator = node.child_text_separator

    def depart_desc_parameterlist(self, node):
        self.body.append('<big>)</big>')
        self.body.append('</tt>')

    def visit_desc_parameter(self, node):
        """A single parameter in a method signature
        """
        self.body.append(
            self.starttag(node, 'span', '', CLASS='desc-parameter'))
        if self.first_param:
            self.first_param = 0
        elif not self.required_params_left:
            self.body.append(self.param_separator)
        if self.optional_param_level == 0:
            self.required_params_left -= 1
        if not node.hasattr('noemph'):
            self.body.append('<em>')

    def depart_desc_parameter(self, node):
        if not node.hasattr('noemph'):
            self.body.append('</em>')
        if self.required_params_left:
            self.body.append(self.param_separator)
        self.body.append('</span>')

    def visit_desc_optional(self, node):
        """Optional parameters in a method signature.
        """
        self.body.append(self.starttag(node, 'span', '', CLASS='desc-optional'))
        self.optional_param_level += 1
        self.body.append('[')

    def depart_desc_optional(self, node):
        self.optional_param_level -= 1
        self.body.append(']</span>')

    def visit_desc_returns(self, node):
        self.body.append(self.starttag(node, 'tt', '', CLASS='desc-returns'))

    def depart_desc_returns(self, node):
        self.body.append('</tt>')

    def visit_desc_content(self, node):
        """The content of a class, method or attribute.
        """
        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 2:
            self.body.append(
                '<div class="accordion panel-group" '
                'id="%s">' % self.collapse_context[-1][1])
            self.collapse_id_count += 1

        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 3:
            self.body.append(
                '<div id="%s"' % self.collapse_context[-1][2] +
                ' class="accordion-body panel-collapse collapse">')
        self.body.append(
            self.starttag(node, 'div',
                          CLASS='accordion-inner panel-body desc-content'))

    def depart_desc_content(self, node):
        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 2:
            self.body.append('</div>')

        if len(self.collapse_context) > 0 \
                and self.collapse_context[-1][0] in ['class'] \
                and len(self.collapse_context[-1]) == 3:
            self.body.append('</div>')
        self.body.append('</div>')

    def visit_desc_annotation(self, node):
        """Annotations in object signatures.

        This is either the ``class``, ``method`` or ``attribute`` identifier or
        the value of module or class attributes.
        """
        self.body.append(
            self.starttag(node, 'tt', '',
                          CLASS='desc-annotation text-muted muted'))

    def depart_desc_annotation(self, node):
        self.body.append('</tt>')

    def visit_toctree(self, node):
        self.body.append(self.starttag(node, 'span', CLASS='toctree'))

    def depart_toctree(self, node):
        self.body.append('</span>')

    # the following four methods are taken from
    #  http://stackoverflow.com/a/15562804
    def visit_displaymath(self, node):
        import sphinx.ext.mathjax
        sphinx.ext.mathjax.html_visit_displaymath(self, node)

    def depart_displaymath(self, node):
        return

    # overridden
    def visit_math(self, node):
        import sphinx.ext.mathjax
        sphinx.ext.mathjax.html_visit_math(self, node)

    # overridden
    def depart_math(self, node):
        return

    # overridden
    def unknown_visit(self, node):
        raise NotImplementedError('Unknown node: %s' % node.__class__.__name__)

    def _print_parameters(self, node):
        self.body.append('<table class="table table-condensed">'
                         '<colgroup>'
                         '<col class="col-parameter-name"></col>'
                         '<col class="col-parameter-type"></col>'
                         '<col class="col-parameter-desc"></col>'
                         '</colgroup>'
                         '<tbody>')

        if isinstance(node.children[0], nodes.paragraph):
            if self.field_context[-1] in ['Raises']:
                if len(node.children) > 1:
                    if isinstance(node[1], nodes.bullet_list):
                        node[0].append(node[1].deepcopy())
                        node.remove(node[1])

            self._print_single_parameter(node[0])
        elif isinstance(node.children[0], nodes.bullet_list):
            first = True
            for _c in node.children[0]:
                self._print_single_parameter(_c[0], first=first)
                if first:
                    first = False
        self.body.append('</tbody></table>')
        node.clear()

    def _print_single_parameter(self, node, first=False):
        _do_name = True
        _name = None
        _do_type = False
        _types = []
        _do_desc = False
        _desc = []
        for _c in node.children:
            if _do_desc:
                _desc.append(_c)

            elif _do_name and node.children.index(_c) == 0 \
                    and isinstance(_c, (nodes.strong, nodes.literal)):
                _name = _c[0].astext()
                _do_name = False

            elif isinstance(_c, nodes.Text):
                if _do_type is False and _c.astext() == ' (':
                    _do_type = True
                if _c.astext() == ')':
                    _c.replace(')', '', 1)
                    _do_type = False
                if _c.astext() in [' -- ', ' --'] \
                        or _c.astext().find(' --') != -1:
                    if len(_c.astext().replace(' --', '', 1).lstrip()) > 0:
                        _desc.append(
                            nodes.Text(
                                _c.astext().replace(' --', '', 1).lstrip()))
                    _do_desc = True
                if ' of ' in _c.astext() and _do_type:
                    _types.append(_c)

            elif isinstance(_c, (nodes.emphasis, nodes.literal,
                                 nodes.reference)) \
                    and _do_type:
                if isinstance(_c, (nodes.emphasis, nodes.literal)):
                    _types.append(_c[0])
                else:
                    _types.append(_c)

        _cls = 'parameter-name'
        if first:
            _cls += ' first-parameter'
        self.body.append(
            '<tr>'
            '<td>'
            '<div class="%s"><strong>%s</strong></div>' % (_cls, _name))
        _cls = 'parameter-type'
        if first:
            _cls += ' first-parameter'
        self.body.append('</td>'
                         '<td>'
                         '<div class="%s">' % _cls)
        _of_type = False
        for _ti in range(0, len(_types)):
            if _types[_ti].astext() == ' of ':
                self.body.append(_types[_ti].astext())
                _of_type = True
            else:
                if len(_types) > 1 and _ti > 0 and not _of_type:
                    self.body.append(', ')
                if _of_type:
                    _of_type = False
                self.body.append('<code>')
                if isinstance(_types[_ti], nodes.reference):
                    if isinstance(_types[_ti][0], nodes.literal):
                        _type = nodes.Text(_types[_ti][0].astext())
                        _types[_ti].clear()
                        _types[_ti].append(_type)
                    _types[_ti].walkabout(self)
                else:
                    self.body.append(_types[_ti].astext())
                self.body.append('</code>')

        _cls = 'parameter-desc'
        if first:
            _cls += ' first-parameter'
        self.body.append('</div></td>'
                         '<td>'
                         '<div class="%s">' % _cls)

        for _desc_elem in _desc:
            _desc_elem.walkabout(self)
        self.body.append('</div>'
                         '</td>'
                         '</tr>')
