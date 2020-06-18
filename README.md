# Ensemble-IDS-multi-attack
This is our final year engineering project titled "Ensemble Based Intrusion Detection System". In this project we have tried to detect multi attacks using ensemble approaches of Machine Learning.

In multi attack environment, there would be more than one attack occurring simultaneously or within a short span of time. In our project, we have considered all those attacks as multi attacks which occur within one second of time span. We have proposed a system that captures live packets from the network and classifies whether the packet is normal or belongs to one of the subclasses of attack using various ensemble approaches such as Bagging, Boosting and Stacking. The highest accuracy we got is using XGBoost of 72.27%.

NSL-KDD dataset has been used for both training and testing the model. KDDExtractor from (https://github.com/AI-IDS/kdd99_feature_extractor).



# Installation required:
a) Python3 libraries:
1. Scapy 
2. Tkinter
3. Pickle
4. Other libraries as per the classifier

b) KDD-extractor


Steps for Installation of scapy:
1. sudo apt-get update -y
2. sudo apt-get install -y scapy

Steps for Installation of Tkinter:
sudo apt-get install python-tk

Steps for Installation of Pickle:
Installed by default in python3

Steps for Installation of Other libraries as per the classifier:
You can use pip3 command or use online compilers like colab but prefer installing them since you require them for using pickle file generated on the system.


Steps for Installation of KDD-extractor:
Download KDDExtractor from (https://github.com/AI-IDS/kdd99_feature_extractor).

#To install cmake
sudo apt-get install cmake

#To build kdd99_feature_extractor
sudo apt-get install libpcap0.8-dev
cd kdd99_feature_extractor-master
cmake CMakeLists.txt 
make
sudo make
cd src
sudo make
sudo ./kdd99extractor 
press ctrl c to stop.
cd ../..
