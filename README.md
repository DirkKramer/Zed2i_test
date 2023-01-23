# Zed2i_test
Zed 2i Camera tests


-	Installeer de SDK van https://www.stereolabs.com/developers/release/   (je hebt CUDA 11.1 -> 11.7 nodig)
-	Run het volgende script 'get_python_api.py'
-	Run 'stereolabs_camera.py' om te kijken of alles werkt.

sidenotes:
- De huidige instellingen in het script zijn de instellingen voor de hoogst mogelijke 'depth' kwaliteit. Sommige parameters zoals 'VIDEO_SETTINGS.EXPOSURE' kunnen naar  wens aangepast worden.
- de 'grab_frame' functie geeft twee arrays terug met shape (1080,1920,3) in respectievelijk rgb,xyz.

