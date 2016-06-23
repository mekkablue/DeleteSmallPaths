# encoding: utf-8

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


from GlyphsApp.plugins import *

class DeleteSmallPaths(FilterWithDialog):

	# Definitions of IBOutlets
	
	# The NSView object from the User Interface. Keep this here!
	dialog = objc.IBOutlet()

	# Text field in dialog
	maximumSizeField = objc.IBOutlet()
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Delete Small Paths',
			'de': u'Kleine Pfade löschen'
		})
		
		self.actionButtonLabel = Glyphs.localize({
			'en': u'Delete',
			'de': u'Löschen'
		})

		# Load dialog from .nib (without .extension)
		self.loadNib('IBdialog', __file__)

	# On dialog show
	def start(self):

		# Set default setting if not present
		if not Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea']:
			Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'] = 400.0

		# Set maxArea of text field
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
	def filter(self, layer, inEditView, customParameters):
		try:
			# Called on font export, get maxArea from customParameters
			maxArea = customParameters['smallerthan']
		except:
			# Called through UI, use stored maxArea
			maxArea = float(Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'])

		# delete paths below threshold:
		for pathIndex in range(len(layer.paths))[::-1]:
			if layer.paths[pathIndex].area() < maxArea:
				del layer.paths[pathIndex]
	
	def generateCustomParameter( self ):
		return "%s; smallerthan:%s;" % (self.__class__.__name__, Glyphs.defaults['com.mekkablue.DeleteSmallPaths.maxArea'] )
