#!/bin/bash

# Descargar e instalar Google Chrome
curl -o google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb

# Limpiar archivos de instalación
rm google-chrome-stable_current_amd64.deb