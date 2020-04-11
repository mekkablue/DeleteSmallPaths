# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	Filter with dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20with%20Dialog
#
#	For help on the use of Interface Builder:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class DeleteSmallPaths(FilterWithDialog):

	# Definitions of IBOutlets
	dialog = objc.IBOutlet()
	maximumSizeField = objc.IBOutlet()

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Delete Small Paths',
			'es': u'Borrar trazados pequeños',
			'de': u'Kleine Pfade löschen',
			'fr': u'Supprimer les petits tracés'
		})
		
		self.actionButtonLabel = Glyphs.localize({
			'en': u'Delete',
			'es': u'Borrar',
			'de': u'Löschen',
			'fr': u'Supprimer'
		})
		
		# Load dialog from .nib (without .extension)
		self.loadNib('IBdialog', __file__)

	# On dialog show
	@objc.python_method
	def start(self):
		# Set default setting if not present
		Glyphs.registerDefault('com.mekkablue.DeleteSmallPaths.maxArea', 400.0)
		# Set value of text field
		self.maximumSizeField.setStringValue_(Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'])
		# Set focus to text field
		self.maximumSizeField.becomeFirstResponder()
		
	# Action triggered by UI
	@objc.IBAction
	def setMaxArea_( self, sender ):
		# Store maxArea coming in from dialog
		Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'] = sender.floatValue()
		# Trigger redraw
		self.update()

	# Actual filter
	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		if inEditView:
			# Called through UI, use stored maxArea
			maxArea = float(Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'])
		else:
			# Called on font export, get maxArea from customParameters
			try:
				maxArea = customParameters['smallerthan']
			except:
				maxArea = 400.0 # fallback if user didn’t specify anything

		# delete paths below threshold:
		for pathIndex in range(len(layer.paths))[::-1]:
			if layer.paths[pathIndex].area() < maxArea:
				del layer.paths[pathIndex]

	@objc.python_method
	def generateCustomParameter( self ):
		return "%s; smallerthan:%s;" % (
			self.__class__.__name__,
			Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea']
		)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
