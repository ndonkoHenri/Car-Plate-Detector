# Car Plate Detector
This is a Computer Vision Program made to detect Car-Plates in an image, Video or in real-time(ex: Webcam)!
Very Interesting right? :)

## The Algorithm || How it works?  
You might ask yourself how precisely does this great tool work...?
An Algorithm is the simplest and understandable way to represent a program.

*Have a look o_o:*

 - It receives an image, video or real-time Capture(ex: Webcam);
- Using the OpenCV python library and a HaarCascade file, it scans through the given objects(image or webcam), searching
  for one thing ~ Car Plates;
 - When detected, it then returns the position in the actual frame;
 - A bounding box is then drawn around this detected Car Plate and a text("Plate") is written above it.
   ![webcam](https://user-images.githubusercontent.com/98978078/154958272-09eef7c9-4971-4d93-b262-2dd5743061ef.png)


## Why use this Program amongst all out there?

Being completely sincere, I will tell you some reasons for you to use this program...

- Two Programs available to avoid confusion: One made only for Images and the other for Real-Time Captures;
  ![programs](https://user-images.githubusercontent.com/98978078/154950670-b24e2341-a307-4521-ad00-4e5ea82208fb.png)

- Concerning the Program only for images `CarPlatesDetectorImages.py`:
    - Several Images(of any image format) could be inputted at ones just by adding their different paths in
      the `all_images` list variable;
      ![paths](https://user-images.githubusercontent.com/98978078/154949651-5ed7251a-eebc-4662-8cb9-3fb54084c5fa.png)

    - When executed, two distinct sections are seen, one for the Original Images and beneath it images showing only the
      Plates(Zoomed/Cropped);

  ![plates](https://user-images.githubusercontent.com/98978078/154949619-0154ea29-9030-4700-bf62-f1ab322e2e44.png)

- Trackbars made available, for extreme Precision;
 
 ![trackbars](https://user-images.githubusercontent.com/98978078/154949507-c5c85173-8120-4171-839b-4347669db128.png)
 - Our Formatting and Syntax respect the Python code styling rules;
 - Comments all over the programs, to ease understanding of the code;
 - Try it out to find more interesting features(ex: speed) and let me know...



>              I(ndonkoHenri) say: *Thank You for using my Programs!! :-)*


