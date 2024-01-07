# spriters_resource_icon_generator
Takes a folder of spritesheets and generates an icon using the first image in the top-left, then resizes it to the 148 x 125 px size needed for Spriter's Resource icons.

# Explanation
I had a large batch of spritesheets that I wanted to upload to Spriter's Resource, and I wanted an easy way to create icons for them without having to do each one by hand. This script is a quick and easy way to take the first non-transparent object it finds (it searches from the top left), crop just that single object into its own individual image, and then resizes the canvas to the 148 x 125 icon size required by Spriter's Resource. 

# Requirements
* Ability to run a python script (Python must be downloaded, etc.)
* Must have Pillow library installed.
  * ```pip install pillow```

