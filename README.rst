neattext
========

NeatText:a simple NLP package for cleaning textual data and text
preprocessing

|Build Status|

|GitHub license|

Problem
-------

-  Cleaning of unstructured text data
-  Reduce noise [special characters,stopwords]
-  Reducing repetition of using the same code for text preprocessing

Solution
--------

-  convert the already known solution for cleaning text into a reuseable
   package

Installation
------------

.. code:: bash

    pip install neattext

Usage
-----

-  The OOP Way(Object Oriented Way)

Clean Text
~~~~~~~~~~

-  Clean text by removing emails,numbers,stopwords,emojis,etc

   .. code:: python

       >>> from neattext import TextCleaner
       >>> docx = TextCleaner()
       >>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
       >>> docx.clean_text()

Remove Emails,Numbers,Phone Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> print(docx.remove_emails())
    >>> 'This is the mail  ,our WEBSITE is https://example.com 😊.'
    >>>
    >>> print(docx.remove_stopwords())
    >>> 'This mail example@gmail.com ,our WEBSITE https://example.com 😊.'
    >>>
    >>> print(docx.remove_numbers())
    >>> docx.remove_phone_numbers()

Remove Special Characters
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> docx.remove_special_characters()

Remove Emojis
~~~~~~~~~~~~~

.. code:: python

    >>> print(docx.remove_emojis())
    >>> 'This is the mail example@gmail.com ,our WEBSITE is https://example.com .'

Replace Emails,Numbers,Phone Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> docx.replace_emails()
    >>> docx.replace_numbers()
    >>> docx.replace_phone_numbers()

Chain Multiple Methods
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊 and it will cost $100 to subscribe."
    >>> docx = TextCleaner(t1)
    >>> result = docx.remove_emails().remove_urls().remove_emojis()
    >>> print(result)
    'This is the mail  ,our WEBSITE is   and it will cost $100 to subscribe.'

Using TextExtractor
-------------------

-  To Extract emails,phone numbers,numbers,urls,emojis from text

   .. code:: python

       >>> from neattext import TextExtractor
       >>> docx = TextExtractor()
       >>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
       >>> docx.extract_emails()
       >>> ['example@gmail.com']
       >>>
       >>> docx.extract_emojis()
       >>> ['😊']

Using TextMetrics
-----------------

-  To Find the Words Stats such as counts of
   vowels,consonants,stopwords,word-stats

   .. code:: python

       >>> from neattext import TextMetrics
       >>> docx = TextMetrics()
       >>> docx.text = "This is the mail example@gmail.com ,our WEBSITE is https://example.com 😊."
       >>> docx.count_vowels()
       >>> docx.count_consonants()
       >>> docx.count_stopwords()
       >>> docx.word_stats()

Usage
-----

-  The MOP(method/function oriented way) Way

.. code:: python

    >>> from neattext.functions import clean_text,extract_emails
    >>> t1 = "This is the mail example@gmail.com ,our WEBSITE is https://example.com ."
    >>> clean_text(t1,True)
    >>>'this is the mail <email> ,our website is <url> .'
    >>> extract_emails(t1)
    >>> ['example@gmail.com']

Explainer
---------

-  Explain an emoji or unicode for emoji

   -  emoji\_explainer()
   -  emojify()
   -  unicode\_2\_emoji()

.. code:: python

    >>> from neattext.explainer import emojify
    >>> emojify('Smiley')
    >>> '😃'

.. code:: python

    >>> from neattext.explainer import emoji_explainer
    >>> emoji_explainer('😃')
    >>> 'SMILING FACE WITH OPEN MOUTH'

.. code:: python

    >>> from neattext.explainer import unicode_2_emoji
    >>> unicode_2_emoji('0x1f49b')
        'FLUSHED FACE'

Documentation
-------------

Please read the
`documentation <https://github.com/Jcharis/neattext/wiki>`__ for more
information on what neattext does and how to use is for your needs.

More Features To Add
--------------------

-  basic nlp task
-  currency normalizer

Acknowledgements
~~~~~~~~~~~~~~~~

-  Inspired by packages like ``clean-text`` from Johannes Fillter and
   ``textify`` by JCharisTech

NB
~~

-  Contributions Are Welcomed
-  Notice a bug, please let us know.
-  Thanks A lot

By
~~

-  Jesse E.Agbe(JCharis)
-  Jesus Saves @JCharisTech

.. |Build Status| image:: https://travis-ci.org/Jcharis/neattext.svg?branch=master
   :target: https://travis-ci.org/Jcharis/neattext
.. |GitHub license| image:: https://img.shields.io/github/license/Jcharis/neattext
   :target: https://github.com/Jcharis/neattext/blob/master/LICENSE
