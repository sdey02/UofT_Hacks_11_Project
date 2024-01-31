<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->
<h3 align="center">Photo Plotter</h3>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is what we came up for the nostolgia theme at UofT Hacks 11. The project allows users to upload a photo along with a short paragraph about what they did at that location. The photo is converted to base 64. Then using Cohere we parse the text to find the location and also generate a simple caption for the photo. The location is then passed to geopy to get the latitude and longitude which get sent a SQLAlchemy database along with the the base64 image for storage. The location data is also passed to leaflet where we create a pointer on the map that contains the photo and the cpation that was generated for that location. We also use a relational database to store a users login details.  

Contact details for the entire team, (Maxence, Hamza and me) can be found below.

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Project Demo
![Login Screen](https://private-user-images.githubusercontent.com/78007563/301278095-8fbb17c3-cf7a-49b7-b9e2-1f46bfcae767.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3Mjg1MDksIm5iZiI6MTcwNjcyODIwOSwicGF0aCI6Ii83ODAwNzU2My8zMDEyNzgwOTUtOGZiYjE3YzMtY2Y3YS00OWI3LWI5ZTItMWY0NmJmY2FlNzY3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTMxVDE5MTAwOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTlhZTY3MmRhMThkZTA0ZDk3MTgxMmJhZDU4ZmQ4ZTgwNjU0OWMyZmI0OTc2ZjNmYzg3OWIwNzI1ZGQ0MzYzN2MmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xFI3oUwofnXDb1of5fhKZLSH4CVrH10IFWdkeOT3MPY)

![Main Screen](https://private-user-images.githubusercontent.com/78007563/301277570-ca718aa8-54db-4365-9be6-6ef35ede90ce.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3MjgzODAsIm5iZiI6MTcwNjcyODA4MCwicGF0aCI6Ii83ODAwNzU2My8zMDEyNzc1NzAtY2E3MThhYTgtNTRkYi00MzY1LTliZTYtNmVmMzVlZGU5MGNlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTMxVDE5MDgwMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4OWE1ZmI2YTkyNWNmMDMzYWYzYzE3YThkY2NjYzliNjNjYmY5NWM1MTEzZjYyNDhjODZjOGQ1N2FjMGY3ZDcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.IDTSt4C7YVeAJMGmUK_00ik9KV0wx9zzhW3CJ5S9lDU)

![Main Screen](https://private-user-images.githubusercontent.com/78007563/301278273-932cb656-459a-4106-969d-b71c9735a6cd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY3Mjg1NjEsIm5iZiI6MTcwNjcyODI2MSwicGF0aCI6Ii83ODAwNzU2My8zMDEyNzgyNzMtOTMyY2I2NTYtNDU5YS00MTA2LTk2OWQtYjcxYzk3MzVhNmNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTMxVDE5MTEwMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY1YzAwNWRmNDEzMDcwNmRhMzAxMjZlNjZhZDI4ODkzNzUwYTM4ZTJiMzg3MWE5N2E5MzRiMzA4NWU0MjUzNTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0._rsOFlAlq1oty0hSKm53LKlhZZctKeN5q6jqsuhIvVc)

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Flask
* Geopy
* Cohere API
* SQLAlchemy
* ssl
* certifi
  ```sh
  pip3 install cohere
  pip3 install geopy
  pip3 isntall flask
  pip3 import ssl
  pip3 import certifi
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sdey02/Chip_8_Emulator.git
   ```

2. In app.py
   ```sh
   python3 app.py
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Plotted Memories lets you uplaod an image along with text about where you were and what you did that day. It can be used as a photo album or as a way to track all the palces you have been to.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Maxence Gilloteaux - https://www.linkedin.com/in/maxenceglt/
<br>
Shreyans Dey - https://www.linkedin.com/in/sdey02/
<br>
Hamza Zadi - https://www.linkedin.com/in/hmzzaidi/

<p align="right">(<a href="#readme-top">back to top</a>)</p>
