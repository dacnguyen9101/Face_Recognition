# Installing Face Recognition for Python 3.8 on Windows 10 | Cmake | Dlib

Install Dlib and others libraries for Face Recognition on Windowns 10

## Getting Started
- **STEP -1:** DOWNLOAD AND INSTALL [Python 3.8](https://www.python.org/downloads/) FOR WINDOWS 10

Add Python to Windows PATH

![](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

If you missed this step, you can refer [here](https://datatofish.com/add-python-to-windows-path/).

- **STEP -2:** INSTALL [VISUAL STUDIO 2019 COMMUNITY EDITION](https://www.youtube.com/redirect?v=xaDJ5xnc8dc&redir_token=QUFFLUhqay1aQTJhNVVLRHlOdDIzMkkydzVuMEJ4bEllQXxBQ3Jtc0ttTFAwUXNady1falVPWHFIODV2MWJzYmEwZ2lRaVZudU9KYmRvTlhpTTZKZ0R2bHFIYkVlSDVPWU5UVGxma05OOVBJYWpEV2VDZEpWM19GU040LWdmY3A4Sm82ZnB1c1lac1FyenJSOGpJMTZOeGp4bw%3D%3D&event=video_description&q=https%3A%2F%2Fvisualstudio.microsoft.com%2Fdownloads%2F)

Visual Studio Window
![](https://scontent.fvca1-2.fna.fbcdn.net/v/t1.15752-9/117302472_338203170897308_607837783062883344_n.png?_nc_cat=100&_nc_sid=b96e70&_nc_ohc=N89jbfxnhkkAX_wg5Wk&_nc_ht=scontent.fvca1-2.fna&oh=555e4e5ce71f7d663436c5cb8fc9e4e2&oe=5F599C70)

- **STEP -3:** CLONE THE FACE RECOGNITION REPO

Open ***Command Propmpt***
```cmd
mkdir facerecog
```

```cmd
cd .\facerecog\
```

```cmd
git clone git://github.com/ageitgey/face_recognition
```

- **STEP -4:** CREATE A PYTHON VIRTUAL ENVIRONMENT

```cmd
pip install virtualenv
```

```cmd
virtualenv myvenvpy
```

```cmd
cd .\myvenvpy\Scripts\
```

```cmd
.\ativate
```

- **STEP -5:** RUN PYTHON SETUP.PY INSTALL
Return facerecog's directory

```cmd
cd ..
```

```cmd
cd ..
```

```cmd
cd .\face_recogition
```

```cmd 
pip install cmake
```

```cmd 
python setup.py install
```

You can type **pip freeze** to check whether dlib is insatlled or not and version of libraries which have been installed

```cmd 
pip freeze
```

![](https://scontent.fvca1-2.fna.fbcdn.net/v/t1.15752-9/117235146_3162465650458047_1889766614407790221_n.png?_nc_cat=107&_nc_sid=b96e70&_nc_ohc=C0NuaHVHO48AX-HGZNy&_nc_ht=scontent.fvca1-2.fna&oh=85d84be9774b4b21815d05e41bbfe55d&oe=5F59C782)
