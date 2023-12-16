# -*- coding: utf-8 -*-
# This file is part of the NEAT Project suite of libraries
from typing import List,Tuple,Callable


class TextPipeline:
	"""
    Pipeline of functions for cleaning text.
    Sequentially apply a list of functions to a given text.
    
    Parameters
    ----------
    steps : list of functions
        List of neattext functions or any functions
    Attributes
    ----------
    named_steps : :
        Dictionary-like object, with the following attributes.
        Read-only attribute to access any step parameter by user given name.
        Keys are step names and values are steps parameters.

    Usage
    -----
    >>> from neattext.pipeline import TextPipeline
    >>> import neattext.functions as nfx
    >>> p = TextPipeline(steps=[nfx.remove_emails,nfx.remove_puncts])
    >>> p.steps
    >>> mytext = "your text here"
    >>> p.transform(mytext)
    >>> 
    >>> p.named_steps


    """
	def __init__(self,steps: List[Callable] = None):
		self.steps = steps 
		
		

	def __repr__(self):
		return 'TextPipeline(steps={})'.format(self.steps)

	def __str__(self):
		return 'TextPipeline(steps={})'.format(self.steps)


	def fit(self,text):
		"""Fit the pipeline to the given text
		This applies all the functions to the text
		"""
		for fxn in self.steps:
			text = fxn(text)

		return text 
		 
	def transform(self,text):
		"""Transform the given text using the pipeline
		This applies all the functions to the text
		"""
		for fxn in self.steps:
			text = fxn(text)

		return text  


	@property
	def named_steps(self):
		"""Access the steps by name.
		        Read-only attribute to access any step by given name.
		        Keys are steps names and values are the steps objects.
		 """

		# convert steps to dictionary
		named_steps_as_dict = {"step_{}".format(k):v.__name__ for k,v in enumerate(self.steps)}
		return named_steps_as_dict




