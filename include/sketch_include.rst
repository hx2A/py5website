* `Py5Font <py5font/>`_: PFont is the font class for Processing.
* `Py5Graphics <py5graphics/>`_: Main graphics and rendering context, as well as the base API implementation for processing "core".
* `Py5Image <py5image/>`_: Datatype for storing images.
* `Py5Shader <py5shader/>`_: This class encapsulates a GLSL shader program, including a vertex and a fragment shader.
* `Py5Shape <py5shape/>`_: Datatype for storing shapes.
* `Py5Surface <py5surface/>`_: new template no description.
* `acos() <acos/>`_: new template no description.
* `alpha() <alpha/>`_: Extracts the alpha value from a color.
* `ambient() <ambient/>`_: Sets the ambient reflectance for shapes drawn to the screen.
* `ambient_light() <ambient_light/>`_: Adds an ambient light.
* `apply_filter() <apply_filter/>`_: Filters the display window using a preset filter or with a custom shader.
* `apply_matrix() <apply_matrix/>`_: Multiplies the current matrix by the one specified through the parameters.
* `arc() <arc/>`_: Draws an arc to the screen.
* `args <args/>`_: new template no description.
* `asin() <asin/>`_: new template no description.
* `atan() <atan/>`_: new template no description.
* `atan2() <atan2/>`_: new template no description.
* `background() <background/>`_: The ``background()`` function sets the color used for the background of the Processing window.
* `begin_camera() <begin_camera/>`_: The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space.
* `begin_contour() <begin_contour/>`_: Use the ``begin_contour()`` and ``end_contour()`` function to create negative shapes within shapes such as the center of the letter 'O'.
* `begin_raw() <begin_raw/>`_: To create vectors from 3D data, use the ``begin_raw()`` and ``end_raw()`` commands.
* `begin_record() <begin_record/>`_: Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window.
* `begin_shape() <begin_shape/>`_: Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more complex forms.
* `bezier() <bezier/>`_: Draws a Bezier curve on the screen.
* `bezier_detail() <bezier_detail/>`_: Sets the resolution at which Beziers display.
* `bezier_point() <bezier_point/>`_: Evaluates the Bezier at point t for points a, b, c, d.
* `bezier_tangent() <bezier_tangent/>`_: Calculates the tangent of a point on a Bezier curve.
* `bezier_vertex() <bezier_vertex/>`_: Specifies vertex coordinates for Bezier curves.
* `bezier_vertices() <bezier_vertices/>`_: new template no description.
* `blend() <blend/>`_: Blends a region of pixels from one image into another (or in itself again) with full alpha channel support.
* `blend_mode() <blend_mode/>`_: Blends the pixels in the display window according to a defined mode.
* `blue() <blue/>`_: Extracts the blue value from a color, scaled to match current ``color_mode()``.
* `box() <box/>`_: A box is an extruded rectangle.
* `brightness() <brightness/>`_: Extracts the brightness value from a color.
* `camera() <camera/>`_: Sets the position of the camera through setting the eye position, the center of the scene, and which axis is facing upward.
* `ceil() <ceil/>`_: new template no description.
* `circle() <circle/>`_: Draws a circle to the screen.
* `clear() <clear/>`_: Clears the pixels within a buffer.
* `clip() <clip/>`_: Limits the rendering to the boundaries of a rectangle defined by the parameters.
* `color() <color/>`_: Creates colors for storing in variables of the ``color`` datatype.
* `color_mode() <color_mode/>`_: Changes the way Processing interprets color data.
* `constrain() <constrain/>`_: new template no description.
* `convert_image() <convert_image/>`_: new template no description.
* `copy() <copy/>`_: Copies a region of pixels from the display window to another area of the display window and copies a region of pixels from an image used as the ``src_img`` parameter into the display window.
* `cos() <cos/>`_: new template no description.
* `create_font() <create_font/>`_: Dynamically converts a font to the format used by Processing from a .ttf or .otf file inside the sketch's "data" folder or a font that's installed elsewhere on the computer.
* `create_graphics() <create_graphics/>`_: Creates and returns a new ``Py5Graphics`` object.
* `create_image() <create_image/>`_: Creates a new PImage (the datatype for storing images).
* `create_image_from_numpy() <create_image_from_numpy/>`_: new template no description.
* `create_shape() <create_shape/>`_: The ``create_shape()`` function is used to define a new shape.
* `cursor() <cursor/>`_: Sets the cursor to a predefined symbol or an image, or makes it visible if already hidden.
* `curve() <curve/>`_: Draws a curved line on the screen.
* `curve_detail() <curve_detail/>`_: Sets the resolution at which curves display.
* `curve_point() <curve_point/>`_: Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``.
* `curve_tangent() <curve_tangent/>`_: Calculates the tangent of a point on a curve.
* `curve_tightness() <curve_tightness/>`_: Modifies the quality of forms created with ``curve()`` and ``curve_vertex()``.
* `curve_vertex() <curve_vertex/>`_: Specifies vertex coordinates for curves.
* `curve_vertices() <curve_vertices/>`_: new template no description.
* `day() <day/>`_: Processing communicates with the clock on your computer.
* `degrees() <degrees/>`_: new template no description.
* `directional_light() <directional_light/>`_: Adds a directional light.
* `display_density() <display_density/>`_: This function returns the number "2" if the screen is a high-density screen (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if not.
* `display_height <display_height/>`_: System variable that stores the height of the entire screen display.
* `display_width <display_width/>`_: System variable that stores the width of the entire screen display.
* `dist() <dist/>`_: new template no description.
* `ellipse() <ellipse/>`_: Draws an ellipse (oval) to the screen.
* `ellipse_mode() <ellipse_mode/>`_: Modifies the location from which ellipses are drawn by changing the way in which parameters given to ``ellipse()`` are intepreted.
* `emissive() <emissive/>`_: Sets the emissive color of the material used for drawing shapes drawn to the screen.
* `end_camera() <end_camera/>`_: The ``begin_camera()`` and ``end_camera()`` functions enable advanced customization of the camera space.
* `end_contour() <end_contour/>`_: Use the ``begin_contour()`` and ``end_contour()`` function to create negative shapes within shapes such as the center of the letter 'O'.
* `end_raw() <end_raw/>`_: Complement to ``begin_raw()``; they must always be used together.
* `end_record() <end_record/>`_: Stops the recording process started by ``begin_record()`` and closes the file.
* `end_shape() <end_shape/>`_: The ``end_shape()`` function is the companion to ``begin_shape()`` and may only be called after ``begin_shape()``.
* `exit_sketch() <exit_sketch/>`_: new template no description.
* `exp() <exp/>`_: new template no description.
* `fill() <fill/>`_: Sets the color used to fill shapes.
* `finished <finished/>`_: new template no description.
* `floor() <floor/>`_: new template no description.
* `focused <focused/>`_: Confirms if a Processing program is "focused," meaning that it is active and will accept mouse or keyboard input.
* `frame_count <frame_count/>`_: The system variable ``frame_count`` contains the number of frames that have been displayed since the program started.
* `frame_rate() <frame_rate/>`_: Specifies the number of frames to be displayed every second.
* `frustum() <frustum/>`_: Sets a perspective matrix as defined by the parameters.
* `full_screen() <full_screen/>`_: This function is new for Processing 3.0.
* `get() <get/>`_: Reads the color of any pixel or grabs a section of an image.
* `get_frame_rate() <get_frame_rate/>`_: new template no description.
* `get_graphics() <get_graphics/>`_: new template no description.
* `get_matrix() <get_matrix/>`_: new template no description.
* `get_surface() <get_surface/>`_: new template no description.
* `green() <green/>`_: Extracts the green value from a color, scaled to match current ``color_mode()``.
* `has_thread() <has_thread/>`_: new template no description.
* `height <height/>`_: System variable that stores the height of the display window.
* `hint() <hint/>`_: This function is used to enable or disable special features that control how graphics are drawn.
* `hot_reload_draw() <hot_reload_draw/>`_: new template no description.
* `hour() <hour/>`_: Processing communicates with the clock on your computer.
* `hue() <hue/>`_: Extracts the hue value from a color.
* `image() <image/>`_: The ``image()`` function draws an image to the display window.
* `image_mode() <image_mode/>`_: Modifies the location from which images are drawn by changing the way in which parameters given to ``image()`` are intepreted.
* `is_dead <is_dead/>`_: new template no description.
* `is_dead_from_error <is_dead_from_error/>`_: new template no description.
* `is_key_pressed() <is_key_pressed/>`_: new template no description.
* `is_mouse_pressed() <is_mouse_pressed/>`_: new template no description.
* `is_ready <is_ready/>`_: new template no description.
* `is_running <is_running/>`_: new template no description.
* `java_platform <java_platform/>`_: new template no description.
* `java_version <java_version/>`_: new template no description.
* `java_version_name <java_version_name/>`_: new template no description.
* `key <key/>`_: The system variable ``key`` always contains the value of the most recent key on the keyboard that was used (either pressed or released).
* `key_code <key_code/>`_: The variable ``key_code`` is used to detect special keys such as the arrow keys (UP, DOWN, LEFT, and RIGHT) as well as ALT, CONTROL, and SHIFT.
* `launch_promise_thread() <launch_promise_thread/>`_: new template no description.
* `launch_repeating_thread() <launch_repeating_thread/>`_: new template no description.
* `launch_thread() <launch_thread/>`_: new template no description.
* `lerp() <lerp/>`_: new template no description.
* `lerp_color() <lerp_color/>`_: Calculates a color between two colors at a specific increment.
* `light_falloff() <light_falloff/>`_: Sets the falloff rates for point lights, spot lights, and ambient lights.
* `light_specular() <light_specular/>`_: Sets the specular color for lights.
* `lights() <lights/>`_: Sets the default ambient light, directional light, falloff, and specular values.
* `line() <line/>`_: Draws a line (a direct path between two points) to the screen.
* `lines() <lines/>`_: new template no description.
* `list_threads() <list_threads/>`_: new template no description.
* `load_font() <load_font/>`_: Loads a .vlw formatted font into a ``Py5Font`` object.
* `load_image() <load_image/>`_: new template no description.
* `load_json() <load_json/>`_: new template no description.
* `load_np_pixels() <load_np_pixels/>`_: new template no description.
* `load_pixels() <load_pixels/>`_: Loads the pixel data of the current display window into the ``pixels[]`` array.
* `load_shader() <load_shader/>`_: Loads a shader into the PShader object.
* `load_shape() <load_shape/>`_: Loads geometry into a variable of type ``Py5Shape``.
* `log() <log/>`_: new template no description.
* `loop() <loop/>`_: By default, Processing loops through ``draw()`` continuously, executing the code within it.
* `mag() <mag/>`_: new template no description.
* `millis() <millis/>`_: Returns the number of milliseconds (thousandths of a second) since starting the program.
* `minute() <minute/>`_: Processing communicates with the clock on your computer.
* `model_x() <model_x/>`_: Returns the three-dimensional X, Y, Z position in model space.
* `model_y() <model_y/>`_: Returns the three-dimensional X, Y, Z position in model space.
* `model_z() <model_z/>`_: Returns the three-dimensional X, Y, Z position in model space.
* `month() <month/>`_: Processing communicates with the clock on your computer.
* `mouse_button <mouse_button/>`_: When a mouse button is pressed, the value of the system variable ``mouse_button`` is set to either ``LEFT``, ``RIGHT``, or ``CENTER``, depending on which button is pressed.
* `mouse_x <mouse_x/>`_: The system variable ``mouse_x`` always contains the current horizontal coordinate of the mouse.
* `mouse_y <mouse_y/>`_: The system variable ``mouse_y`` always contains the current vertical coordinate of the mouse.
* `no_clip() <no_clip/>`_: Disables the clipping previously started by the ``clip()`` function.
* `no_cursor() <no_cursor/>`_: Hides the cursor from view.
* `no_fill() <no_fill/>`_: Disables filling geometry.
* `no_lights() <no_lights/>`_: Disable all lighting.
* `no_loop() <no_loop/>`_: Stops Processing from continuously executing the code within ``draw()``.
* `no_smooth() <no_smooth/>`_: Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.
* `no_stroke() <no_stroke/>`_: Disables drawing the stroke (outline).
* `no_texture() <no_texture/>`_: new template no description.
* `no_tint() <no_tint/>`_: Removes the current fill value for displaying images and reverts to displaying images with their original hues.
* `noise() <noise/>`_: new template no description.
* `noise_detail() <noise_detail/>`_: new template no description.
* `noise_mode() <noise_mode/>`_: new template no description.
* `noise_seed() <noise_seed/>`_: new template no description.
* `norm() <norm/>`_: new template no description.
* `normal() <normal/>`_: Sets the current normal vector.
* `np_pixels <np_pixels/>`_: new template no description.
* `ortho() <ortho/>`_: Sets an orthographic projection and defines a parallel clipping volume.
* `parse_json() <parse_json/>`_: new template no description.
* `pause() <pause/>`_: new template no description.
* `perspective() <perspective/>`_: Sets a perspective projection applying foreshortening, making distant objects appear smaller than closer ones.
* `pixel_density() <pixel_density/>`_: This function is new with Processing 3.0.
* `pixel_height <pixel_height/>`_: When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OS X or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled.
* `pixel_width <pixel_width/>`_: When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OS X or high-dpi on Windows and Linux), the width and height of the sketch do not change, but the number of pixels is doubled.
* `pixels[] <pixels/>`_: The ``pixels[]`` array contains the values for all the pixels in the display window.
* `pmouse_x <pmouse_x/>`_: The system variable ``pmouse_x`` always contains the horizontal position of the mouse in the frame previous to the current frame.
* `pmouse_y <pmouse_y/>`_: The system variable ``pmouse_y`` always contains the vertical position of the mouse in the frame previous to the current frame.
* `point() <point/>`_: Draws a point, a coordinate in space at the dimension of one pixel.
* `point_light() <point_light/>`_: Adds a point light.
* `points() <points/>`_: new template no description.
* `pop() <pop/>`_: The ``pop()`` function restores the previous drawing style settings and transformations after ``push()`` has changed them.
* `pop_matrix() <pop_matrix/>`_: Pops the current transformation matrix off the matrix stack.
* `pop_style() <pop_style/>`_: The ``push_style()`` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together.
* `print_camera() <print_camera/>`_: Prints the current camera matrix to the Console (the text window at the bottom of Processing).
* `print_line_profiler_stats() <print_line_profiler_stats/>`_: new template no description.
* `print_matrix() <print_matrix/>`_: Prints the current matrix to the Console (the text window at the bottom of Processing).
* `print_projection() <print_projection/>`_: Prints the current projection matrix to the Console (the text window at the bottom of Processing).
* `profile_draw() <profile_draw/>`_: new template no description.
* `profile_functions() <profile_functions/>`_: new template no description.
* `push() <push/>`_: The ``push()`` function saves the current drawing style settings and transformations, while ``pop()`` restores these settings.
* `push_matrix() <push_matrix/>`_: Pushes the current transformation matrix onto the matrix stack.
* `push_style() <push_style/>`_: The ``push_style()`` function saves the current style settings and ``pop_style()`` restores the prior settings.
* `quad() <quad/>`_: A quad is a quadrilateral, a four sided polygon.
* `quadratic_vertex() <quadratic_vertex/>`_: Specifies vertex coordinates for quadratic Bezier curves.
* `quadratic_vertices() <quadratic_vertices/>`_: new template no description.
* `radians() <radians/>`_: new template no description.
* `random() <random/>`_: new template no description.
* `random_gaussian() <random_gaussian/>`_: new template no description.
* `random_seed() <random_seed/>`_: new template no description.
* `rect() <rect/>`_: Draws a rectangle to the screen.
* `rect_mode() <rect_mode/>`_: Modifies the location from which rectangles are drawn by changing the way in which parameters given to ``rect()`` are intepreted.
* `red() <red/>`_: Extracts the red value from a color, scaled to match current ``color_mode()``.
* `redraw() <redraw/>`_: Executes the code within ``draw()`` one time.
* `remap() <remap/>`_: new template no description.
* `request_image() <request_image/>`_: new template no description.
* `reset_matrix() <reset_matrix/>`_: Replaces the current matrix with the identity matrix.
* `reset_shader() <reset_shader/>`_: Restores the default shaders.
* `resume() <resume/>`_: new template no description.
* `rotate() <rotate/>`_: Rotates the amount specified by the ``angle`` parameter.
* `rotate_x() <rotate_x/>`_: Rotates around the x-axis the amount specified by the ``angle`` parameter.
* `rotate_y() <rotate_y/>`_: Rotates around the y-axis the amount specified by the ``angle`` parameter.
* `rotate_z() <rotate_z/>`_: Rotates around the z-axis the amount specified by the ``angle`` parameter.
* `run_sketch() <run_sketch/>`_: new template no description.
* `saturation() <saturation/>`_: Extracts the saturation value from a color.
* `save() <save/>`_: new template no description.
* `save_frame() <save_frame/>`_: new template no description.
* `save_json() <save_json/>`_: new template no description.
* `scale() <scale/>`_: Increases or decreases the size of a shape by expanding and contracting vertices.
* `screen_x() <screen_x/>`_: Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.
* `screen_y() <screen_y/>`_: Takes a three-dimensional X, Y, Z position and returns the Y value for where it will appear on a (two-dimensional) screen.
* `screen_z() <screen_z/>`_: Takes a three-dimensional X, Y, Z position and returns the Z value for where it will appear on a (two-dimensional) screen.
* `second() <second/>`_: Processing communicates with the clock on your computer.
* `set_matrix() <set_matrix/>`_: new template no description.
* `set_np_pixels() <set_np_pixels/>`_: new template no description.
* `shader() <shader/>`_: Applies the shader specified by the parameters.
* `shape() <shape/>`_: Draws shapes to the display window.
* `shape_mode() <shape_mode/>`_: Modifies the location from which shapes draw.
* `shear_x() <shear_x/>`_: Shears a shape around the x-axis the amount specified by the ``angle`` parameter.
* `shear_y() <shear_y/>`_: Shears a shape around the y-axis the amount specified by the ``angle`` parameter.
* `shininess() <shininess/>`_: Sets the amount of gloss in the surface of shapes.
* `sin() <sin/>`_: new template no description.
* `size() <size/>`_: Defines the dimension of the display window width and height in units of pixels.
* `sketch_path() <sketch_path/>`_: new template no description.
* `smooth() <smooth/>`_: Draws all geometry with smooth (anti-aliased) edges.
* `specular() <specular/>`_: Sets the specular color of the materials used for shapes drawn to the screen, which sets the color of highlights.
* `sphere() <sphere/>`_: A sphere is a hollow ball made from tessellated triangles.
* `sphere_detail() <sphere_detail/>`_: Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh.
* `spot_light() <spot_light/>`_: Adds a spot light.
* `sq() <sq/>`_: new template no description.
* `sqrt() <sqrt/>`_: new template no description.
* `square() <square/>`_: Draws a square to the screen.
* `start() <start/>`_: new template no description.
* `stop() <stop/>`_: new template no description.
* `stop_all_threads() <stop_all_threads/>`_: new template no description.
* `stop_thread() <stop_thread/>`_: new template no description.
* `stroke() <stroke/>`_: Sets the color used to draw lines and borders around shapes.
* `stroke_cap() <stroke_cap/>`_: Sets the style for rendering line endings.
* `stroke_join() <stroke_join/>`_: Sets the style of the joints which connect line segments.
* `stroke_weight() <stroke_weight/>`_: Sets the width of the stroke used for lines, points, and the border around shapes.
* `tan() <tan/>`_: new template no description.
* `text() <text/>`_: Draws text to the screen.
* `text_align() <text_align/>`_: Sets the current alignment for drawing text.
* `text_ascent() <text_ascent/>`_: Returns ascent of the current font at its current size.
* `text_descent() <text_descent/>`_: Returns descent of the current font at its current size.
* `text_font() <text_font/>`_: Sets the current font that will be drawn with the ``text()`` function.
* `text_leading() <text_leading/>`_: Sets the spacing between lines of text in units of pixels.
* `text_mode() <text_mode/>`_: Sets the way text draws to the screen, either as texture maps or as vector geometry.
* `text_size() <text_size/>`_: Sets the current font size.
* `text_width() <text_width/>`_: Calculates and returns the width of any character or text string.
* `texture() <texture/>`_: Sets a texture to be applied to vertex points.
* `texture_mode() <texture_mode/>`_: Sets the coordinate space for texture mapping.
* `texture_wrap() <texture_wrap/>`_: Defines if textures repeat or draw once within a texture map.
* `tint() <tint/>`_: Sets the fill value for displaying images.
* `translate() <translate/>`_: Specifies an amount to displace objects within the display window.
* `triangle() <triangle/>`_: A triangle is a plane created by connecting three points.
* `update_np_pixels() <update_np_pixels/>`_: new template no description.
* `update_pixels() <update_pixels/>`_: Updates the display window with the data in the ``pixels[]`` array.
* `vertex() <vertex/>`_: All shapes are constructed by connecting a series of vertices.
* `vertices() <vertices/>`_: new template no description.
* `width <width/>`_: System variable that stores the width of the display window.
* `year() <year/>`_: Processing communicates with the clock on your computer.
