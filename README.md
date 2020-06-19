# Ensemble-IDS-multi-attack
This is our final year engineering project titled **Ensemble Based Intrusion Detection System for Multi attack Environment**. In this project we have tried to detect multi attacks using ensemble approaches of Machine Learning.

In multi attack environment, there would be more than one attack occurring simultaneously or within a short span of time. In our project, we have considered all those attacks as multi attacks which occur within one second of time span. We have proposed a system that captures live packets from the network and classifies whether the packet is normal or belongs to one of the subclasses of attack using various ensemble approaches such as Bagging, Boosting and Stacking. The highest accuracy we got is using XGBoost of 72.27%.

NSL-KDD dataset has been used for both training and testing the model. KDDExtractor from [GitHub KDDExtractor](https://github.com/AI-IDS/kdd99_feature_extractor).


### Installations ###

#### Installation required: ####

* Python3 libraries:
	- Scapy 
	- Tkinter
	- Pickle
	- Other libraries as per the classifier

* KDD-extractor


#### Steps for Installation of scapy: ####
	sudo apt-get update -y
	sudo apt-get install -y scapy


#### Steps for Installation of Tkinter: ####
	sudo apt-get install python-tk


#### Steps for Installation of Pickle: ####
Installed by default in python3


#### Steps for Installation of other libraries as per the classifier: ####
You can use pip3 command or use online compilers like colab but prefer installing them since you require them for using pickle file generated on the system.


#### Steps for Installation of KDD-extractor: ####
First download KDDExtractor from [GitHub KDDExtractor](https://github.com/AI-IDS/kdd99_feature_extractor).


#### To install cmake ####
	sudo apt-get install cmake


#### To build kdd99_feature_extractor ####
	sudo apt-get install libpcap0.8-dev
Then,
1. cd kdd99_feature_extractor-master
2. cmake CMakeLists.txt 
3. make
4. sudo make
5. cd src
6. sudo make
7. sudo ./kdd99extractor 
8. press Ctrl + C to stop
9. cd ../..


#### Steps for creating pickle file: ####
Run the pickle_generation.py also keep the KDDTrain+.csv in the home directory or adjust the path accordingly.

> Note: Change the name of pickle file accordingly in gui.py depending on classifier used.

 
#### Steps for running the code: ####
1. Copy the kdd99extractor file created after building the kdd99_feature_extractor, pcap_to_csv.py, packetlog.py, gui.py file in home folder only or make proper path changes as required.

2. Run pcap_to_csv file using 
	- sudo python3 pcap_to_csv.py

> Note: Code might run slow, show no output or look like hanging the system depending on classifier used for pickle file generation so wait for atleast 2 minutes.
