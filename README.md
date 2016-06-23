# DeleteSmallPaths.glyphsFilter

*Filter > Delete Small Paths* is a plugin for the [Glyphs font editor](http://glyphsapp.com/). It deletes all paths smaller than a threshold value in square units. It can be useful for cleaning up glyphs from vector debris.

![Paths smaller than the provided threshold value disappear.](DeleteSmallPaths.png "Delete Small Paths")

### Installation

#### Easy Installation in Glyphs 2.3+

Go to *Window > Plugin Manager*, look for *Delete Small Paths*, and click the *Install* button next to it, then restart Glyphs.

#### Manual Installation

1. Download the complete ZIP file and unpack it, or clone the repository.
2. Double click the .glyphsFilter file. Confirm the dialog that appears in Glyphs.
3. Restart Glyphs
4. You can set a keyboard shortcut in System Preferences.

### Usage Instructions

1. Open a glyph in Edit View, or select any number of glyphs in Font or Edit View.
2. Use *Filter > Delete Small Paths* to bring up the dialog and enter a threshold value.

Alternatively, you can also use it as a custom parameter in an instance:

	Property: Filter
	Value: DeleteSmallPaths; smallerthan:<threshold>;

If you do not feel like typing it, you can click the *Copy Parameter* button, which puts the custom parameter with the current dialog settings in the clipboard. You can then paste it into an instance parameter field.

### Requirements

The plugin needs Glyphs 2.3 or higher, running on OS X 10.9 or later.

### License

Copyright 2014 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
