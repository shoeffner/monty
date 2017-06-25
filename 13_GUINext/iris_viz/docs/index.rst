Welcome to Castle Crashers Princess Edition's documentation!
============================================================

This is a simple example file. For your project documentation, you just need to
change this text. Keep everything below (and including) :code:`..toctree::`.

If you want to get fancy, take a look at how `reStructuredText (ReST)`_ works in
the `Sphinx documentation`_.

However, for your final project we only expect you to enter some brief
explanations about what your project is supposed to do, how to start it and how
to use it, like this:

.. code-block:: ReST
   :linenos:

   Ultimate Guide to Princess' World Domination
   ============================================

   In a world, where princesses and knights fight bravely over the crown,
   dragons might ruin the party.

   This game is packed with intense battles between *princesses* and *knights*.
   Choose your character and fight! But beware: There might be **dragons**!


   Running the game
   ----------------

   To run the game, simply run :code:`python main.py` in the :code:`src` dir.
   Select a princess or a knight by typing :code:`p` or :code:`k`. Then use
   :code:`s` and :code:`w` for strong and weak attacks, respectively. Fight
   through your opponents until you conquer the crown!

   .. toctree::
      :maxdepth: 2

      modules/modules

You do not need to document your functions or modules here, just use
`google style`_ doc comments, `napoleon`_, an extension to sphinx, should pick
it up automatically. You can find some examples on how to write them in the
`examples section`_.

To build the documentation, just run :code:`make html` in the :code:`docs`
directory. However, make sure to change the :code:`conf.py`! You need to change
the title and author there:

.. literalinclude:: conf.py
   :linenos:
   :lineno-start: 27
   :lines: 27-30

Additionally, you might have to delete the directory :code:`docs/modules` when
you changed some of your source files – especially once you deleted the example
files!

To view the documentation in all its glory, navigate to
:code:`docs/_build/html`, run :code:`python -m http.server 8080` and open your
browser. You can find it at `http://localhost:8080`_. To stop the server again,
hit :code:`CTRL+C`.

.. _reStructuredText (ReST): http://docutils.sourceforge.net/rst.html
.. _Sphinx documentation: http://www.sphinx-doc.org/en/stable/rest.html
.. _google style: https://google.github.io/styleguide/pyguide.html#Comments
.. _napoleon: http://www.sphinx-doc.org/en/stable/ext/napoleon.html
.. _examples section: http://www.sphinx-doc.org/en/stable/ext/example_google.html
.. _http://localhost:8080: http://localhost:8080

.. toctree::
   :maxdepth: 2

   modules/modules

