```
   _____    _________________ .___.___                                              
  /  _  \  /   _____\_   ___ \|   |   |                                             
 /  /_\  \ \_____  \/    \  \/|   |   |                                             
/    |    \/        \     \___|   |   |                                             
\____|__  /_______  /\______  |___|___|                                             
        \/        \/        \/                                                      
   _____          __    ________                                   __               
  /  _  \________/  |_ /  _____/  ____   ____   ________________ _/  |_ ___________ 
 /  /_\  \_  __ \   __/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __/  _ \_  __ \
/    |    |  | \/|  | \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  |(  <_> |  | \/
\____|__  |__|   |__|  \______  /\___  |___|  /\___  |__|  (____  |__| \____/|__|   
        \/                    \/     \/     \/     \/           \/                  
                                                                
```               

### 👩🏻‍💻 A simple, lightweight and blazingly fast ASCII Art Generator that converts images into text-based artwork using ASCII characters. A fun and creative way to visualize images with code!

This is a CLI program. Requires Python and PiP.

## 📦 Libraries 

### [1. Pillow 11.3.0 - Python Imaging Library](https://pillow.readthedocs.io/en/stable/)

The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.

Check python support for Pillow to check compatibility of Pillow with your system. https://pillow.readthedocs.io/en/stable/installation/platform-support.html

## 📄 Installation Intructions -

Make sure you have - 

- python
- pip
- jdk

Follow these instruction to install and run it on your machine!

1. Install all required packages in requirements.txt
~~~
> pip install <packageName>
~~~
2. Run the main python script
~~~
> python main.py
~~~ 

![Galaxy](image.png)

## ⚙ Configuration

### 1. Image config -

Inside the [main.py](https://github.com/prathmesh-ka-github/ASCII-ArtGenerator/blob/main/main.py), edit Image.open() function. It takes the image path as the file parameter in String.
~~~
image = Image.open("<imagePath.extension>")
~~~
You can input .png, .jpg, .jpeg, .tiff, .svg, .bmp and .webp image formats.

### 2. Resolution config -

### 3. ASCII characters config -

## 📝 License
This project is licensed under the MIT License.

Checkout [LICENSE.md](https://github.com/prathmesh-ka-github/ASCII-ArtGenerator/blob/main/LICENSE) for more info.

## 🤝🏻 Contribute
1. Fork this repository.
1. Create your own branch.
1. Commit changes.
1. Submit a pull request.

your code will be reviewed and request will be merged!

## 💛 Appreciation
Give this repo a star! Submit issues if you find bugs! 