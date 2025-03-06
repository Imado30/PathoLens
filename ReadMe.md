# Medical Imaging Diagnostic Aid Platform

A full-stack web application that supports medical diagnoses through AI-powered image analysis. The platform enables doctors to view MRI images, visualize AI predictions, and enhance their diagnoses by incorporating external feedback (AI models) using annotations and interactive tools. The application provides a user-friendly interface to assist doctors in the precise and efficient diagnosis of complex medical pathologies.


---

## Features

- **User Registration and Login**: Authentication and individual user accounts.
- **Medical Image Visualization**: Support for the NIFTI format using the `niivue` javascript-library.
- ** Admin-pannel feature: - all diagnosis are exportable and assigning specific datasets to each doctor is possible **
- **AI Prediction Overlays**: Display AI model outputs on (edited) medical images.
- **Image Annotation**: Easy annotations using free-hand-drawing, rectangles, or optional AI-masks for marking multiple lesions.
- **Data Management**: Store annotations, user data and diagnostic information.
- **Time Tracking**: tracks time of every action for further analysis.
- **Randomized Experiment Workflow**: Minimize bias through randomized dataset presentation.
- **Session Continuation**: Progress is preserved upon logout.

---

## Technologies  

### Frontend  
- HTML  
- CSS  
- JavaScript (`niivue` for image rendering)  

### Backend  
- Python  
- Django  

### Database  
- MySQL lite

### Deployment
- Docker

---

## Installation  

### Prerequisites
- Git: `sudo apt install git`
- Docker and Docker Compose  
- A modern web browser  
- Python
- Pip

### Setup
- Docker-Command: 

Once your server is running, open your web browser and navigate to your application's local address. The application is set to automatically reload whenever you modify any of the source files.

### Authors  
- **Torge Rau** 
- **Lukas Baumeister**
- **Christoph Mauel**
- **Snehpreet Kaur Dhinsa**
- **Imene Benamer Belkacem Zadoud**
- **Imad Azizi**
- **Rafik Farhane**
 


