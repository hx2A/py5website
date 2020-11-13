* `apply_filter() <../py5image_apply_filter/>`_: Filters the image as defined by one of the following modes:

THRESHOLD
Converts the image to black and white pixels depending if they are above or below the threshold defined by the level parameter. The parameter must be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

GRAY
Converts any colors in the image to grayscale equivalents. No parameter is used.

OPAQUE
Sets the alpha channel to entirely opaque. No parameter is used.

INVERT
Sets each pixel to its inverse value. No parameter is used.

POSTERIZE
Limits each channel of the image to the number of colors specified as the parameter. The parameter can be set to values between 2 and 255, but results are most noticeable in the lower ranges.

BLUR
Executes a Gaussian blur with the level parameter specifying the extent of the blurring. If no parameter is used, the blur is equivalent to Gaussian blur of radius 1. Larger values increase the blur.

ERODE
Reduces the light areas. No parameter is used.

DILATE
Increases the light areas. No parameter is used.
* `blend() <../py5image_blend/>`_: Blends a region of pixels into the image specified by the ``img`` parameter.
* `copy() <../py5image_copy/>`_: Copies a region of pixels from one image into another.
* `get() <../py5image_get/>`_: Reads the color of any pixel or grabs a section of an image.
* `height <../py5image_height/>`_: The height of the image in units of pixels.
* `load_pixels() <../py5image_load_pixels/>`_: Loads the pixel data for the image into its ``pixels[]`` array.
* `mask() <../py5image_mask/>`_: Masks part of an image from displaying by loading another image and using it as an alpha channel.
* `pixels[] <../py5image_pixels/>`_: The pixels[] array contains the values for all the pixels in the image.
* `update_pixels() <../py5image_update_pixels/>`_: Updates the image with the data in its ``pixels[]`` array.
* `width <../py5image_width/>`_: The width of the image in units of pixels.
