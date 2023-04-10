CLIMV is a command line interface media viewer, it will convert your video of choice to ASCII and play it onto the terminal.

CLIMV uses OpenCV in the convert_frame_to_ascii method to convert the frames to grayscale, resizing them to fit the terminal size, then mapping the pixel intensities to characters in the character set.
The video is then rendered using the convert_frame_to_ascii method iteratively in the render_video method for the amount of frames in the video, then appending to a buffer to be returned once fully rendered.
The display_video method iterates through each ASCII frame and prints it to the terminal while clearing the screen to create the illusion of animation. A time delay is also introduced to attempt to synchronize the video playback with the sound.
In the driver code, it converts the video to audio and saves it to a temporary file stored in your Downloads directory, it then uses threading to call display_video and the sound function, a function that simply plays the converted video's sound. 
